"""Rename column in Student model

Revision ID: c56d96d3b72d
Revises: 2971672880a6
Create Date: 2023-12-07 14:05:12.000724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c56d96d3b72d'
down_revision = '2971672880a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column( 'name', 'full_name')


def downgrade() -> None:
    op.alter_column( 'full_name', 'name')
