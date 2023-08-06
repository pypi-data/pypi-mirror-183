"""
Abstract base class for scene release databases
"""

import abc
import asyncio
import collections
import copy
import difflib
import os
import re

from ... import constants, errors, utils
from . import SceneCheckResult

import logging  # isort:skip
_log = logging.getLogger(__name__)

natsort = utils.LazyModule(module='natsort', namespace=globals())


class PredbApiBase(abc.ABC):
    """Base class for scene release database APIs"""

    def __init__(self, config=None):
        self._config = copy.deepcopy(self.default_config)
        if config is not None:
            self._config.update(config.items())

    @property
    @abc.abstractmethod
    def name(self):
        """Unique name of the scene release database"""

    @property
    @abc.abstractmethod
    def label(self):
        """User-facing name of the scene release database"""

    @property
    def config(self):
        """
        User configuration

        This is a deep copy of :attr:`default_config` that is updated with the
        `config` argument from initialization.
        """
        return self._config

    @property
    @abc.abstractmethod
    def default_config(self):
        """Default user configuration as a dictionary"""

    @abc.abstractmethod
    async def _search(self, keywords, group=None):
        pass

    async def search(self, query, only_existing_releases=True):
        """
        Search for scene release

        If there are no results and `query` is a directory path that looks like
        a season pack, perform one search per video file in that directory or
        any subdirectory. This is necessary to find mixed season packs.

        :param query: :class:`~.SceneQuery` object or :class:`str` to pass to
            :meth:`~.SceneQuery.from_string` or :class:`collections.abc.Mapping`
            to pass to :meth:`~.SceneQuery.from_release`
        :param bool only_existing_releases: If this is truthy, imaginary season
            pack releases are created and added to the search results.

        :return: :class:`list` of release names as :class:`str`

        :raise RequestError: if the search request fails
        """
        path = None
        if isinstance(query, str):
            path = query
            query = utils.predbs.SceneQuery.from_string(query)
        elif isinstance(query, collections.abc.Mapping):
            query = utils.predbs.SceneQuery.from_release(query)

        results = list(await self._search(query.keywords, group=query.group))
        if not results and path:
            # Maybe `path` points to season pack?
            # Find episodes and search for them individually.
            return await self._search_for_episodes(path, only_existing_releases)
        else:
            return self._postprocess_search_results(results, query, only_existing_releases)

    async def _search_for_episodes(self, path, only_existing_releases):
        combined_results = []
        for episode_query in self._generate_episode_queries(path):
            results = await self.search(episode_query, only_existing_releases)
            combined_results.extend(results)
        return combined_results

    def _generate_episode_queries(self, path):
        info = utils.release.ReleaseInfo(path)
        if info['type'] is utils.release.ReleaseType.season:
            # Create SceneQuery from each episode path
            episode_paths = utils.fs.file_list(path, extensions=constants.VIDEO_FILE_EXTENSIONS)
            for episode_path in episode_paths:
                if not utils.predbs.is_abbreviated_filename(episode_path):
                    _log.debug('Generating query for episode: %r', episode_path)
                    # guessit prefers getting the group name from the parent
                    # directory, but the group in the parent directory is likely
                    # "MiXED", so we definitely want the group from the file.
                    filename = utils.fs.basename(episode_path)
                    yield utils.predbs.SceneQuery.from_string(filename)

    def _postprocess_search_results(self, results, query, only_existing_releases):
        def sorted_and_deduped(results):
            return natsort.natsorted(set(results), key=str.casefold)

        if not query.episodes:
            _log.debug('No episodes queried: %r', query.episodes)
            return sorted_and_deduped(results)
        else:
            _log.debug('Episodes queried: %r', query.episodes)

            def get_wanted_episodes(season):
                # Combine episodes from any season with episodes from given
                # season (season being empty string means "any season")
                eps = None
                if '' in query.episodes:
                    eps = query.episodes['']
                if season in query.episodes:
                    eps = (eps or []) + query.episodes[season]
                return eps

            # Translate single episodes into season packs.
            matches = []
            for result in results:
                for result_season, result_eps in utils.release.Episodes.from_string(result).items():
                    wanted_episodes = get_wanted_episodes(result_season)

                    # [] means season pack
                    if wanted_episodes == []:
                        if only_existing_releases:
                            # Add episode from wanted season pack
                            _log.debug('Adding episode from season pack: %r', result)
                            matches.append(result)
                        else:
                            season_pack = utils.predbs.common.get_season_pack_name(result)
                            _log.debug('Adding season pack: %r', season_pack)
                            matches.append(season_pack)

                    elif wanted_episodes is not None:
                        for ep in result_eps:
                            if ep in wanted_episodes:
                                matches.append(result)
                                break

            return sorted_and_deduped(matches)

    @abc.abstractmethod
    async def _release_files(self, release_name):
        pass

    async def release_files(self, release_name):
        """
        Map release file names to file information

        If this is not implemented by the subclass, :class:`NotImplemented` is
        returned.

        Each file information is a dictionary that contains at least the keys
        ``release_name``, ``file_name`` and ``size``. More keys may be available
        depending on the subclass implementation.

        If `release_name` is a season pack, information the relevant episode
        releases is returned.

        :param str release_name: Exact name of the release

        :raise RequestError: if request fails or `release_name` is not found
        """
        files = await self._release_files(release_name)
        if files is NotImplemented:
            return NotImplemented
        elif files:
            return files
        else:
            _log.debug('No such release: %r', release_name)
            files = {}

        # If scene released "Foo.S01E0{1,2,3,...}.720p.BluRay-BAR" and we're
        # searching for "Foo.S01.720p.BluRay-BAR", we most likely don't get any
        # results. But we can get release names of individual episodes by
        # searching for the season pack, and then we can call release_files()
        # for each episode.
        release_info = utils.release.ReleaseInfo(release_name)
        if release_info['type'] is utils.release.ReleaseType.season:
            results = await self.search(release_info, only_existing_releases=True)
            if results:
                files = await asyncio.gather(
                    *(self._release_files(result) for result in results)
                )

                # Flatten sequence of dictionaries into single dictionary
                files = {
                    file_name: file_info
                    for files_ in files
                    for file_name, file_info in files_.items()
                }
                _log.debug('Season pack from multiple episode releases: %r', files)

        # If scene released season pack (e.g. Extras or Bonus content) and we're
        # searching for a single episode, we most likely don't get any results.
        # Search for the season pack to get all files.
        elif release_info['type'] is utils.release.ReleaseType.episode:
            # Remove single episodes from seasons
            release_info['episodes'].remove_specific_episodes()
            results = await self.search(release_info)
            if len(results) == 1:
                _log.debug('Getting files from single result: %r', results[0])
                files = await self._release_files(results[0])

        # Go through all files and find the exact release name we're looking for.
        # Don't do this exclusively for episodes because not all multi-file releases
        # are a list of episodes (e.g. extras may not contain any "Exx").
        for file_name, file_info in files.items():
            if utils.fs.strip_extension(release_name) == utils.fs.strip_extension(file_name):
                files = {file_name: file_info}
                _log.debug('Single file from season pack release: %r', files)
                break

        return files

    _nogroup_regexs = (
        re.compile(r'^$'),
        re.compile(r'^(?i:nogroup)$'),
        re.compile(r'^(?i:nogrp)$'),
    )

    async def is_scene_release(self, release):
        """
        Return whether `release` is a scene release or not

        .. note:: A renamed or otherwise altered scene release is still
            considered a scene release.

        :param release: Release name, path to release or
            :class:`~.release.ReleaseInfo` instance

        :return: :class:`~.types.SceneCheckResult`
        """
        if isinstance(release, str):
            release_info = utils.release.ReleaseInfo(release)
        else:
            release_info = release

        # Empty group or names like "NOGROUP" are non-scene
        if (
            # Any NOGROUP-equivalent means it's not scene
            any(regex.search(release_info['group']) for regex in self._nogroup_regexs)

            # Abbreviated file names also have an empty group, but ReleaseInfo()
            # can pick up information from the parent directory and we can do a
            # successful search for that.
            and not utils.predbs.is_abbreviated_filename(release_info.path)
        ):
            return SceneCheckResult.false

        # Do we have enough information to pinpoint a single release?
        needed_keys = utils.predbs.common.get_needed_keys(release_info)
        if needed_keys and all(release_info[k] for k in needed_keys):
            # We know which keys we need and all needed keys have values in
            # `release_info`. If there are search results, we have a scene
            # release.
            results = await self.search(release)
            if results:
                return SceneCheckResult.true
            else:
                return SceneCheckResult.false
        else:
            return SceneCheckResult.unknown

    async def verify_release_name(self, content_path, release_name):
        """
        Raise if release was renamed

        :param content_path: Path to release file or directory
        :param release_name: Known exact release name, e.g. from :meth:`search`
            results

        :raise SceneRenamedError: if release was renamed
        :raise SceneError: if `release_name` is not a scene release

        :return: `NotImplemented` if :meth:`release_files` is not implemented,
            `None` otherwise
        """
        _log.debug('Verifying release name: %r =? %r', content_path, release_name)

        if not await self.is_scene_release(release_name):
            raise errors.SceneError(f'Not a scene release: {release_name}')

        content_path = content_path.strip(os.sep)
        files = await self.release_files(release_name)
        if files is NotImplemented:
            return NotImplemented

        # Figure out which file is the actual payload. Note that the release may not
        # contain any files, e.g. Wrecked.2011.DiRFiX.LIMITED.FRENCH.720p.BluRay.X264-LOST.
        main_release_file = None
        if files:
            content_file_extension = utils.fs.file_extension(content_path)
            if content_file_extension:
                # `content_path` points to a file, not a directory
                content_file = utils.fs.basename(content_path)
                # Find the closest match in the released files
                # (`content_file` may have been renamed)
                filename_matches = difflib.get_close_matches(content_file, files)
                if filename_matches:
                    main_release_file = filename_matches[0]

            if not main_release_file and files:
                # Default to the largest file
                main_release_file = sorted(
                    (info for info in files.values()),
                    key=lambda info: info['size'],
                )[0]['file_name']

        # No files in this release, default to `release_name`
        if not main_release_file:
            main_release_file = release_name
        _log.debug('Main release file: %r', main_release_file)

        # Generate set of paths that are valid for this release
        acceptable_paths = {release_name}

        # Properly named directory that contains the released file. This covers
        # abbreviated files and all other files.
        for file in files:
            acceptable_paths.add(os.path.join(release_name, file))

        # Any non-abbreviated files may exist outside of a properly named parent
        # directory
        for file in files:
            if not utils.predbs.is_abbreviated_filename(file):
                acceptable_paths.add(file)

        # If `release_name` is an episode, it may be inside a season pack parent
        # directory. This only matters if we're dealing with an abbreviated file
        # name; normal file names are independent of their parent directory name.
        if utils.predbs.is_abbreviated_filename(content_path):
            season_pack_name = utils.predbs.common.get_season_pack_name(release_name)
            for file in files:
                acceptable_paths.add(f'{season_pack_name}/{file}')

        # Standalone file is also ok if it is named `release_name` with the same
        # file extension as the main file
        main_release_file_extension = utils.fs.file_extension(main_release_file)
        acceptable_paths.add('.'.join((release_name, main_release_file_extension)))

        # Release is correctly named if `content_path` ends with any acceptable path
        for path in (p.strip(os.sep) for p in acceptable_paths):
            if re.search(rf'(?:^|{re.escape(os.sep)}){re.escape(path)}$', content_path):
                return

        # All attempts to match `content_path` against `release_name` have failed.
        # Produce a useful error message.
        if utils.predbs.is_abbreviated_filename(content_path):
            # Abbreviated files should never be handled without a parent
            original_name = os.path.join(release_name, main_release_file)
        elif utils.fs.file_extension(content_path):
            # Assume `content_path` refers to a file, not a directory
            # NOTE: We can't use os.path.isdir(), `content_path` may not exist.
            original_name = main_release_file
        else:
            # Assume `content_path` refers to directory
            original_name = release_name

        # Use the same number of parent directories for original/existing path. If
        # original_name contains the parent directory, we also want the parent
        # directory in existing_name.
        original_name_parts_count = original_name.count(os.sep)
        content_path_parts = content_path.split(os.sep)
        existing_name = os.sep.join(content_path_parts[-original_name_parts_count - 1:])

        raise errors.SceneRenamedError(
            original_name=original_name,
            existing_name=existing_name,
        )

    async def verify_release_files(self, content_path, release_name):
        """
        Check if existing files have the correct size

        :param content_path: Path to release file or directory
        :param release_name: Known exact release name, e.g. from :meth:`search`
            results

        The return value is a sequence of :class:`~.errors.SceneError` exceptions:

            * :class:`~.errors.SceneFileSizeError` if a file has the wrong size
            * :class:`~.errors.SceneMissingInfoError` if the correct file size
              of file cannot be found
            * :class:`~.errors.SceneError` if `release_name` is not a scene release
        """
        exceptions = []

        if not await self.is_scene_release(release_name):
            exceptions.append(errors.SceneError(f'Not a scene release: {release_name}'))
        if exceptions:
            return tuple(exceptions)

        fileinfos = await self.release_files(release_name)
        if fileinfos is NotImplemented:
            return NotImplemented

        def get_release_filesize(filename):
            return fileinfos.get(filename, {}).get('size', None)

        # Map file paths to expected file sizes
        if os.path.isdir(content_path):
            # Map each file in content_path to its correct size
            exp_filesizes = {
                filepath: get_release_filesize(utils.fs.basename(filepath))
                for filepath in utils.fs.file_list(content_path)
            }
        else:
            # `content_path` is file
            if len(fileinfos) == 1:
                # Original release is also a single file, but it may be in a directory
                filename = tuple(fileinfos)[0]
                exp_filesize = get_release_filesize(filename)
                exp_filesizes = {
                    # Title.2015.720p.BluRay.x264-FOO.mkv
                    content_path: exp_filesize,
                    # Title.2015.720p.BluRay.x264-FOO/foo-title.mkv
                    os.path.join(utils.fs.strip_extension(content_path), filename): exp_filesize,
                }
            else:
                # Original release is multiple files (e.g. Extras or Bonus)
                filename = utils.fs.basename(content_path)
                exp_filesizes = {content_path: get_release_filesize(filename)}

        # Compare expected file sizes to actual file sizes
        for filepath, exp_size in exp_filesizes.items():
            filename = utils.fs.basename(filepath)
            actual_size = utils.fs.file_size(filepath)
            _log.debug('Checking file size: %s: %r ?= %r', filename, actual_size, exp_size)
            if exp_size is None:
                _log.debug('No info: %s', filename)
                exceptions.append(errors.SceneMissingInfoError(filename))
            elif actual_size is not None:
                if actual_size != exp_size:
                    _log.debug('Wrong size: %s', filename)
                    exceptions.append(
                        errors.SceneFileSizeError(
                            filename=filename,
                            original_size=exp_size,
                            existing_size=actual_size,
                        )
                    )
                else:
                    _log.debug('Correct size: %s', filepath)
            else:
                _log.debug('No such file: %s', filepath)

        return tuple(e for e in exceptions if e)

    async def verify_release(self, content_path, release_name=None):
        """
        Find matching scene releases and apply :meth:`verify_release_name`
        and :meth:`verify_release_files`

        :param content_path: Path to release file or directory
        :param release_name: Known exact release name or `None` to
            :meth:`search` for `content_path`

        :return: :class:`~.types.SceneCheckResult` enum from
            :meth:`is_scene_release` and sequence of
            :class:`~.errors.SceneError` exceptions from
            :meth:`verify_release_name` and :meth:`verify_release_files`
        """
        # If we know the exact release name, this is easy.
        if release_name:
            return await self._verify_release(content_path, release_name)

        # Find possible `release_name` values. For season packs that were released
        # as single episodes, this will get us a sequence of episode release names.
        existing_release_names = await self.search(content_path)
        if not existing_release_names:
            return SceneCheckResult.false, ()

        # Maybe `content_path` was released by scene as it is (as file or directory)
        for existing_release_name in existing_release_names:
            is_scene_release, exceptions = await self._verify_release(content_path, existing_release_name)
            if is_scene_release and not exceptions:
                return SceneCheckResult.true, ()

        # Maybe `content_path` is a directory (season pack) and scene released
        # single files (episodes).
        return await self._verify_release_per_file(content_path)

    async def _verify_release(self, content_path, release_name):
        _log.debug('Verifying %r against release: %r', content_path, release_name)

        # Stop other checks if this is not a scene release
        is_scene = await self.is_scene_release(release_name)
        if not is_scene:
            return SceneCheckResult.false, ()

        # Combined exceptions from verify_release_name() and verify_release_files()
        exceptions = []

        # verify_release_name() can only produce one exception, so it is raised
        try:
            await self.verify_release_name(content_path, release_name)
        except errors.SceneError as e:
            exceptions.append(e)

        # verify_release_files() can produce multiple exceptions, so it returns them
        exceptions.extend(await self.verify_release_files(content_path, release_name))
        return is_scene, tuple(exceptions)

    async def _verify_release_per_file(self, content_path):
        _log.debug('Verifying each file beneath %r', content_path)
        is_scene_releases = []
        combined_exceptions = collections.defaultdict(lambda: [])
        filepaths = utils.fs.file_list(content_path, extensions=constants.VIDEO_FILE_EXTENSIONS)
        for filepath in filepaths:
            existing_release_names = await self.search(filepath)
            _log.debug('Search results for %r: %r', filepath, existing_release_names)

            # If there are no search results, default to "not a scene release"
            is_scene_release = SceneCheckResult.false

            # Match each existing_release_name against filepath
            for existing_release_name in existing_release_names:
                is_scene_release, exceptions = await self._verify_release(filepath, existing_release_name)
                _log.debug('Verified %r against %r: %r, %r',
                           filepath, existing_release_name, is_scene_release, exceptions)
                if is_scene_release and not exceptions:
                    # Match found, don't check other existing_release_names
                    break
                elif is_scene_release:
                    # Remember exceptions per file (makes debugging easier)
                    combined_exceptions[filepath].extend(exceptions)

            # Remember the SceneCheckResult when the for loop ended. True if we
            # found a scene release at any point, other it's the value of the last
            # existing_release_name.
            is_scene_releases.append(is_scene_release)

        # Collapse `is_scene_releases` into a single value
        if is_scene_releases and all(isr is SceneCheckResult.true for isr in is_scene_releases):
            _log.debug('All files are scene releases')
            is_scene_release = SceneCheckResult.true
        elif is_scene_releases and all(isr is SceneCheckResult.false for isr in is_scene_releases):
            _log.debug('All files are non-scene releases')
            is_scene_release = SceneCheckResult.false
        else:
            _log.debug('Uncertain scene status: %r', is_scene_releases)
            is_scene_release = SceneCheckResult.unknown

        return is_scene_release, tuple(
            exception
            for exceptions in combined_exceptions.values()
            for exception in exceptions
        )


