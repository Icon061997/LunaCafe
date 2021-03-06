# Generated by Django 4.0.2 on 2022-03-04 11:51

import backend.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_image',
            field=models.ImageField(blank=True, default='profile_pic/image.jpg', null=True, upload_to=backend.models.image_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 4, 11, 51, 17, 585207, tzinfo=utc)),
        ),
    ]
