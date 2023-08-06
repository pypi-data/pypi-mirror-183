import re

from functools import wraps

from .exceptions import SwarmCompatibleError, SwarmError


def minimal_version(version):
    def wrapper(f):
        @wraps(f)
        def _check_version(self, *args, **kwargs):
            if hasattr(self, 'swarm'):
                current_version = self.swarm.version
            else:
                current_version = self.version

            if float(current_version) >= float(version):
                return f(self, *args, **kwargs)

            raise SwarmCompatibleError(
                'Unsupported with API v{} (needed v{}+)'.format(
                    current_version,
                    version
                )
            )

        return _check_version
    return wrapper


def get_review_id(review_url: str) -> int:
    ret = re.compile(r'/(\d+)').findall(review_url)
    if not ret:
        raise SwarmError('Invalid review: ' + review_url)

    return int(ret[0])
