"""followers

Revision ID: 13f89ebe7a94
Revises: cf96e0f8d4bb
Create Date: 2020-02-22 10:33:06.429904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13f89ebe7a94'
down_revision = 'cf96e0f8d4bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
