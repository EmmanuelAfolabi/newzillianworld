# Generated by Django 3.1.3 on 2020-12-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium', '0002_reply_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='reply',
            name='active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]