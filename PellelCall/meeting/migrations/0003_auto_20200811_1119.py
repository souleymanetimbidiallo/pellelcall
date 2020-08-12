# Generated by Django 3.0.8 on 2020-08-11 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meeting', '0002_auto_20200811_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='users',
            field=models.ManyToManyField(related_name='offers', through='meeting.Souscription', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateurs souscrits'),
        ),
        migrations.AlterField(
            model_name='souscription',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='souscriptions', to='meeting.Offer'),
        ),
        migrations.AlterField(
            model_name='souscription',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='souscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
