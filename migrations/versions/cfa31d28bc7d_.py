"""empty message

Revision ID: cfa31d28bc7d
Revises: 4bae44a74516
Create Date: 2021-04-25 15:22:55.663167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfa31d28bc7d'
down_revision = '4bae44a74516'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(length=10), nullable=True),
    sa.Column('account_type', sa.Enum('Ahorro', 'Corriente'), nullable=True),
    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id', 'client_id'),
    sa.UniqueConstraint('identifier')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###