import sqlite3
import re
conn = sqlite3.connect('chessdb.sqlite')
cur = conn.cursor()
cur.execute("SELECT id, white, white_score, black_score, black, moves, movcount, data from Parties")
rows = cur.fetchall()
count = 0
for row in rows:
    count+=1
    event = "[Event \"AI Battle\"]\n"
    site = "[Site \"Russia-Ufa\"]\n"
    date = "[Date \""+row[7]+"\"]\n"
    id = "[Round \""+str(row[0])+"\"]\n"
    white = "[White \""+row[1]+"\"]\n"
    black = "[Black \""+row[4]+"\"]\n"
    result = "[Result \""+str(row[2])+"-"+str(row[3])+"\"]\n\n"
    '''Make Reparations with # symbol fix that in chess_app.py
    now when it draw there is nothing in Database after last move
    but there is no draw program automatically add '#' - symbol
    movcount = row[6]'''
    if re.search("#",row[5]):
        moves = re.sub(r"#"," "+str(row[2])+"-"+str(row[3]),row[5])
    else:
        moves = row[5]+" "+str(row[2])+"-"+str(row[3])
    x = event+site+date+id+white+black+result+moves
    print(x+"\n")
    print(x, file=open("test.pgn", "a+"), end="\n\n")
print("In total there is",count,"games")
