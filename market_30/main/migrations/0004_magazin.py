# Generated by Django 4.0.4 on 2022-05-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('products', models.ManyToManyField(to='main.product')),
            ],
        ),
    ]
