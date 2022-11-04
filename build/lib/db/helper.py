import MySQLdb

class Connection:
    def __init__(self):
        con = MySQLdb.connect(database='nba', user='root', host='localhost', password='root')
        self.cur = con.cursor()

    def get_players(self,team_id):
        self.cur.execute('select playerId,firstName from players where teamId = %s', [team_id])
        return self.cur.fetchall()

    def get_stats(self,player_id):
        self.cur.execute('select * from players where playerId = %s', [player_id])
        return self.cur.fetchall()

    def get_teams(self):
        self.cur.execute('select teamId,teamName from teams')
        return self.cur.fetchall()
