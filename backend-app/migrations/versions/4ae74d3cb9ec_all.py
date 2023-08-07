"""all

Revision ID: 4ae74d3cb9ec
Revises: a098525e051d
Create Date: 2023-08-06 13:22:09.650987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae74d3cb9ec'
down_revision = 'a098525e051d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relacaoCadeiraUnidade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('unidade_id', sa.Integer(), nullable=False),
    sa.Column('cadeiras_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cadeiras_id'], ['cadeiras.id'], ),
    sa.ForeignKeyConstraint(['unidade_id'], ['unidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('cadeiras', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
        batch_op.drop_column('unidade_id')

    with op.batch_alter_table('unidade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
        batch_op.drop_column('id_cadeiras')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unidade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_cadeiras', sa.INTEGER(), nullable=False))
        batch_op.drop_column('id')

    with op.batch_alter_table('cadeiras', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unidade_id', sa.INTEGER(), nullable=False))
        batch_op.drop_column('id')

    op.drop_table('relacaoCadeiraUnidade')
    # ### end Alembic commands ###
