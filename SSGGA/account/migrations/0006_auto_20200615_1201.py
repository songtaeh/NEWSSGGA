# Generated by Django 3.0.7 on 2020-06-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200615_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/user_default_img.png', null=True, upload_to='', verbose_name='(선택) 프로필사진'),
        ),
    ]