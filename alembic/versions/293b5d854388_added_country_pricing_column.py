"""Added country_pricing column

Revision ID: 293b5d854388
Revises: 
Create Date: 2023-10-11 17:40:54.120745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "293b5d854388"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("products", sa.Column("country_pricing_analysis", sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("products", "country_pricing_analysis")
    # ### end Alembic commands ###