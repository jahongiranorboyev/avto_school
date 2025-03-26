from rest_framework.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def validate_image(image):
    max_width = 1920
    max_height = 1080
    max_size = 5 * 1024 * 1024

    width, height = get_image_dimensions(image)
    if width > max_width or height > max_height:
        raise ValidationError(f"Image dimensions should not exceed {max_width}x{max_height} pixels.")

    if image.size > max_size:
        raise ValidationError(f"Image size should not exceed {max_size / (1024 * 1024)} MB.")

