"""init

Revision ID: 41cea22067fb
Revises:
Create Date: 2020-12-04 08:42:31.602349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41cea22067fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('company',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('paintwork',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sculptor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('series',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('size', sa.SmallInteger(), nullable=True),
    sa.Column('scale', sa.SmallInteger(), nullable=True),
    sa.Column('resale', sa.Boolean(), nullable=True),
    sa.Column('adult', sa.Boolean(), nullable=True),
    sa.Column('copyright', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('jan', sa.BigInteger(), nullable=True),
    sa.Column('id_by_official', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('series_id', sa.Integer(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('releaser_id', sa.Integer(), nullable=True),
    sa.Column('distributer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['distributer_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['releaser_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['series_id'], ['series.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jan')
    )
    op.create_table('product_official_image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_paintwork',
    sa.Column('prodcut_id', sa.Integer(), nullable=True),
    sa.Column('paintwork_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['paintwork_id'], ['paintwork.id'], ),
    sa.ForeignKeyConstraint(['prodcut_id'], ['product.id'], )
    )
    op.create_table('product_release_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('order_period_start', sa.DateTime(), nullable=True),
    sa.Column('order_period_end', sa.DateTime(), nullable=True),
    sa.Column('initial_release_date', sa.Date(), nullable=False),
    sa.Column('delay_release_date', sa.Date(), nullable=True),
    sa.Column('announced_at', sa.Date(), nullable=True),
    sa.Column('release_at', sa.Date(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_sculptor',
    sa.Column('prodcut_id', sa.Integer(), nullable=True),
    sa.Column('sculptor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prodcut_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['sculptor_id'], ['sculptor.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_sculptor')
    op.drop_table('product_release_info')
    op.drop_table('product_paintwork')
    op.drop_table('product_official_image')
    op.drop_table('product')
    op.drop_table('series')
    op.drop_table('sculptor')
    op.drop_table('paintwork')
    op.drop_table('company')
    op.drop_table('category')
    # ### end Alembic commands ###