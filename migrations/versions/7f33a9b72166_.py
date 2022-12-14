"""empty message

Revision ID: 7f33a9b72166
Revises: f803806a434b
Create Date: 2022-08-27 13:43:35.222547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f33a9b72166'
down_revision = 'f803806a434b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Provinsi', 'latitude',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('Provinsi', 'longtitude',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Provinsi', 'longtitude',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('Provinsi', 'latitude',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    # ### end Alembic commands ###
