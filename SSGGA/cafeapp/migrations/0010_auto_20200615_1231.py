# Generated by Django 3.0.7 on 2020-06-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0009_auto_20200615_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='image',
            field=models.ImageField(default='images/user_default_img.png', null=True, upload_to='', verbose_name='카페 아이콘'),
        ),
    ]