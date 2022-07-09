'''
    Title: pysports_join_queries.py
    Author: Robert D Boggs
    Date: 07/09/22
    Description: Test program for joining the player and team tables
'''

# import statements

from errno import errorcode
import mysql.connector


#database config object
config = {
    "user": "root",
    "password": "RylieEatsWorms4414$",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#try/catch block for errors

try:

    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    # inner join
    cursor.execute('''SELECT player_id, first_name, last_name, team_name FROM player
     INNER JOIN team ON player.team_id = team.team_id''')
    # get results from object
    players = cursor.fetchall()
    print("\n --DISPLAYING PLAYER RECORDS --")
    # iterate over data set and display results
    for player in players:
        print('''  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n
        '''.format(player[0], player[1], player[2], player[3]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
