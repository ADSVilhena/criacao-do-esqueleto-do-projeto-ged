# Generated by Django 2.1.7 on 2019-05-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0008_auto_20190501_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='descricao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
