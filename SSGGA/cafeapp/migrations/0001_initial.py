# Generated by Django 3.0.6 on 2020-06-14 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='카페명')),
                ('explain', models.TextField(max_length=1000, null=True, verbose_name='카페 설명')),
                ('tag', models.CharField(max_length=30, verbose_name='태그')),
                ('secret', models.BooleanField(verbose_name='공개여부')),
                ('image', models.ImageField(default='./images/userdefaultimg.png', null=True, upload_to='', verbose_name='카페 아이콘')),
                ('adminuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
