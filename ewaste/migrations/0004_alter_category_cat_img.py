# Generated by Django 5.0.3 on 2024-03-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewaste', '0003_waste_mat_total_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
