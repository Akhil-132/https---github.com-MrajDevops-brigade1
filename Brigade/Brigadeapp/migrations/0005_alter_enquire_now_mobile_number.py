# Generated by Django 4.1.7 on 2023-05-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brigadeapp', '0004_alter_overview_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquire_now',
            name='Mobile_number',
            field=models.IntegerField(),
        ),
    ]
