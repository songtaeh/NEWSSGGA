# Generated by Django 3.0.6 on 2020-06-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='카페이름')),
                ('Explain', models.TextField(verbose_name='카페설명')),
                ('tag', models.CharField(max_length=30, verbose_name='태그')),
                ('secret', models.BooleanField(verbose_name='공개여부')),
            ],
        ),
    ]
