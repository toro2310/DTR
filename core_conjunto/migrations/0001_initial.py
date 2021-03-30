# Generated by Django 3.1 on 2021-03-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administracion',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='porteria',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='residente',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('num_apartamEnto', models.CharField(max_length=5)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]