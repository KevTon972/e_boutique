# Generated by Django 3.1.7 on 2022-08-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_sneaker_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=39)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='sneaker_size',
        ),
        migrations.AddField(
            model_name='product',
            name='sneaker_size',
            field=models.ManyToManyField(to='store.Size'),
        ),
    ]
