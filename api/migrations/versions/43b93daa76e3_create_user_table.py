"""Create User table

Revision ID: 43b93daa76e3
Revises: 
Create Date: 2024-08-24 20:38:16.028103

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43b93daa76e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True, nullable=False),
        sa.Column("email", sa.String, unique=True, index=True, nullable=False),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("last_password", sa.String),
        sa.Column("last_password_at", sa.DateTime),
        sa.Column("last_login_at", sa.DateTime),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
