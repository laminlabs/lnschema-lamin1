from enum import Enum

from django.db import models
from django.db.models import PROTECT
from lnschema_bionty.models import CellLine, CellType, Disease, Species, Tissue
from lnschema_core import ids
from lnschema_core.models import ORM, File, User
from lnschema_core.types import ChoicesMixin
from lnschema_core.users import current_user_id


class ExperimentType(ORM):
    """Experiment types."""

    id: str = models.CharField(max_length=4, default=ids.base62_4, primary_key=True)
    name: str = models.CharField(max_length=255, default=None, db_index=True)
    """Name of the experiment type."""
    description = models.TextField(null=True, default=None)
    """Description of the experiment."""
    ontology_id = models.CharField(max_length=32, db_index=True, null=True, default=None)
    """Ontology ID (EFO) of the experiment type."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    """Time of creation of record."""
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    """Time of last update to record."""
    created_by = models.ForeignKey(User, PROTECT, default=current_user_id, related_name="created_experiment_types")
    """Creator of record, a :class:`~lamindb.User`."""


class TreatmentType(ChoicesMixin, Enum):
    genetic = "genetic"
    chemical = "chemical"


class TreatmentSystem(ChoicesMixin, Enum):
    CRISPR_Cas9 = "CRISPR Cas9"
    CRISPRi = "CRISPRi"
    CRISPRa = "CRISPRa"
    shRNA = "shRNA"
    siRNA = "siRNA"
    transgene = "transgene"
    transient_transfection = "transient transfection"


class Experiment(ORM):
    """Experiments."""

    id: str = models.CharField(max_length=8, default=ids.base62_8, primary_key=True)
    name: str = models.CharField(max_length=255, default=None, db_index=True)
    """Name of the experiment."""
    description = models.TextField(null=True, default=None)
    """Description of the experiment."""
    date = models.DateField(default=None, null=True, db_index=True)
    """Date of the experiment."""
    experiment_type = models.ForeignKey(ExperimentType, PROTECT, null=True, related_name="experiments")
    """Type of the experiment."""
    files = models.ManyToManyField(File, related_name="experiments")
    """Date on which the experiment is performed."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    """Time of creation of record."""
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    """Time of last update to record."""
    created_by = models.ForeignKey(User, PROTECT, default=current_user_id, related_name="created_experiments")
    """Creator of record, a :class:`~lamindb.User`."""


class PlateWell(ORM):
    """Wells in a experimental plate."""

    plate = models.IntegerField()
    row = models.CharField(max_length=4, default=None)
    column = models.IntegerField()
    files = models.ManyToManyField(File, related_name="wells")

    class Meta:
        unique_together = (("plate", "row", "column"),)


class TreatmentTarget(ORM):
    """Treatment target."""

    id = models.CharField(max_length=8, default=ids.base62_8, primary_key=True)
    name = models.CharField(max_length=60, default=None, db_index=True)
    """Name of the treatment target."""
    description = models.TextField(null=True, default=None)
    """Description of the treatment target."""
    genes = models.ManyToManyField("lnschema_bionty.Gene", related_name="treatment_targets")
    """Genes of the treatment target, link to :class:`~lnschema_bionty.Gene` records."""
    files = models.ManyToManyField(File, related_name="treatment_targets")
    """Files linked to the treatment target."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    """Time of creation of record."""
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    """Time of last update to record."""
    created_by = models.ForeignKey(
        User,
        PROTECT,
        default=current_user_id,
        related_name="created_treatment_targets",
    )
    """Creator of record, a :class:`~lamindb.User`."""


class Treatment(ORM):
    id = models.CharField(max_length=12, default=ids.base62_12, primary_key=True)
    name = models.CharField(max_length=255, default=None, db_index=True)
    """Name of the treatment."""
    type = models.CharField(max_length=20, choices=TreatmentType.choices(), db_index=True)
    """Type of the treatment.
    "genetic" or "chemical"
    """
    system = models.CharField(max_length=20, choices=TreatmentSystem.choices(), default=None, db_index=True)
    """System used for the genetic treatment."""
    description = models.TextField(null=True, default=None)
    """Description of the treatment."""
    targets = models.ManyToManyField(TreatmentTarget, related_name="treatments")
    """Targets of the treatment."""
    sequence = models.TextField(null=True, default=None, db_index=True)
    """Sequence of the treatment."""
    on_target_score = models.FloatField(default=None, null=True, db_index=True)
    """On-target score of the treatment."""
    off_target_score = models.FloatField(default=None, null=True, db_index=True)
    """Off-target score of the treatment."""
    ontology_id = models.CharField(max_length=32, db_index=True, null=True, default=None)
    """Ontology ID of the treatment."""
    pubchem_id = models.CharField(max_length=32, db_index=True, null=True, default=None)
    """Pubchem ID of the chemical treatment."""
    files = models.ManyToManyField(File, related_name="treatments")
    """Files linked to the treatment."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    """Time of creation of record."""
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    """Time of last update to record."""
    created_by = models.ForeignKey(User, PROTECT, default=current_user_id, related_name="created_treatments")
    """Creator of record, a :class:`~lamindb.User`."""


class Biosample(ORM):
    """Biological samples that are registered in experiments."""

    id = models.CharField(max_length=12, default=ids.base62_12, primary_key=True)
    name = models.CharField(max_length=255, default=None, db_index=True, null=True)
    """Name of the biosample."""
    batch = models.CharField(max_length=60, default=None, null=True, db_index=True)
    """Batch label of the biosample."""
    description = models.TextField(null=True, default=None)
    """Description of the biosample."""
    species = models.ForeignKey(Species, PROTECT, null=True, related_name="biosamples")
    """Species of the biosample."""
    tissues = models.ManyToManyField(Tissue, related_name="biosamples")
    """Tissues linked to the biosample."""
    cell_lines = models.ManyToManyField(CellLine, related_name="biosamples")
    """Cell lines linked to the biosample."""
    cell_types = models.ManyToManyField(CellType, related_name="biosamples")
    """Cell types linked to the biosample."""
    diseases = models.ManyToManyField(Disease, related_name="biosamples")
    """Diseases linked to the biosample."""
    files = models.ManyToManyField(File, related_name="biosamples")
    """Files linked to the biosample."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    """Time of creation of record."""
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    """Time of last update to record."""
    created_by = models.ForeignKey(User, PROTECT, default=current_user_id, related_name="created_biosamples")
    """Creator of record, a :class:`~lamindb.User`."""


class Techsample(ORM):
    id: str = models.CharField(max_length=12, default=ids.base62_12, primary_key=True)
    name = models.CharField(max_length=255, default=None, db_index=True)
    """Name of the techsample."""
    batch = models.CharField(max_length=60, default=None, db_index=True)
    """Batch label of the techsample."""
    description = models.TextField(null=True, default=None)
    """Description of the techsample."""
    biosamples = models.ManyToManyField(Biosample, related_name="techsamples")
    """Linked biosamples."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    """Time of creation of record."""
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    """Time of last update to record."""
    created_by = models.ForeignKey(User, PROTECT, default=current_user_id, related_name="created_techsamples")
    """Creator of record, a :class:`~lamindb.User`."""
