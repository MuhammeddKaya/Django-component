# Generated by Django 4.1.7 on 2023-02-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_isactive_pages_isenable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pages',
            name='PageFather',
        ),
    ]