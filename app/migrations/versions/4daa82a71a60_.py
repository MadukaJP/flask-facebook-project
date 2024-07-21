"""empty message

Revision ID: 4daa82a71a60
Revises: f2a2f3c27840
Create Date: 2024-07-19 17:34:40.253447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4daa82a71a60'
down_revision = 'f2a2f3c27840'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('state', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('state')

    # ### end Alembic commands ###
