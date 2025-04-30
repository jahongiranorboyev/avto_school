from PIL import Image
from django.core.exceptions import ValidationError

def check_image(value):
    if value:
        try:
            Image.open(value)
            if value.size > 5 * 1024 * 1024:
                raise ValidationError("Rasmning hajmi 5MB dan katta bo'lmasligi kerak.")
        except IOError:
            raise ValidationError("Rasmni o'qishda xato yuz berdi.")
