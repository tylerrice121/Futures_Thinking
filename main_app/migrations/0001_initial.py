# Generated by Django 3.2.9 on 2021-12-01 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('entry', models.CharField(max_length=350)),
                ('img', models.CharField(blank=True, max_length=250)),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AllEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_entries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.userentries')),
            ],
        ),
    ]