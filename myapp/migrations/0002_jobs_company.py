# Generated by Django 5.0 on 2023-12-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='company',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
