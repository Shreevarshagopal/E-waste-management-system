# Generated by Django 5.0.3 on 2024-03-30 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewaste', '0005_alter_total_cat_waste_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_cat',
            name='cat_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ewaste.category'),
            preserve_default=False,
        ),
    ]
