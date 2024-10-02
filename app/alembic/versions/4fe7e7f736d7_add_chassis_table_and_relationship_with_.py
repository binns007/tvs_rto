"""Add Chassis table and relationship with User

Revision ID: 4fe7e7f736d7
Revises: c14eb39261aa
Create Date: 2024-10-02 10:45:01.895360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fe7e7f736d7'
down_revision: Union[str, None] = 'c14eb39261aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Create Chassis table
    op.create_table(
        'chassis',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('chassis_number', sa.String(), nullable=False, unique=True),
        sa.Column('chassis_photo_url', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.user_id'), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False)
                )

    # Add chassis_data relationship to User table (this is handled by the ORM model, not in the schema directly)
    # No schema changes needed for this, but just updating the model in the backend would be enough.

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Drop Chassis table
    op.drop_table('chassis')
