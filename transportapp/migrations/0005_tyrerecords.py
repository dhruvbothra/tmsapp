# Generated by Django 3.1.3 on 2020-11-17 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transportapp', '0004_auto_20201116_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='TyreRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truckno', models.CharField(default=None, max_length=100)),
                ('tyre_date', models.DateField()),
                ('tyre_brand', models.CharField(max_length=200)),
                ('tyre_model', models.CharField(max_length=100)),
                ('tyre_number', models.CharField(max_length=100)),
                ('tyre_price', models.FloatField()),
                ('km_reading', models.FloatField()),
                ('tyre_status', models.CharField(max_length=30)),
                ('tyre_description', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]