# Generated by Django 3.1.5 on 2021-01-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amitnagar', '0008_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
