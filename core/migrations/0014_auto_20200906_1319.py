# Generated by Django 2.2.9 on 2020-09-06 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200906_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='shop_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Shop'),
        ),
    ]