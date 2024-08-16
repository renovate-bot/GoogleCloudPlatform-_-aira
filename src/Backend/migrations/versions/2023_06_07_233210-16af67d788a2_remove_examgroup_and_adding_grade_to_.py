"""Remove ExamGroup and adding grade to exam

Revision ID: 16af67d788a2
Revises: 9a650cbb895f
Create Date: 2023-06-07 23:32:10.129697+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '16af67d788a2'
down_revision = '9a650cbb895f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exams_groups')
    op.add_column('exams', sa.Column('grade', postgresql.ENUM('FIRST_FUND', 'SECOND_FUND', 'THIRD_FUND', 'FOURTH_FUND', 'FIFTH_FUND', 'SIXTH_FUND', 'SEVENTH_FUND', 'EIGHTH_FUND', 'NINETH_FUND', 'FIRST_HS', 'SECOND_HS', 'THIRD_HS', name='grades'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exams', 'grade')
    op.create_table('exams_groups',
    sa.Column('exam_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['exams.id'], name='exams_groups_exam_id_fkey'),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name='exams_groups_group_id_fkey'),
    sa.PrimaryKeyConstraint('exam_id', 'group_id', name='exams_groups_pkey')
    )
    # ### end Alembic commands ###
