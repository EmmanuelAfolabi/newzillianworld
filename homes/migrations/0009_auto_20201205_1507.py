# Generated by Django 3.1.3 on 2020-12-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0008_auto_20201205_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='bathrooms',
            field=models.CharField(blank=True, choices=[('5', '5'), ('3', '3'), ('6', '6'), ('2', '2'), ('0', '0'), ('1', '1'), ('9', '9'), ('4', '4'), ('8', '8'), ('7', '7')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='bedrooms',
            field=models.CharField(blank=True, choices=[('5', '5'), ('3', '3'), ('6', '6'), ('2', '2'), ('0', '0'), ('1', '1'), ('9', '9'), ('4', '4'), ('8', '8'), ('7', '7')], max_length=300),
        ),
        migrations.AlterField(
            model_name='upload',
            name='parking',
            field=models.CharField(blank=True, choices=[('5', '5'), ('3', '3'), ('6', '6'), ('2', '2'), ('0', '0'), ('1', '1'), ('9', '9'), ('4', '4'), ('8', '8'), ('7', '7')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='toilets',
            field=models.CharField(blank=True, choices=[('5', '5'), ('3', '3'), ('6', '6'), ('2', '2'), ('0', '0'), ('1', '1'), ('9', '9'), ('4', '4'), ('8', '8'), ('7', '7')], max_length=30),
        ),
    ]