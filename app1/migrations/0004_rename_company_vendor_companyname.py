# Generated by Django 4.0.4 on 2022-09-15 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='company',
            new_name='companyname',
        ),
    ]
