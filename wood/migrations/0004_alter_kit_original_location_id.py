# Generated by Django 4.1.3 on 2022-11-25 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0004_alter_location_warehouse_id_alter_warehouse_map_url"),
        ("wood", "0003_alter_product_city_options_alter_product_height_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kit",
            name="original_location_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="original",
                to="warehouse.location",
            ),
        ),
    ]
