# Generated by Django 3.2.6 on 2021-09-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.CharField(max_length=1000),
        ),
    ]
