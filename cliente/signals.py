from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Cliente

@receiver(post_delete, sender=Cliente)
def delete_usuario(sender, instance, **kwargs):
    if instance.usuario:
        instance.usuario.delete()