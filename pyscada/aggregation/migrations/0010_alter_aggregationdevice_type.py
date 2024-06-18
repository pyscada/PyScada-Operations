# Generated by Django 5.0.3 on 2024-06-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aggregation", "0009_alter_aggregationdevice_calculation_end_offset_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aggregationdevice",
            name="type",
            field=models.SmallIntegerField(
                blank=True,
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
                    (15, "index increment"),
                ],
                help_text="Min: Minimum value of a field<br>Max: Maximum value of a field<br>Total: Sum of all values in a field<br>Difference: Difference between first and last value of a field<br>Difference percent: Percentage change between first and last value of a field<br>Delta: Cumulative change in value, only counts increments<br>Mean: Mean value of all values in a field<br>First: First value in a field<br>Last: Last value in a field<br>Count: Number of values in a field<br>Count value: Number of a value in a field<br>Range: Difference between maximum and minimum values of a field<br>Step: Minimal interval between values of a field<br>Change count: Number of times the field’s value changes<br>Distinct count: Number of unique values in a field<br>Index increment: Incrementation of an index with previous known value",
                null=True,
            ),
        ),
    ]
