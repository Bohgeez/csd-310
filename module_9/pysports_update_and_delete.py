'''
    Title: pysports_update_and_delete.py
    Author: Robert D Boggs
    Date: 07/09/22
    Description: Program for adding, editing, and removing pysports database records
'''
# import statement
import mysql.connector
from mysql.connector import errorcode

# Creates database config object
config = {
    "user": "root",
    "password": "RylieEatsWorms4414$",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
# Uses inner join on the player and team tables, loop
# through the dataset, and display the results to the terminal window

def show_players(cursor, title):
    cursor.execute('''SELECT player_id, first_name, last_name, team_name
     FROM player INNER JOIN team ON player.team_id = team.team_id''')
    players = cursor.fetchall()
    print("\n -- {} --".format(title))

    for player in players:
        print(''' Player ID: {}\n  First Name: {}\n  Last Name: {}\n  
Team ID: {}\n'''.format(player[0], player[1], player[2], player[3]))

# try/catch block
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
    player_data = ("Scrappers", "The Dog", 1)
    cursor.execute(add_player, player_data)
    db.commit()
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    update_player = ("""UPDATE player SET team_id = 2, first_name = 'Scrappy',
     last_name = 'Doo' WHERE first_name = 'Scrappers'""")
    cursor.execute(update_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    delete_player = ("DELETE FROM player WHERE first_name = 'Scrappy'")
    cursor.execute(delete_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
