"""empty message

Revision ID: 5823e4224d02
Revises: 1e60df51a36d
Create Date: 2022-08-27 14:39:20.340900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5823e4224d02'
down_revision = '1e60df51a36d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Sayuran',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('catatan', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Sayuran')
    # ### end Alembic commands ###
