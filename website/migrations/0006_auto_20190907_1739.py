# Generated by Django 2.2.4 on 2019-09-07 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190211_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='news_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.News'),
        ),
    ]
