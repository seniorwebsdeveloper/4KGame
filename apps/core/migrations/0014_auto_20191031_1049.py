# Generated by Django 2.2.2 on 2019-10-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20191025_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_processing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='platform',
            field=models.CharField(blank=True, choices=[('amaozn', 'Amazon'), ('ebay', 'Ebay'), ('bestbuy', 'BestBuy'), ('wallmart', 'WallMart'), ('newegg', 'NewEgg')], default='amaozn', max_length=32, null=True),
        ),
    ]
