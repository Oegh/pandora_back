# Generated by Django 3.2.7 on 2021-10-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandora_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
