"""add last columns

Revision ID: fa34513d676b
Revises: d0695a8b88b7
Create Date: 2024-04-22 16:07:27.269741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa34513d676b'
down_revision: Union[str, None] = 'd0695a8b88b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

