# Generated by Django 3.0.7 on 2020-06-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='SSGGA/static/img/userimg.png', null=True, upload_to='', verbose_name='(선택) 프로필사진'),
        ),
    ]