# Generated by Django 3.2.9 on 2021-11-16 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_review_review_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='phoneNumber',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_star',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='space',
            name='contact_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})')]),
        ),
    ]