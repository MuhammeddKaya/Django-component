# Generated by Django 4.1.7 on 2023-02-21 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LanguageCode', models.CharField(max_length=10, verbose_name='Dil Kodu')),
                ('LanguageName', models.CharField(max_length=100, verbose_name='Dil Adi')),
                ('IsActive', models.BooleanField(default=True, verbose_name='Aktif')),
            ],
            options={
                'db_table': 'Language',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TemplateName', models.CharField(max_length=80, verbose_name='Template Adı')),
                ('IsActive', models.BooleanField(default=False, verbose_name='Aktif')),
            ],
            options={
                'db_table': 'Template',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubdomainName', models.CharField(max_length=100, verbose_name='Domain')),
                ('IsActive', models.BooleanField(default=True, verbose_name='Aktif')),
                ('Template', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genaralApp.template', verbose_name='Template')),
            ],
            options={
                'db_table': 'Domain',
            },
        ),
    ]