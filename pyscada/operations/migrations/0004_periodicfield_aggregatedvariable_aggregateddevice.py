# Generated by Django 4.2.5 on 2024-01-16 11:02

from django.db import migrations, models
import django.db.models.deletion
import pyscada.models


class Migration(migrations.Migration):
    dependencies = [
        ("pyscada", "0107_alter_calculatedvariableselector_period_fields"),
        ("operations", "0003_add_aggregated_device_protocol"),
    ]

    operations = [
        migrations.CreateModel(
            name="PeriodicField",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.SmallIntegerField(
                        choices=[
                            (0, "min"),
                            (1, "max"),
                            (2, "total"),
                            (3, "difference"),
                            (4, "difference percent"),
                            (5, "delta"),
                            (6, "mean"),
                            (7, "first"),
                            (8, "last"),
                            (9, "count"),
                            (10, "count value"),
                            (11, "range"),
                            (12, "step"),
                            (13, "change count"),
                            (14, "distinct count"),
                        ],
                        help_text="Min: Minimum value of a field<br>Max: Maximum value of a field<br>Total: Sum of all values in a field<br>Difference: Difference between first and last value of a field<br>Difference percent: Percentage change between first and last value of a field<br>Delta: Cumulative change in value, only counts increments<br>Mean: Mean value of all values in a field<br>First: First value in a field<br>Last: Last value in a field<br>Count: Number of values in a field<br>Count value: Number of a value in a field<br>Range: Difference between maximum and minimum values of a field<br>Step: Minimal interval between values of a field<br>Change count: Number of times the field’s value changes<br>Distinct count: Number of unique values in a field",
                    ),
                ),
                (
                    "property",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Min: superior or equal this value, ex: 53.5 (use >53.5 for strictly superior)<br>Max: lower or equal this value, ex: 53.5 (use <53.5 for strictly lower)<br>Count value : enter the value to count",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "start_from",
                    models.DateTimeField(
                        default=pyscada.models.start_from_default,
                        help_text="Calculate from this DateTime and then each period_factor*period",
                    ),
                ),
                (
                    "period",
                    models.SmallIntegerField(
                        choices=[
                            (0, "second"),
                            (1, "minute"),
                            (2, "hour"),
                            (3, "day"),
                            (4, "week"),
                            (5, "month"),
                            (6, "year"),
                        ]
                    ),
                ),
                (
                    "period_factor",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="Example: set to 2 and choose minute to have a 2 minutes period",
                        validators=[pyscada.models.validate_nonzero],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AggregatedVariable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_check", models.DateTimeField(blank=True, null=True)),
                ("state", models.CharField(default="", max_length=100)),
                (
                    "aggregated_variable",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pyscada.variable",
                    ),
                ),
                (
                    "period",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="operations.periodicfield",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AggregatedDevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aggregated_device",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="pyscada.device"
                    ),
                ),
                (
                    "variable",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pyscada.variable",
                    ),
                ),
            ],
        ),
    ]
