"""empty message

Revision ID: ff7a66e66a21
Revises: 
Create Date: 2021-03-07 22:04:33.898192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff7a66e66a21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modelo', sa.String(length=64), nullable=True),
    sa.Column('cor', sa.Integer(), nullable=True),
    sa.Column('ano', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_carro_ano'), 'carro', ['ano'], unique=False)
    op.create_index(op.f('ix_carro_cor'), 'carro', ['cor'], unique=False)
    op.create_index(op.f('ix_carro_modelo'), 'carro', ['modelo'], unique=False)
    op.create_table('comentario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_usuario', sa.String(length=60), nullable=True),
    sa.Column('corpo', sa.String(length=93), nullable=True),
    sa.Column('nota', sa.Integer(), nullable=True),
    sa.Column('carro_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carro_id'], ['carro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comentario')
    op.drop_index(op.f('ix_carro_modelo'), table_name='carro')
    op.drop_index(op.f('ix_carro_cor'), table_name='carro')
    op.drop_index(op.f('ix_carro_ano'), table_name='carro')
    op.drop_table('carro')
    # ### end Alembic commands ###
