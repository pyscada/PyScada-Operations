# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-24 12:49
from __future__ import unicode_literals
from .. import PROTOCOL_ID, __app_name__

from django.db import migrations
from django.db.utils import ProgrammingError

import logging

logger = logging.getLogger(__name__)


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    try:
        Device = apps.get_model("pyscada", "Device")
        AggregationDeviceOld = apps.get_model("aggregation", "AggregationDeviceOld")
        AggregationDevice = apps.get_model("aggregation", "AggregationDevice")
        DeviceProtocol = apps.get_model("pyscada", "DeviceProtocol")
        Variable = apps.get_model("pyscada", "Variable")
        AggregationVariableOld = apps.get_model("aggregation", "AggregationVariableOld")
        AggregationVariable = apps.get_model("aggregation", "AggregationVariable")
        PeriodField = apps.get_model("aggregation", "PeriodicField")
        db_alias = schema_editor.connection.alias

        agg_protocol = DeviceProtocol.objects.using(db_alias).get(id=PROTOCOL_ID)

        # create devices
        for period in PeriodField.objects.using(db_alias).all():
            avos = AggregationVariableOld.objects.using(db_alias).filter(
                period=period
            )
            if avos.count():
                # create device
                d, _ = Device.objects.using(db_alias).get_or_create(
                    short_name=f"Aggregation_{period.type}_{period.property}_{period.period}_{period.period_factor}",
                    protocol=agg_protocol,
                    description=f"Aggregation variable for {period.__str__()}",
                    polling_interval=60,  # 1 minute, TODO add synchronisation for device polling interval
                )
                ad, _ = AggregationDevice.objects.using(db_alias).get_or_create(
                    aggregation_device=d, type=period.type, property=period.property,
                    start_from=period.start_from, period=period.period, period_factor=period.period_factor
                )

                # create variables
                for avo in avos:
                    try:
                        v2=avo.aggregation_variable.device.aggregationdeviceold.variable
                    except:
                        continue
                    v = avo.aggregation_variable
                    v.name += "-new"
                    v.id = None
                    v.device = d
                    v.save()
                    av, _ = AggregationVariable.objects.using(db_alias).get_or_create(
                        aggregation_variable=v, variable=v2
                    )
                    logger.info(
                        f"Created AggregationVariable {av.aggregation_variable.name}"
                    )
    except (ProgrammingError, LookupError):
        pass


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("aggregation", "0005_aggregationvariable_aggregationdevice"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
