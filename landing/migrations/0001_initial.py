# Generated by Django 2.2 on 2019-07-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('context', models.FloatField(max_length=300, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Подпищики',
            },
        ),
    ]