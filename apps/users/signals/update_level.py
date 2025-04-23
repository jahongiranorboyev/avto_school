from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.general.models import Level
from apps.users.models import CustomUser

@receiver(post_save, dispatch_uid="update_user_level")
def update_user_level(sender, instance, **kwargs):
    if isinstance(instance, CustomUser):
        post_save.disconnect(update_user_level, sender=CustomUser)

        try:
            levels = Level.objects.order_by('coins')
            if not levels.exists():
                return

            for level in levels:
                if instance.coins < level.coins:
                    break
                instance.level = level

            # CustomUser.objects.filter(pk=instance.pk).update(level=instance.level)
            instance.save(update_fields=['level'])
        finally:
            post_save.connect(update_user_level, sender=CustomUser, dispatch_uid="update_user_level")

    elif isinstance(instance, Level):
        post_save.disconnect(update_user_level, sender=Level)

        try:
            levels = Level.objects.order_by('coins')
            users = CustomUser.objects.all()

            for user in users:
                for level in levels:
                    if user.coins < level.coins:
                        break
                    user.level = level
                # CustomUser.objects.filter(pk=user.pk).update(level=user.level)
                user.save(update_fields=['level'])
        finally:
            post_save.connect(update_user_level, sender=Level, dispatch_uid="update_user_level")