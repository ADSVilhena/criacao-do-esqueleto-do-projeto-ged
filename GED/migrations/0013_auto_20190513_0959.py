# Generated by Django 2.2 on 2019-05-13 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0012_auto_20190513_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anexo',
            old_name='arquivo',
            new_name='file_upload',
        ),
    ]
