# Generated by Django 4.0.4 on 2022-09-30 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_rename_item_name_itemtable_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='contact_address',
            new_name='contact_name',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='deliverto',
            field=models.TextField(null=True),
        ),
    ]