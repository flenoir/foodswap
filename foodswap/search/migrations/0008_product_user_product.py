# Generated by Django 2.2.2 on 2019-06-25 19:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0007_product_substitutes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_product',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]