# Generated by Django 3.1.4 on 2021-04-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0005_auto_20201226_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
    ]
