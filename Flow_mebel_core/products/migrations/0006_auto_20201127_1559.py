# Generated by Django 3.1.3 on 2020-11-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_merge_20201127_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]