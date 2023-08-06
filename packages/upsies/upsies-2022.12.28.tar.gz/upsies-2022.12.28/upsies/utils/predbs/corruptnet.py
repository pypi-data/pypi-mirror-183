import time
from base64 import b64decode

from . import base
from .. import http

import logging  # isort:skip
_log = logging.getLogger(__name__)

# https://pre.corrupt-net.org/search.php?search=wrecked+2011&ts=1671622472280&pretimezone=0&timezone=0

class CorruptnetApi(base.PredbApiBase):
    name = 'corruptnet'
    label = 'pre.corrupt-net.org'

    default_config = {}

    _url_base = b64decode('aHR0cHM6Ly9wcmUuY29ycnVwdC1uZXQub3Jn').decode('ascii')
    _search_url = f'{_url_base}/search.php'

    def _join_keywords(self, keywords, group):
        kws = ' '.join(keywords)
        if group:
            kws += f' group:{group}'
        return kws

    async def _search(self, keywords, group):
        params = {
            'search': self._join_keywords(keywords, group),
            # Current time in milliseconds
            'ts': int(time.time() * 1000),
            # Not sure what these are
            'pretimezone': 0,
            'timezone': 0,
        }

        # _log.debug('%s search: %r, %r', self.label, self._search_url, params)
        # response = await http.get(self._search_url, params=params, cache=True, verify=False)
        # with open('corrupt.net.html', 'w') as f:
        #     f.write(response)

        with open('corrupt.net.html', 'r') as f:
            response = f.read()

        self._


#     def _get_params(self, keywords, group):
#         if group:
#             keywords = list(keywords)
#             keywords.extend(('@team', str(group).replace('@', r'\@').strip()))
#         kws = (str(kw).lower().strip() for kw in keywords)
#         return ' '.join(kw for kw in kws if kw)

#     async def _request_all_pages(self, q):
#         combined_results = []

#         # We can request 30 pages per minute before we get an error
#         for page in range(1, 31):
#             results, next_page = await self._request_page(q, page)
#             combined_results.extend(results)

#             # Negative next page means last page
#             if next_page < 0:
#                 break

#         return combined_results

#     async def _request_page(self, q, page):
#         params = {
#             'q': q,
#             'count': 100,
#             'page': page,
#         }
#         _log.debug('%s search: %r, %r', self.label, self._search_url, params)
#         response = (await http.get(self._search_url, params=params, cache=True)).json()

#         # Report API error or return list of release names
#         if response['status'] != 'success':
#             raise errors.RequestError(f'{self.label}: {response["message"]}')
#         else:
#             # Extract release names
#             results = tuple(result['name'] for result in response['data']['rows'])

#             # Is there another page of results?
#             if len(results) >= response['data']['reqCount']:
#                 next_page = page + 1
#             else:
#                 next_page = -1

#             return results, next_page

    async def _release_files(self, release_name):
        """Always return an empty :class:`dict`"""
        return NotImplemented
