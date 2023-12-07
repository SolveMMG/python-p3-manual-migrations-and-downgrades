"""Renaming students to scholars

Revision ID: 2971672880a6
Revises: 791279dd0760
Create Date: 2023-12-07 13:54:13.208510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2971672880a6'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
