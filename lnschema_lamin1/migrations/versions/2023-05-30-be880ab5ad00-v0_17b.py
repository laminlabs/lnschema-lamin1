"""v0.17b."""
import sqlalchemy as sa  # noqa
import sqlmodel as sqm  # noqa
from alembic import op

revision = "be880ab5ad00"
down_revision = "c3f38ffe9e05"


def upgrade() -> None:
    delim = "." if op.get_bind().engine.name == "sqlite" else "_"
    op.drop_index(f"ix_lamin1{delim}biosample_cell_type_id", table_name="lnschema_lamin1_biosample")
    op.drop_index(f"ix_lamin1{delim}biosample_created_at", table_name="lnschema_lamin1_biosample")
    op.drop_index(f"ix_lamin1{delim}biosample_created_by", table_name="lnschema_lamin1_biosample")
    op.drop_index(f"ix_lamin1{delim}biosample_disease_id", table_name="lnschema_lamin1_biosample")
    op.drop_index(f"ix_lamin1{delim}biosample_name", table_name="lnschema_lamin1_biosample")
    op.drop_index(f"ix_lamin1{delim}biosample_species_id", table_name="lnschema_lamin1_biosample")
    op.drop_index(f"ix_lamin1{delim}biosample_tissue_id", table_name="lnschema_lamin1_biosample")
    op.drop_index(f"ix_lamin1{delim}biosample_updated_at", table_name="lnschema_lamin1_biosample")
    op.create_index(op.f("ix_lnschema_lamin1_biosample_cell_type_id"), "lnschema_lamin1_biosample", ["cell_type_id"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_biosample_created_at"), "lnschema_lamin1_biosample", ["created_at"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_biosample_created_by"), "lnschema_lamin1_biosample", ["created_by"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_biosample_disease_id"), "lnschema_lamin1_biosample", ["disease_id"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_biosample_name"), "lnschema_lamin1_biosample", ["name"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_biosample_species_id"), "lnschema_lamin1_biosample", ["species_id"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_biosample_tissue_id"), "lnschema_lamin1_biosample", ["tissue_id"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_biosample_updated_at"), "lnschema_lamin1_biosample", ["updated_at"], unique=False)
    op.drop_index(f"ix_lamin1{delim}experiment_created_at", table_name="lnschema_lamin1_experiment")
    op.drop_index(f"ix_lamin1{delim}experiment_created_by", table_name="lnschema_lamin1_experiment")
    op.drop_index(f"ix_lamin1{delim}experiment_date", table_name="lnschema_lamin1_experiment")
    op.drop_index(f"ix_lamin1{delim}experiment_experiment_type_id", table_name="lnschema_lamin1_experiment")
    op.drop_index(f"ix_lamin1{delim}experiment_name", table_name="lnschema_lamin1_experiment")
    op.drop_index(f"ix_lamin1{delim}experiment_updated_at", table_name="lnschema_lamin1_experiment")
    op.create_index(op.f("ix_lnschema_lamin1_experiment_created_at"), "lnschema_lamin1_experiment", ["created_at"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experiment_created_by"), "lnschema_lamin1_experiment", ["created_by"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experiment_date"), "lnschema_lamin1_experiment", ["date"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experiment_experiment_type_id"), "lnschema_lamin1_experiment", ["experiment_type_id"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experiment_name"), "lnschema_lamin1_experiment", ["name"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experiment_updated_at"), "lnschema_lamin1_experiment", ["updated_at"], unique=False)
    op.drop_index(f"ix_lamin1{delim}experiment_type_created_at", table_name="lnschema_lamin1_experimenttype")
    op.drop_index(f"ix_lamin1{delim}experiment_type_created_by", table_name="lnschema_lamin1_experimenttype")
    op.drop_index(f"ix_lamin1{delim}experiment_type_name", table_name="lnschema_lamin1_experimenttype")
    op.drop_index(f"ix_lamin1{delim}experiment_type_updated_at", table_name="lnschema_lamin1_experimenttype")
    op.drop_constraint("uq_experiment_type_efo_id", "lnschema_lamin1_experimenttype", type_="unique")
    op.create_index(op.f("ix_lnschema_lamin1_experimenttype_created_at"), "lnschema_lamin1_experimenttype", ["created_at"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experimenttype_created_by"), "lnschema_lamin1_experimenttype", ["created_by"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experimenttype_name"), "lnschema_lamin1_experimenttype", ["name"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_experimenttype_updated_at"), "lnschema_lamin1_experimenttype", ["updated_at"], unique=False)
    op.create_unique_constraint(op.f("uq_lnschema_lamin1_experimenttype_efo_id"), "lnschema_lamin1_experimenttype", ["efo_id"])
    op.drop_index(f"ix_lamin1{delim}techsample_created_at", table_name="lnschema_lamin1_techsample")
    op.drop_index(f"ix_lamin1{delim}techsample_created_by", table_name="lnschema_lamin1_techsample")
    op.drop_index(f"ix_lamin1{delim}techsample_name", table_name="lnschema_lamin1_techsample")
    op.drop_index(f"ix_lamin1{delim}techsample_updated_at", table_name="lnschema_lamin1_techsample")
    op.create_index(op.f("ix_lnschema_lamin1_techsample_created_at"), "lnschema_lamin1_techsample", ["created_at"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_techsample_created_by"), "lnschema_lamin1_techsample", ["created_by"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_techsample_name"), "lnschema_lamin1_techsample", ["name"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_techsample_updated_at"), "lnschema_lamin1_techsample", ["updated_at"], unique=False)
    op.drop_index(f"ix_lamin1{delim}treatment_created_at", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_created_by", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_description", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_name", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_off_target_score", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_on_target_score", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_ontology_id", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_pubchem_id", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_sequence", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_system", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_target", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_type", table_name="lnschema_lamin1_treatment")
    op.drop_index(f"ix_lamin1{delim}treatment_updated_at", table_name="lnschema_lamin1_treatment")
    op.create_index(op.f("ix_lnschema_lamin1_treatment_created_at"), "lnschema_lamin1_treatment", ["created_at"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_created_by"), "lnschema_lamin1_treatment", ["created_by"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_description"), "lnschema_lamin1_treatment", ["description"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_name"), "lnschema_lamin1_treatment", ["name"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_off_target_score"), "lnschema_lamin1_treatment", ["off_target_score"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_on_target_score"), "lnschema_lamin1_treatment", ["on_target_score"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_ontology_id"), "lnschema_lamin1_treatment", ["ontology_id"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_pubchem_id"), "lnschema_lamin1_treatment", ["pubchem_id"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_sequence"), "lnschema_lamin1_treatment", ["sequence"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_system"), "lnschema_lamin1_treatment", ["system"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_target"), "lnschema_lamin1_treatment", ["target"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_type"), "lnschema_lamin1_treatment", ["type"], unique=False)
    op.create_index(op.f("ix_lnschema_lamin1_treatment_updated_at"), "lnschema_lamin1_treatment", ["updated_at"], unique=False)


def downgrade() -> None:
    pass
