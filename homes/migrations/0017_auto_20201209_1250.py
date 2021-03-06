# Generated by Django 3.1.4 on 2020-12-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0016_auto_20201209_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='bathrooms',
            field=models.CharField(blank=True, choices=[('1', '1'), ('5', '5'), ('8', '8'), ('2', '2'), ('9', '9'), ('4', '4'), ('7', '7'), ('6', '6'), ('3', '3'), ('0', '0')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='bedrooms',
            field=models.CharField(blank=True, choices=[('1', '1'), ('5', '5'), ('8', '8'), ('2', '2'), ('9', '9'), ('4', '4'), ('7', '7'), ('6', '6'), ('3', '3'), ('0', '0')], max_length=300),
        ),
        migrations.AlterField(
            model_name='upload',
            name='numberOfImages',
            field=models.CharField(choices=[('1', '1'), ('5', '5'), ('8', '8'), ('10', '10'), ('2', '2'), ('9', '9'), ('4', '4'), ('7', '7'), ('6', '6'), ('3', '3'), ('0', '0')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='parking',
            field=models.CharField(blank=True, choices=[('1', '1'), ('5', '5'), ('8', '8'), ('2', '2'), ('9', '9'), ('4', '4'), ('7', '7'), ('6', '6'), ('3', '3'), ('0', '0')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='toilets',
            field=models.CharField(blank=True, choices=[('1', '1'), ('5', '5'), ('8', '8'), ('2', '2'), ('9', '9'), ('4', '4'), ('7', '7'), ('6', '6'), ('3', '3'), ('0', '0')], max_length=30),
        ),
    ]
