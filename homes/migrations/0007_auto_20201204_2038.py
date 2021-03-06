# Generated by Django 3.1.3 on 2020-12-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0006_auto_20201204_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='bathrooms',
            field=models.CharField(blank=True, choices=[('4', '4'), ('3', '3'), ('2', '2'), ('7', '7'), ('9', '9'), ('0', '0'), ('5', '5'), ('8', '8'), ('1', '1'), ('6', '6')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='bedrooms',
            field=models.CharField(blank=True, choices=[('4', '4'), ('3', '3'), ('2', '2'), ('7', '7'), ('9', '9'), ('0', '0'), ('5', '5'), ('8', '8'), ('1', '1'), ('6', '6')], max_length=300),
        ),
        migrations.AlterField(
            model_name='upload',
            name='parking',
            field=models.CharField(blank=True, choices=[('4', '4'), ('3', '3'), ('2', '2'), ('7', '7'), ('9', '9'), ('0', '0'), ('5', '5'), ('8', '8'), ('1', '1'), ('6', '6')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='toilets',
            field=models.CharField(blank=True, choices=[('4', '4'), ('3', '3'), ('2', '2'), ('7', '7'), ('9', '9'), ('0', '0'), ('5', '5'), ('8', '8'), ('1', '1'), ('6', '6')], max_length=30),
        ),
    ]
