# Generated by Django 3.0.3 on 2020-02-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0004_inventory_item_iteminstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminstance',
            name='data',
            field=models.TextField(default='{}'),
        ),
    ]
