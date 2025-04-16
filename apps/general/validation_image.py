from PIL import Image
from django.core.exceptions import ValidationError


def check_image(value):
    if value:
        img = Image.open(value.image)
        if value.size > 5 * 1024 * 1024:  # 5MB
            raise ValidationError("Rasmning hajmi 5MB dan katta bo'lmasligi kerak.")