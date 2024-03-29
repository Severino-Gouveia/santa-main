"""empty message

Revision ID: ad4456f28950
Revises: 
Create Date: 2024-01-24 06:54:15.847638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad4456f28950'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resposta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('tocar', sa.Integer(), nullable=True),
    sa.Column('cantar', sa.Integer(), nullable=True),
    sa.Column('de_manha', sa.Integer(), nullable=True),
    sa.Column('a_tarde', sa.Integer(), nullable=True),
    sa.Column('receber_email', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resposta')
    # ### end Alembic commands ###
