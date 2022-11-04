import pandas as pd
from sqlalchemy import create_engine
from urls import urls


class Populate:
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="root", pw="root", db="nba"))

    def populate(self):
        # gets teams and writes to sql
        teams = get_dataframe_from_response_teams(urls[1])
        # I only want to store certain columns
        teams.to_sql('teams', con=self.engine, if_exists='replace', chunksize=1000)

        # gets players and writes to sql, replacing if table exists
        players = get_dataframe_from_response_players(urls[0])
        players.to_sql('players', con=self.engine, if_exists='replace', chunksize=1000)


def get_dataframe_from_response_teams(url):
    data = pd.read_json(url)

    frame = pd.DataFrame(data[['teamId', 'teamName']])

    print(frame)

    return frame


def get_dataframe_from_response_players(url):
    data = pd.read_json(url)

    frame = pd.DataFrame(data[['firstName', 'lastName', 'playerId', 'teamId']])

    print(frame)

    return frame


populate = Populate()

populate.populate()
