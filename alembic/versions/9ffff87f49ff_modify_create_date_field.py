"""modify create_date_field

Revision ID: 9ffff87f49ff
Revises: a68f6ff5e0eb
Create Date: 2025-04-21 10:07:55.260516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ffff87f49ff'
down_revision: Union[str, None] = 'a68f6ff5e0eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
