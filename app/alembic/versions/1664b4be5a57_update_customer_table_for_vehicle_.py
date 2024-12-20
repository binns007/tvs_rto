"""Update Customer table for vehicle_number, number plate front and back

Revision ID: 1664b4be5a57
Revises: 6ba5806ab807
Create Date: 2024-10-13 07:21:41.389254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1664b4be5a57'
down_revision: Union[str, None] = '6ba5806ab807'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # Add new column for combined Aadhaar photos
    op.add_column('customers', sa.Column('number_plate_front', sa.String(), nullable=True))
    op.add_column('customers', sa.Column('number_plate_back', sa.String(), nullable=True))
    op.add_column('customers', sa.Column('vehicle_number', sa.String(), nullable=True))



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column('customers', 'number_plate_front')
    op.drop_column('customers', 'number_plate_back')
    op.drop_column('customers', 'vehicle_number')

    # ### end Alembic commands ##