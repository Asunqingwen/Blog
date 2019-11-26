# Generated by Django 2.2.7 on 2019-11-26 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20191126_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_list', to='userapp.User', verbose_name='作者'),
        ),
    ]
