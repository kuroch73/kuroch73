# Generated by Django 4.2.5 on 2023-09-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='blog/image/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(verbose_name='Доп.источник'),
        ),
    ]
