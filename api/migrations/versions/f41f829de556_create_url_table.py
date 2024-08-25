"""Create URL table

Revision ID: f41f829de556
Revises: 43b93daa76e3
Create Date: 2024-08-24 23:14:23.633822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKeyConstraint

# revision identifiers, used by Alembic.
revision: str = 'f41f829de556'
down_revision: Union[str, None] = '43b93daa76e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column("id", sa.String, primary_key=True, index=True),
        sa.Column("url", sa.String, unique=True, index=True, nullable=False),
        sa.Column("short_url", sa.String, unique=True, index=True, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        sa.Column("clicks", sa.Integer, default=0),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_deleted", sa.Boolean, default=False),
        sa.Column("deleted_at", sa.DateTime),
        sa.Column("deleted_by", sa.String),
        sa.Column("updated_by", sa.String, nullable=False),
        sa.Column("created_by", sa.String, nullable=False),
        ForeignKeyConstraint(
            ["created_by"],
            ["users.id"],
        ),
        ForeignKeyConstraint(
            ["updated_by"],
            ["users.id"],
        ),
        ForeignKeyConstraint(
            ["deleted_by"],
            ["users.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("urls")
