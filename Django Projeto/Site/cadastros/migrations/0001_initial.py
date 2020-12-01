# Generated by Django 2.2.10 on 2020-11-28 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50, unique=True, verbose_name='Endereço')),
                ('telefone', models.IntegerField()),
                ('email', models.CharField(max_length=50, unique=True)),
                ('cpf', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50, unique=True, verbose_name='Endereço')),
                ('telefone', models.IntegerField()),
                ('email', models.CharField(max_length=50, unique=True)),
                ('cpf', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=50)),
                ('qtd', models.IntegerField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Funcionario')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Pessoa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
