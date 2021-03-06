# Generated by Django 2.2 on 2019-05-01 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GED', '0007_auto_20190430_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pessoa_dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pessoa_doc_dono', to='GED.Pessoa', verbose_name='Referente a'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='pessoa_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pessoa_doc_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Responsável'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='GED.Departamento'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='funcao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='GED.Funcao'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
