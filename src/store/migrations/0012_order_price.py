# Generated by Django 3.1.6 on 2022-09-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]