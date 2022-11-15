# Generated by Django 4.1.3 on 2022-11-15 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiaresapp', '0004_alter_familia_edad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Primos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('parentesco', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.IntegerField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('parentesco', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.IntegerField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]