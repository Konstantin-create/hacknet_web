"""posts table

Revision ID: d8be486fb12a
Revises: 
Create Date: 2022-10-20 18:33:11.769892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8be486fb12a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('header', sa.String(), nullable=False),
    sa.Column('text', sa.String(length=120), nullable=False),
    sa.Column('tags', sa.String(length=12000), nullable=False),
    sa.Column('img', sa.String(), nullable=False),
    sa.Column('time_stamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_time_stamp'), 'posts', ['time_stamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_time_stamp'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
