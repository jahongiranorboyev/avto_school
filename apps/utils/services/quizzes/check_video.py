from rest_framework.exceptions import ValidationError


def validate_video(video):
    max_size = 50 * 1024 * 1024  # 50 MB
    if video.size > max_size:
        raise ValidationError(f"Video size should not exceed {max_size / (1024 * 1024)} MB.")
