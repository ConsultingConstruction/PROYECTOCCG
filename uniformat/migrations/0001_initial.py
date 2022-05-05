# Generated by Django 3.2.13 on 2022-05-02 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UFTCategorias',
            fields=[
                ('idUftCat', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftCat')),
                ('Codigo', models.CharField(max_length=1)),
                ('descriEng', models.CharField(max_length=45)),
                ('descriSpa', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'UFTCategorias',
            },
        ),
        migrations.CreateModel(
            name='UFTNivel2',
            fields=[
                ('idUftN2', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftN2')),
                ('Codigo', models.CharField(max_length=3)),
                ('descriEng', models.CharField(max_length=70)),
                ('descriSpa', models.CharField(max_length=70)),
                ('explicacionEng', models.CharField(max_length=70)),
                ('explicacionSpa', models.CharField(max_length=100)),
                ('fk_UftCat', models.ForeignKey(db_column='fk_UftCat', on_delete=django.db.models.deletion.CASCADE, to='uniformat.uftcategorias', verbose_name='Categoria')),
            ],
            options={
                'db_table': 'UFTNivel2',
            },
        ),
        migrations.CreateModel(
            name='UFTNivel3',
            fields=[
                ('idUftN3', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftN3')),
                ('Codigo', models.CharField(max_length=5)),
                ('descriEng', models.CharField(max_length=150)),
                ('descriSpa', models.CharField(max_length=150)),
                ('explicacionEng', models.CharField(max_length=700)),
                ('explicacionSpa', models.CharField(max_length=800)),
                ('Observaciones', models.CharField(max_length=100)),
                ('fk_UftN2', models.ForeignKey(db_column='fk_UftN2', on_delete=django.db.models.deletion.CASCADE, to='uniformat.uftnivel2', verbose_name='Categoria Nivel 2')),
            ],
            options={
                'db_table': 'UFTNivel3',
            },
        ),
        migrations.CreateModel(
            name='UFTNivel4',
            fields=[
                ('idUftN4', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftN4')),
                ('Codigo', models.CharField(max_length=8)),
                ('descriEng', models.CharField(max_length=200)),
                ('descriSpa', models.CharField(max_length=200)),
                ('explicacionEng', models.CharField(max_length=800)),
                ('explicacionSpa', models.CharField(max_length=800)),
                ('Observaciones', models.CharField(max_length=100)),
                ('fk_UftN3', models.ForeignKey(db_column='fk_UftN3', on_delete=django.db.models.deletion.CASCADE, to='uniformat.uftnivel3', verbose_name='Categoria Nivel 3')),
            ],
            options={
                'db_table': 'UFTNivel4',
            },
        ),
    ]
