"""empty message

Revision ID: 0b73300269fb
Revises: 
Create Date: 2022-03-19 16:25:03.075576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b73300269fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('service', sa.String(length=100), nullable=False),
    sa.Column('money', sa.String(length=100), nullable=False),
    sa.Column('card_number', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('project', sa.String(length=255), nullable=True),
    sa.Column('shop_guide', sa.String(length=255), nullable=True),
    sa.Column('teacher', sa.String(length=255), nullable=True),
    sa.Column('financial', sa.String(length=255), nullable=True),
    sa.Column('remarks1', sa.String(length=255), nullable=True),
    sa.Column('collect_money', sa.String(length=255), nullable=True),
    sa.Column('remarks2', sa.String(length=255), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('modify_time', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('super_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('super_user')
    op.drop_table('card')
    # ### end Alembic commands ###