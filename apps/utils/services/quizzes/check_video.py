from django.utils.translation import gettext_lazy as _
from apps.utils.custom_exception import CustomAPIException


def validate_video(video):
    """ check a valid video """
    max_size = 50 * 1024 * 1024  # 50 MB
    if video.size > max_size:
        raise CustomAPIException(_(f"Video size should not exceed {max_size / (1024 * 1024)} MB."))
