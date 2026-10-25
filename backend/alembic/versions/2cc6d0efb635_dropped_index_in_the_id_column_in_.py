"""dropped index in the id column in documents

Revision ID: 2cc6d0efb635
Revises: e42a1b5ab5f8
Create Date: 2026-10-25 19:39:40.948168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cc6d0efb635'
down_revision: Union[str, Sequence[str], None] = 'e42a1b5ab5f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
