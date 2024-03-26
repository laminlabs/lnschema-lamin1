# Generated by Django 4.2.2 on 2023-06-12 19:01

import django.db.models.deletion
import lnschema_core.ids
import lnschema_core.users
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("lnschema_core", "0001_initial"),
        ("lnschema_bionty", "0001_initial"),
    ]

    operations = [
        # only necessary for legacy instances
        # migrations.RunSQL("alter table wetlab_biosample rename to wetlab_legacy_biosample"),
        # migrations.RunSQL("alter table wetlab_techsample rename to wetlab_legacy_techsample"),
        # migrations.RunSQL("alter table wetlab_treatment rename to wetlab_legacy_treatment"),
        # migrations.RunSQL("alter table wetlab_experimenttype rename to wetlab_legacy_experimenttype"),
        # migrations.RunSQL("alter table wetlab_experiment rename to wetlab_legacy_experiment"),
        # migrations.RunSQL("alter table wetlab_well rename to wetlab_legacy_well"),
        migrations.CreateModel(
            name="Biosample",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lnschema_core.ids.base62_12,
                        max_length=12,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(db_index=True, default=None, max_length=255, null=True),
                ),
                (
                    "batch_name",
                    models.CharField(db_index=True, default=None, max_length=60, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "cell_line",
                    models.ManyToManyField(related_name="biosamples", to="lnschema_bionty.cellline"),
                ),
                (
                    "cell_type",
                    models.ManyToManyField(related_name="biosamples", to="lnschema_bionty.celltype"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_storages",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "disease",
                    models.ManyToManyField(related_name="biosamples", to="lnschema_bionty.disease"),
                ),
                (
                    "files",
                    models.ManyToManyField(related_name="biosamples", to="lnschema_core.artifact"),
                ),
                (
                    "species",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="biosamples",
                        to="lnschema_bionty.organism",
                    ),
                ),
                (
                    "tissue",
                    models.ManyToManyField(related_name="biosamples", to="lnschema_bionty.tissue"),
                ),
            ],
            options={},
        ),
        migrations.CreateModel(
            name="Treatment",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lnschema_core.ids.base62_12,
                        max_length=12,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                (
                    "description",
                    models.CharField(db_index=True, default=None, max_length=255),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("genetic", "genetic"), ("chemical", "chemical")],
                        db_index=True,
                        max_length=20,
                    ),
                ),
                (
                    "system",
                    models.CharField(
                        choices=[
                            ("CRISPR Cas9", "CRISPR_Cas9"),
                            ("CRISPRi", "CRISPRi"),
                            ("CRISPRa", "CRISPRa"),
                            ("shRNA", "shRNA"),
                            ("siRNA", "siRNA"),
                            ("transgene", "transgene"),
                            ("transient transfection", "transient_transfection"),
                        ],
                        db_index=True,
                        default=None,
                        max_length=20,
                    ),
                ),
                (
                    "target",
                    models.CharField(db_index=True, default=None, max_length=60),
                ),
                ("sequence", models.TextField(db_index=True, default=None)),
                (
                    "on_target_score",
                    models.FloatField(db_index=True, default=None, null=True),
                ),
                (
                    "off_target_score",
                    models.FloatField(db_index=True, default=None, null=True),
                ),
                (
                    "ontology_id",
                    models.CharField(db_index=True, default=None, max_length=20),
                ),
                (
                    "pubchem_id",
                    models.CharField(db_index=True, default=None, max_length=20),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_storages",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "files",
                    models.ManyToManyField(related_name="treatments", to="lnschema_core.artifact"),
                ),
            ],
            options={},
        ),
        migrations.CreateModel(
            name="Techsample",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lnschema_core.ids.base62_12,
                        max_length=12,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("batch", models.CharField(db_index=True, default=None, max_length=60)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "biosamples",
                    models.ManyToManyField(related_name="techsamples", to="wetlab.biosample"),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_storages",
                        to="lnschema_core.user",
                    ),
                ),
            ],
            options={},
        ),
        migrations.CreateModel(
            name="ExperimentType",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lnschema_core.ids.base62_4,
                        max_length=4,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("efo_id", models.CharField(default=None, max_length=30)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_experiment_types",
                        to="lnschema_core.user",
                    ),
                ),
            ],
            options={},
        ),
        migrations.CreateModel(
            name="Experiment",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=lnschema_core.ids.base62_8,
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("date", models.DateTimeField(db_index=True, default=None, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_experiments",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "experiment_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="experiments",
                        to="wetlab.experimenttype",
                    ),
                ),
                (
                    "files",
                    models.ManyToManyField(related_name="experiments", to="lnschema_core.artifact"),
                ),
            ],
            options={},
        ),
        migrations.CreateModel(
            name="Well",
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
                ("row", models.CharField(default=None, max_length=4)),
                ("column", models.IntegerField()),
                (
                    "files",
                    models.ManyToManyField(related_name="wells", to="lnschema_core.artifact"),
                ),
            ],
            options={
                "unique_together": {("row", "column")},
            },
        ),
        migrations.AlterModelOptions(name="biosample", options={"managed": True}),
        migrations.AlterModelOptions(name="experiment", options={"managed": True}),
        migrations.AlterModelOptions(name="experimenttype", options={"managed": True}),
        migrations.AlterModelOptions(name="techsample", options={"managed": True}),
        migrations.AlterModelOptions(name="treatment", options={"managed": True}),
        migrations.AlterModelOptions(name="well", options={"managed": True}),
    ]