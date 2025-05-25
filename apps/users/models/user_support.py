from django.db import models

from apps.utils.models.base_model import BaseModel


class Support(BaseModel):
    class Report(models.TextChoices):
        APP_USE = 'App use', 'Basic app usage and feature'
        ACCOUNT = 'Account', 'Login and account settings.'
        PAYMENT = 'Payment', 'Subscription & payment'
        STUDY_CONTENT = 'Study content', 'About learning materials'
        APP_ISSUES = 'App issues', 'Report bugs or problems'
        OTHER = 'Other', 'For any other queries'


    email = models.EmailField()
    report = models.CharField(max_length=100, default=Report.OTHER, choices=Report)
    message = models.CharField(max_length=150, blank=True, null=True)


    def __str__(self):
        return self.message