# Generated by Django 4.0.2 on 2022-02-14 13:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_rename_catergoty_meatproduct_catergoty2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meatproduct',
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 14, 13, 46, 11, 334385, tzinfo=utc)),
        ),
    ]