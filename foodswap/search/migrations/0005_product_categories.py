# Generated by Django 2.2.2 on 2019-06-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_remove_product_nutrition_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
