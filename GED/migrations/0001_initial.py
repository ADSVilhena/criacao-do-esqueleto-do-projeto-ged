# Generated by Django 2.2 on 2019-04-02 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ramal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GED.Departamento')),
                ('funcao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GED.Funcao')),
            ],
        ),
    ]
