from django.db.models.signals import pre_save
from django.dispatch import receiver

from accounts.models import CustomUser


@receiver(pre_save, sender=CustomUser)
def admin_superuser(sender, instance, **kwargs):
    if instance.is_superuser:
        instance.role = 'admin'
