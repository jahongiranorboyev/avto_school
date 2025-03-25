from django.core.exceptions import ValidationError
from PIL import Image

def validate_image_size(image):
    img = Image.open(image)
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError("Max image size is 5MB.")