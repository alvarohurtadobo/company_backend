# Generated by Django 4.1.3 on 2022-11-22 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("warehouse", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created datetime"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=80)),
                ("password", models.CharField(max_length=256)),
                ("first_name", models.CharField(max_length=256)),
                ("last_name", models.CharField(max_length=256)),
                ("photo_url", models.CharField(max_length=256, null=True)),
                ("document", models.CharField(max_length=20)),
                ("charge", models.CharField(max_length=20, null=True)),
                ("active", models.BooleanField()),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created datetime"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created datetime"
                    ),
                ),
                (
                    "city_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="warehouse.city",
                    ),
                ),
                (
                    "role_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="user.role"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=256)),
                ("last_name", models.CharField(max_length=256)),
                ("nit", models.CharField(max_length=256)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created datetime"
                    ),
                ),
                (
                    "city_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="warehouse.city",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=256)),
                ("last_name", models.CharField(max_length=256)),
                ("nit", models.CharField(max_length=256)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created datetime"
                    ),
                ),
                (
                    "city_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="warehouse.city",
                    ),
                ),
            ],
        ),
    ]