class MultiPredbApi:
    """
    Wrapper around multiple :class:`~.PredbApiBase` instances

    Each method loops over every provided predb and calls the same method on
    it. The first call that does not raise :class:`~.RequestError` and does not
    return `NotImplemented` is returned.

    If no call succeeds and any exceptions were raised, they are combined into a
    single :class:`~.RequestError`, which is raised. If every call returned
    `NotImplemented`, `NotImplemented` is returned.

    :param predbs: Sequence of :class:`~.PredbApiBase` instances
    """

    DEFAULT_PREDB_NAMES = ('predbde', 'srrdb')

    def __init__(self, predbs=None):
        if predbs:
            self._predbs = predbs
        else:
            self._predbs = [
                utils.predbs.predb(name)
                for name in type(self).DEFAULT_PREDB_NAMES
            ]

    async def search(self, *args, **kwargs):
        """See :meth:`~.PredbApiBase.search`"""
        return await self._for_each_predb('search', *args, **kwargs)

    async def release_files(self, *args, **kwargs):
        """See :meth:`~.PredbApiBase.release_files`"""
        return await self._for_each_predb('release_files', *args, **kwargs)

    async def is_scene_release(self, *args, **kwargs):
        """See :meth:`~.PredbApiBase.is_scene_release`"""
        return await self._for_each_predb('is_scene_release', *args, **kwargs)

    async def verify_release_name(self, *args, **kwargs):
        """See :meth:`~.PredbApiBase.verify_release_name`"""
        return await self._for_each_predb('verify_release_name', *args, **kwargs)

    async def verify_release_files(self, *args, **kwargs):
        """See :meth:`~.PredbApiBase.verify_release_files`"""
        return await self._for_each_predb('verify_release_files', *args, **kwargs)

    async def verify_release(self, *args, **kwargs):
        """See :meth:`~.PredbApiBase.verify_release`"""
        return await self._for_each_predb('verify_release', *args, **kwargs)

    async def _verify_release(self, *args, **kwargs):
        return await self._for_each_predb('_verify_release', *args, **kwargs)

    async def _verify_release_per_file(self, *args, **kwargs):
        return await self._for_each_predb('_verify_release_per_file', *args, **kwargs)

    async def _for_each_predb(self, method_name, *args, **kwargs):
        # Call the same method on multiple PredbApiBase instances until one
        # does not raise RequestError and does not return NotImplemented.
        exceptions = []
        for predb in self._predbs:
            method = getattr(predb, method_name)
            _log.debug('Trying %r: %r', predb.name, method)
            try:
                result = await method(*args, **kwargs)
            except errors.RequestError as e:
                _log.debug('Collecting scene search error: %r', e)
                exceptions.append(e)
            else:
                if result is not NotImplemented:
                    return result

        if not exceptions:
            return NotImplemented
        elif len(exceptions) == 1:
            raise exceptions[0]
        else:
            raise errors.RequestError(
                'All queries failed: ' + ', '.join(str(e) for e in exceptions)
            )
