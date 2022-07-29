from typing import List

from utils.db_utils.teams import FirstTeam, SecondTeam
from repositories.base import Session

session = Session()


def get_first_team():
    teams: List[FirstTeam] = session \
        .query(FirstTeam) \
        .all()

    return teams


def get_second_team():
    teams: List[SecondTeam] = session \
        .query(SecondTeam) \
        .all()

    return teams
