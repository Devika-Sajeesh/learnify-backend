"""add subject fields

Revision ID: db70c7e21516
Revises: 46d3f570d6e5
Create Date: 2025-05-29 10:35:31.489151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db70c7e21516'
down_revision: Union[str, None] = '46d3f570d6e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
