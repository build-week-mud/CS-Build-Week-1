# Generated by Django 3.0.3 on 2020-02-04 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20200204_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='room',
            name='e_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='e_room', to='adventure.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='n_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='n_room', to='adventure.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='s_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='s_room', to='adventure.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='w_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='w_room', to='adventure.Room'),
        ),
    ]
