"""empty message

Revision ID: 1b54995bc086
Revises: e99989e6ad56
Create Date: 2021-01-11 10:23:51.674493

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b54995bc086'
down_revision = 'e99989e6ad56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###
