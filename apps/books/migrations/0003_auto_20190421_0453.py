# Generated by Django 2.2 on 2019-04-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookprogress_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookprogress',
            name='pages_read',
            field=models.PositiveIntegerField(default=0, verbose_name='Pages read'),
        ),
    ]
