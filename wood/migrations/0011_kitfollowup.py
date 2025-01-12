# Generated by Django 4.1.3 on 2023-01-12 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_alter_city_options_alter_location_options_and_more'),
        ('user', '0005_alter_employee_options_alter_provider_options_and_more'),
        ('wood', '0010_remove_kit_transformed_into_kit_id_kit_source_kit_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitFollowup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('used_at_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de utilización total')),
                ('transformed_at_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de transformación')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('destiny_location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='followup_destiny', to='warehouse.location', verbose_name='Ubicación de destino')),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.employee', verbose_name='Empleado')),
                ('external_provider_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.provider', verbose_name='Proveedor externo')),
                ('kit_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.kit', verbose_name='Kit fuente')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='followup_current', to='warehouse.location', verbose_name='Ubicación')),
                ('original_location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='followup_original', to='warehouse.location', verbose_name='Ubicación de origen')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.product', verbose_name='Producto')),
                ('source_kit_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wood.kitfollowup', verbose_name='Kit materia prima')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wood.wood_state', verbose_name='Estado')),
                ('updating_user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.user', verbose_name='Usuario de última actualización')),
            ],
            options={
                'verbose_name': 'Seguimiento Kit',
                'verbose_name_plural': '2.7 Seguimiento a Kits',
            },
        ),
    ]
