from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


def avatar_path(elem: "Profile", filename: str) -> str:

    return f"avatar/user_{elem.user.pk}/{filename}"


class Profile(models.Model):
    POSITION_CHOICES = [
        ("Оператор", "Оператор"),
        ("Маркетолог", "Маркетолог"),
        ("Менеджер", "Менеджер"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, blank=True, choices=POSITION_CHOICES)
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_path)

    def __str__(self) -> str:
        return f"Profile(pk={self.pk}, user={self.user!r})"


@receiver(post_save, sender=Profile)
def assign_group(sender, instance, created, **kwargs):
    if created and instance.position in ["Оператор", "Маркетолог", "Менеджер"]:
        group, _ = Group.objects.get_or_create(name=instance.position + "ы")
        instance.user.groups.add(group)
