# Generated by Django 3.1.4 on 2021-01-22 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_review_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='createdAt',
        ),
    ]
