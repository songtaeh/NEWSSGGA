
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
                ('title', models.CharField(max_length=100, verbose_name='카페명')),
                ('Explain', models.TextField(max_length=1000, verbose_name='카페설명')),
                ('tag', models.CharField(max_length=30, verbose_name='태그')),
                ('secret', models.BooleanField(verbose_name='공개여부')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='카페아이콘')),
            ],
        ),
    ]
