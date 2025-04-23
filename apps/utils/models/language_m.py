from django.db import models
from django.conf import settings
from django.core.cache import cache

from apps.utils.models import BaseModel


class CustomLanguage(BaseModel):

    CACHE_KEY = 'cached_languages'

    code = models.CharField(max_length=200, unique=True, choices=settings.LANGUAGES)
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=False)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @classmethod
    def languages(cls):
        from apps.utils.serializers import LanguageSerializer
        langs = cache.get('cached_languages')
        if langs is None:
            langs = cls.objects.filter(is_active=True).order_by(
                'ordering').values(*LanguageSerializer.Meta.fields)
            cache.set(cls.CACHE_KEY, list(langs), 60 * 60 * 24)

        return langs