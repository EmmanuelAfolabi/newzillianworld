# Generated by Django 3.1.3 on 2020-12-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0010_auto_20201205_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='image10',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='upload',
            name='image7',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='upload',
            name='image8',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='upload',
            name='image9',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='bathrooms',
            field=models.CharField(blank=True, choices=[('0', '0'), ('4', '4'), ('7', '7'), ('3', '3'), ('2', '2'), ('1', '1'), ('8', '8'), ('9', '9'), ('6', '6'), ('5', '5')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='bedrooms',
            field=models.CharField(blank=True, choices=[('0', '0'), ('4', '4'), ('7', '7'), ('3', '3'), ('2', '2'), ('1', '1'), ('8', '8'), ('9', '9'), ('6', '6'), ('5', '5')], max_length=300),
        ),
        migrations.AlterField(
            model_name='upload',
            name='numberOfImages',
            field=models.CharField(choices=[('0', '0'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('6', '6'), ('5', '5')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='parking',
            field=models.CharField(blank=True, choices=[('0', '0'), ('4', '4'), ('7', '7'), ('3', '3'), ('2', '2'), ('1', '1'), ('8', '8'), ('9', '9'), ('6', '6'), ('5', '5')], max_length=30),
        ),
        migrations.AlterField(
            model_name='upload',
            name='toilets',
            field=models.CharField(blank=True, choices=[('0', '0'), ('4', '4'), ('7', '7'), ('3', '3'), ('2', '2'), ('1', '1'), ('8', '8'), ('9', '9'), ('6', '6'), ('5', '5')], max_length=30),
        ),
    ]
