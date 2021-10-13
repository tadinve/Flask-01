"""create accounts table

Revision ID: 9c8ffbdabebb
Revises: 
Create Date: 2021-08-30 06:34:54.296806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c8ffbdabebb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    account = op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('deleted_at', sa.DateTime)
    )


def downgrade():
    op.drop_table('account')
