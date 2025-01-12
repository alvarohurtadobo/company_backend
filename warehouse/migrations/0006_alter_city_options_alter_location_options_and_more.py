# Generated by Django 4.1.3 on 2022-11-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0005_alter_city_options_alter_location_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name": "Ciudad", "verbose_name_plural": "3.1 Ciudades"},
        ),
        migrations.AlterModelOptions(
            name="location",
            options={
                "verbose_name": "Ubicación",
                "verbose_name_plural": "3.3 Ubicaciones",
            },
        ),
        migrations.AlterModelOptions(
            name="warehouse",
            options={"verbose_name": "Bodega", "verbose_name_plural": "3.2 Bodegas"},
        ),
        migrations.AlterField(
            model_name="warehouse",
            name="map_url",
            field=models.ImageField(
                default="media/maps/default.png",
                upload_to="maps/",
                verbose_name="Mapa guía",
            ),
        ),
    ]
