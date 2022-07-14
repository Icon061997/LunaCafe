# Generated by Django 4.0.2 on 2022-02-14 13:10

import backend.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_delete_productmeat_alter_user_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meatproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_image', models.ImageField(default='profile_pic/image.jpg', upload_to=backend.models.image_path)),
                ('pro_id', models.CharField(max_length=50, unique=True, verbose_name='Product id')),
                ('pro_name', models.CharField(max_length=200, verbose_name='Product name')),
                ('pro_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pro_size', models.CharField(max_length=200, verbose_name='Size')),
                ('Catergoty', models.CharField(max_length=200, verbose_name='Catergory')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 14, 13, 10, 55, 807980, tzinfo=utc)),
        ),
    ]