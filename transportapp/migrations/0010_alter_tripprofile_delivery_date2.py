# Generated by Django 4.1.2 on 2022-10-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportapp', '0009_auto_20201118_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripprofile',
            name='delivery_date2',
            field=models.DateField(blank=True, null=True),
        ),
    ]