"""empty message

Revision ID: 626362df9d58
Revises: bf516100b3ad
Create Date: 2022-09-12 15:21:22.200880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '626362df9d58'
down_revision = 'bf516100b3ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('created', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'created')
    # ### end Alembic commands ###