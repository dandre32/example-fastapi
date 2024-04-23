"""add content column to posts table

Revision ID: 8b28d89daaf7
Revises: 943e87bdd796
Create Date: 2024-04-22 08:10:02.604217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b28d89daaf7'
down_revision: Union[str, None] = '943e87bdd796'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('posts', sa.Column('content', sa.String(), nullable =False))


def downgrade() -> None:
   op.drop_column('posts', 'content')
