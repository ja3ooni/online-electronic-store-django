# Generated by Django 3.1.2 on 2020-12-03 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_product_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='dob',
        ),
    ]
