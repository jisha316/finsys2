# Generated by Django 4.0.4 on 2022-10-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_alter_vendor_statment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasepayment',
            name='amtcredit',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='purchasepayment',
            name='amtreceived',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
