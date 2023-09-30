"""create TransportUnit table

Revision ID: 99e36ae97edc
Revises: ef94c89f4b97
Create Date: 2023-09-30 18:27:09.171559

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "99e36ae97edc"
down_revision: Union[str, None] = "ef94c89f4b97"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "driver",
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "transportunit",
        sa.Column("driver_id", sa.Integer(), nullable=False),
        sa.Column("auto_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["auto_id"],
            ["auto.id"],
        ),
        sa.ForeignKeyConstraint(
            ["driver_id"],
            ["driver.id"],
        ),
        sa.PrimaryKeyConstraint("driver_id", "auto_id", "id"),
        sa.UniqueConstraint("driver_id", "auto_id", name="unique_transport_unit"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("transportunit")
    op.drop_table("driver")
    # ### end Alembic commands ###