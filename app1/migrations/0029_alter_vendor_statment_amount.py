# Generated by Django 4.0.4 on 2022-10-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_vendor_statment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_statment',
            name='amount',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]