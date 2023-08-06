"""
Concrete :class:`~.base.TrackerJobsBase` subclass for PTP
"""

from ...utils import cached_property
from ..base import TrackerJobsBase

import logging  # isort:skip
_log = logging.getLogger(__name__)


class PtpTrackerJobs(TrackerJobsBase):

    @cached_property
    def jobs_before_upload(self):
        return (
            # Background jobs

            # Interactive jobs
        )
