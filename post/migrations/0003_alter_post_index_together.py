# Generated by Django 3.2.7 on 2021-09-21 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210921_2015'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='post',
            index_together={('id', 'slug')},
        ),
    ]
