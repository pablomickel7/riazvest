# Generated by Django 5.1.1 on 2025-01-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0004_rename_amount_invested_userinvestment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvestment',
            name='ref_code',
            field=models.CharField(default='1234567890', max_length=15, unique=True),
        ),
    ]
