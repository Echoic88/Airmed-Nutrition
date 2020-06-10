from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    """
    Model for user profile/personal details
    """
    MALE = "MA"
    FEMALE = "FE"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
    )
    profile_pic = models.ImageField(
        upload_to="profile_pictures",
        null=True,
        blank=True,
        max_length=100
    )
    email_confirmed = models.BooleanField(default=False)
    receive_email = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



# from Simple Is Better Than Complex
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# Create a Profile instance along when a User instance is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Modified from Stack Overflow
# https://stackoverflow.com/questions/19287719/remove-previous-image-from-media-folder-when-imagefiled-entry-modified-in-django
@receiver(pre_save, sender=Profile)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Profile.objects.get(pk=instance.pk)
        if instance.profile_pic and \
                existing_image.profile_pic != instance.profile_pic:
            existing_image.profile_pic.delete(False)
