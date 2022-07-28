from utils.db_utils.teams import Team
from repositories.base import Session

session = Session()


def save_team(name: str):
    t = Team(name=name)
    session.add(t)
    session.commit()
