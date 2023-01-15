# Generated by Django 4.1.5 on 2023-01-12 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_rename_uploadtext_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
