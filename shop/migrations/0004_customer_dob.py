# Generated by Django 3.1.2 on 2020-11-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
