# Generated by Django 3.1.2 on 2020-12-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20201203_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.CharField(default='New', max_length=10),
        ),
    ]
