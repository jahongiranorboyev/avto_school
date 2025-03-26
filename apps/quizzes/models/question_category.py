from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
from apps.utils.models import BaseModel
from apps.utils.services.quizzes.check_image import validate_image


class QuestionCategory(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100,
        editable=False
    )
    image = models.ImageField(
        upload_to='question_categories/%Y/%m/%d',
        validators=[validate_image]
    )
    is_premium = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        if not self.slug:
            self.slug = slugify(self.title)

        if QuestionCategory.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError("A question category with this slug already exists")

    def __str__(self):
        return self.title


