# Generated by Django 4.2.1 on 2023-09-18 15:46

import lnschema_core.ids
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lnschema_core", "0019_dataset_reference_dataset_reference_type_and_more"),
        ("lnschema_lamin1", "0009_alter_platewell_id"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PlateWell",
            new_name="Well",
        ),
        migrations.AlterUniqueTogether(
            name="well",
            unique_together={("row", "column")},
        ),
        migrations.AddField(
            model_name="well",
            name="name",
            field=models.CharField(db_index=True, default=None, max_length=32, null=True, unique=True),
        ),
        migrations.RemoveField(
            model_name="well",
            name="plate",
        ),
        migrations.AlterField(
            model_name="well",
            name="id",
            field=models.CharField(
                default=lnschema_core.ids.base62_4,
                max_length=4,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
