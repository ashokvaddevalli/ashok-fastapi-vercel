"""userid should be string not int

Revision ID: 4976c6d1e98a
Revises: de319184bb9e
Create Date: 2023-10-11 19:39:33.224576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '4976c6d1e98a'
down_revision: Union[str, None] = 'de319184bb9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'userid',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('users', 'userid',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'userid',
               existing_type=sa.String(length=100),
               type_=mysql.INTEGER(),
               existing_nullable=False)
    op.alter_column('products', 'userid',
               existing_type=sa.String(length=100),
               type_=mysql.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###