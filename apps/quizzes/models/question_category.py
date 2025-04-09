from django.db import models
from apps.utils.models import BaseModel
from django.core.validators import MinValueValidator
from apps.utils.services.quizzes.check_image import validate_image


class QuestionCategory(BaseModel):
    title = models.CharField(max_length=100)
    question_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(
        upload_to='question_categories/%Y/%m/%d',
        validators=[validate_image]
    )
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title
