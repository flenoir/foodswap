# Generated by Django 2.2.2 on 2019-06-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.CharField(max_length=500, null=True),
        ),
    ]