"""add questions table

Revision ID: a260ff90d09f
Revises: db70c7e21516
Create Date: 2025-05-29 19:23:31.245165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a260ff90d09f'
down_revision: Union[str, None] = 'db70c7e21516'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
