# Generated by Django 5.1.4 on 2024-12-09 14:21

import django.db.models.deletion
import goods.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('is_published', models.BooleanField(default=True, verbose_name='Отображать')),
                ('image', models.ImageField(upload_to=goods.models.BaseGoodModel.upload_path)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('is_published', models.BooleanField(default=True, verbose_name='Отображать')),
                ('image', models.ImageField(upload_to=goods.models.BaseGoodModel.upload_path)),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Количество на складе')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('discount', models.PositiveSmallIntegerField(default=0, verbose_name='Скидка в %')),
                ('rating', models.DecimalField(decimal_places=1, default=2.5, max_digits=2, verbose_name='Оценка товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'db_table': 'product',
            },
        ),
    ]
