from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"

    def _normalize_name(self, name):
        return name
        # try:
        #     return safe_join(self.location, name)
        # except (SuspiciousOperation, ValueError):
        #     return ""

class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False

    def _normalize_name(self, name):
        return name
        # try:
        #     return safe_join(self.location, name)
        # except (SuspiciousOperation, ValueError):
        #     return ""
