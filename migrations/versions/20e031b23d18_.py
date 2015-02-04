"""empty message

Revision ID: 20e031b23d18
Revises: 28af272381c0
Create Date: 2015-02-04 16:19:45.930039

"""

# revision identifiers, used by Alembic.
revision = '20e031b23d18'
down_revision = '28af272381c0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('stream_id', sa.Integer(), nullable=True),
    sa.Column('subscriber_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['stream_id'], ['stream.id'], ),
    sa.ForeignKeyConstraint(['subscriber_id'], ['subscriber.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscription')
    ### end Alembic commands ###