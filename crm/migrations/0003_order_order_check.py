# Generated by Django 3.2.4 on 2021-06-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210617_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_check',
            field=models.BooleanField(default=False),
        ),
    ]
