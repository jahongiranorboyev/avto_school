from django.db import models

from apps.utils.models.base_model import BaseModel


class Support(BaseModel):
    class Report(models.TextChoices):
        APP_USE = 'app_use', 'Basic app usage and feature'
        ACCOUNT = 'account', 'Login and account settings.'
        PAYMENT = 'payment', 'Subscription & payment'
        STUDY_CONTENT = 'study_content', 'About learning materials'
        APP_ISSUES = 'app_issues', 'Report bugs or problems'
        OTHER = 'other', 'For any other queries'


    email = models.EmailField()
    report = models.CharField(max_length=100, default=Report.OTHER)
    message = models.CharField(max_length=150, blank=True, null=True)


