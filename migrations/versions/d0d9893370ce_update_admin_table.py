"""update admin table

Revision ID: d0d9893370ce
Revises: 920fd041f98c
Create Date: 2022-11-30 15:45:25.020414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0d9893370ce'
down_revision = '920fd041f98c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('last_login_ip', sa.String(), nullable=True))
    op.add_column('admin', sa.Column('last_login_time', sa.DateTime(), nullable=True))
    op.drop_column('admin', 'last_login')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('last_login', sa.DATETIME(), nullable=True))
    op.drop_column('admin', 'last_login_time')
    op.drop_column('admin', 'last_login_ip')
    # ### end Alembic commands ###