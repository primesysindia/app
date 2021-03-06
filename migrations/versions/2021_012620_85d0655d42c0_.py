"""empty message

Revision ID: 85d0655d42c0
Revises: 74906d31d994
Create Date: 2021-01-26 20:09:13.949591

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85d0655d42c0'
down_revision = '74906d31d994'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sender_format_updated_at', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sender_format_updated_at')
    # ### end Alembic commands ###
