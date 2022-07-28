from typing import List

from utils.db_utils.teams import Team
from repositories.base import Session

session = Session()


def get_teams():
    teams: List[Team] = session \
        .query(Team) \
        .all()

    return teams