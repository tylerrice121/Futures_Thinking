# Generated by Django 3.2.9 on 2021-12-02 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentries',
            name='relevant_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=350),
            preserve_default=False,
        ),
    ]