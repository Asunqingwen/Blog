# Generated by Django 2.2.7 on 2019-11-26 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('nick_name', models.CharField(max_length=10)),
                ('user_email', models.EmailField(max_length=20)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
