"""empty message

Revision ID: 3484f145daeb
Revises: 1eeac39f1bc3
Create Date: 2020-01-18 17:09:18.646945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3484f145daeb'
down_revision = '1eeac39f1bc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_rows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_rows2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_rows2')
    op.drop_table('test_rows')
    # ### end Alembic commands ###
