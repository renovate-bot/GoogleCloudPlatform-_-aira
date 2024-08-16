"""adding user rating

Revision ID: 6349ef8435cb
Revises: f3943cb79c0c
Create Date: 2024-02-19 00:32:23.805628+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6349ef8435cb'
down_revision = 'f3943cb79c0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE userrating AS ENUM('NO_RATING', 'FLUENT', 'READER', 'PRE_READER_ONE', 'PRE_READER_FOUR')")
    op.add_column('exams_users', sa.Column('user_rating', postgresql.ENUM('NO_RATING', 'FLUENT', 'READER', 'PRE_READER_ONE', 'PRE_READER_FOUR', name='userrating'), nullable=True))
    op.execute("UPDATE exams_users SET user_rating = 'NO_RATING'")
    op.alter_column('exams_users', 'user_rating', nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exams_users', 'user_rating')
    op.execute("DROP TYPE userrating")
    # ### end Alembic commands ###
