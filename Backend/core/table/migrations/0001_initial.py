# Generated by Django 3.2.7 on 2021-12-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('distance', models.PositiveIntegerField(default=0, verbose_name='Дистанция')),
            ],
            options={
                'verbose_name': 'Таблица',
                'verbose_name_plural': 'Таблицы',
            },
        ),
    ]