# Generated by Django 2.2.2 on 2019-06-21 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20190607_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nova_groups',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='nutrition_grades',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
