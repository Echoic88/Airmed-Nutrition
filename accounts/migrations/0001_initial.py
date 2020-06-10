# Generated by Django 3.0.7 on 2020-06-10 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('MA', 'Male'), ('FE', 'Female')], max_length=2)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pictures')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('receive_email', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]