from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models.base_model import BaseModel


class Support(BaseModel):

    class Report(models.TextChoices):
        APP_USE = 'app_use', _('Basic app usage and feature')
        ACCOUNT = 'account', _('Login and account settings.')
        PAYMENT = 'payment', _('Subscription & payment')
        STUDY_CONTENT = 'study_content', _('About learning materials')
        APP_ISSUES = 'app_issues', _('Report bugs or problems')
        OTHER = 'other', _('For any other queries')

    email = models.EmailField()
    report = models.CharField(max_length=100, default=Report.OTHER)
    message = models.CharField(max_length=150, blank=True, null=True)