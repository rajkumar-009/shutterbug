# Generated by Django 3.2.4 on 2021-06-16 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_delete_photoshootsession'),
        ('home', '0002_auto_20210614_1112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Photographer',
        ),
    ]
