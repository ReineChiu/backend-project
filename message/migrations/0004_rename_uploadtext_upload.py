# Generated by Django 4.1.5 on 2023-01-12 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_uploadtext_file_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadText',
            new_name='Upload',
        ),
    ]
