# Generated by Django 2.2 on 2019-05-27 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('nascimento', models.DateField()),
                ('rg', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=14)),
                ('sexo_choices', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Graduação', 'Graduação'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'), ('Extensão', 'Extensão'), ('Certificação', 'Certificação')], max_length=15)),
                ('nome_curso', models.CharField(max_length=50)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colaboraApp.Colaborador')),
            ],
        ),
    ]
