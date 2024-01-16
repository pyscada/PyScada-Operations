# Generated by Django 4.2.5 on 2024-01-16 16:19

from django.db import migrations, models
import pyscada.operations.models


class Migration(migrations.Migration):
    dependencies = [
        ("operations", "0006_move_calculated_variable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="operationsdevice",
            name="period_factor",
            field=models.PositiveSmallIntegerField(
                default=1,
                help_text="Example: set to 2 and choose minute to have a 2 minutes period",
                validators=[pyscada.operations.models.validate_nonzero],
            ),
        ),
        migrations.AlterField(
            model_name="operationsdevice",
            name="start_from",
            field=models.DateTimeField(
                default=pyscada.operations.models.start_from_default,
                help_text="Calculate from this DateTime and then each period_factor*period",
            ),
        ),
        migrations.AlterField(
            model_name="periodicfield",
            name="period_factor",
            field=models.PositiveSmallIntegerField(
                default=1,
                help_text="Example: set to 2 and choose minute to have a 2 minutes period",
                validators=[pyscada.operations.models.validate_nonzero],
            ),
        ),
        migrations.AlterField(
            model_name="periodicfield",
            name="start_from",
            field=models.DateTimeField(
                default=pyscada.operations.models.start_from_default,
                help_text="Calculate from this DateTime and then each period_factor*period",
            ),
        ),
    ]
