#1  Download and install the latest release:
#   py -m pip install chess         #1.3.0 version at the current time
#   py -m pip install IPython       #?version
#   py -m pip install notebook      #?version
#   py -m notebook                  #launch from webrowser

#Board representation
import chess#https://python-chess.readthedocs.io/en/latest/
import chess.svg
from IPython.display import SVG
#inside browser
board = chess.Board()
#SVG(chess.svg.board(board=board,size=400))

#Board evaluation
def evaluate_board():
    if board.is_checkmate():
        if board.turn:  #if white is mated
            return -9999
        else:           #if black is mated
            return 9999
    if board.is_stalemate():
        return 0#?for a draw
    if board.is_insufficient_material():
        return 0

    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)

    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)]
                                    for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                                    for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq= sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                                    for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                                    for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                                    for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                                    for i in board.pieces(chess.KING, chess.BLACK)])

    eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
    if board.turn:
        return eval
    else:
        return -eval

#Piece-square tables
pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]
knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]
bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]
rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]
queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]
kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]

#Search
def alphabeta( alpha, beta, depthleft ):
    bestscore = -9999
    if( depthleft == 0 ):
        return quiesce( alpha, beta )
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta( -beta, -alpha, depthleft - 1 )
        board.pop()
        if( score >= beta ):
            return score
        if( score > bestscore ):
            bestscore = score
        if( score > alpha ):
            alpha = score
    return bestscore
def quiesce( alpha, beta ):
    stand_pat = evaluate_board()
    if( stand_pat >= beta ):
        return beta
    if( alpha < stand_pat ):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce( -beta, -alpha )
            board.pop()

            if( score >= beta ):
                return beta
            if( score > alpha ):
                alpha = score
    return alpha
import chess.polyglot
def selectmove(depth):
    try:
        move = chess.polyglot.MemoryMappedReader("bookfish.bin").weighted_choice(board).move()
        movehistory.append(move)
        return move
    except:
        count = 0
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in board.legal_moves:
            count += 1
            print("ex",count)
            board.push(move)
            boardValue = -alphabeta(-beta, -alpha, depth-1)
            if boardValue > bestValue:
                bestValue = boardValue;
                bestMove = move
            if( boardValue > alpha ):
                alpha = boardValue
            board.pop()
        return bestMove
#
import sqlite3
conn = sqlite3.connect('chessdb.sqlite')
cur = conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS Parties
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
white TEXT,
white_score INTEGER,
black_score INTEGER,
black TEXT,
moves TEXT,
movcount INTEGER,
data TEXT)
''')

#Match against Stockfish
import chess.pgn
import datetime
board = chess.Board()
#while not board.is_game_over(claim_draw=True):
import random
import re
import chess.engine
x = int(input('Enter the number of chess game you want to store in database:'))
try:
    engine_1 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\Shams\Desktop\ChessProject\stockfish_20090216_32bit.exe")
    engine_2 = chess.engine.SimpleEngine.popen_uci(r"C:\Users\Shams\Desktop\ChessProject\komodo-12.1.1-32bit.exe")
    for num in range(x):
        print("game #",num+1)
        game = chess.pgn.Game()
        #game.headers["Event"] = "ChessAI Battle"
        #game.headers["Site"] = "Ufa, Republic of Bashkortostan Russia"
        #game.headers["Round"] = 1
        game.headers["Date"] = str(datetime.datetime.now().date())
        x = bool(random.getrandbits(1))#50% BLACK 50% WHITE CHANGE ENGINES
        if x:
            game.headers["White"] = "stockfish_20090216_32bit"  #engine_1
            game.headers["Black"] = "komodo-12.1.1-32bit"       #engine_2
        else:
            game.headers["White"] = "komodo-12.1.1-32bit"
            game.headers["Black"] = "stockfish_20090216_32bit"
        print("white:",game.headers["White"]," vs ", "black:", game.headers["Black"])
        movehistory =[]#clear history list()
        board = chess.Board()#start new board
        count = 0
        while not board.is_game_over():
            count = count + 1
            if board.turn:#WHITE
                 #move = selectmove(3)   #python chess with depth 3 moves
                 #board.push_san("e4")   #human moves
                if x:
                    result = engine_1.play(board, chess.engine.Limit(time=0.1))
                else:
                    result = engine_2.play(board, chess.engine.Limit(time=0.1))
                move = result.move
                board.push(move)
                print ("white",count,move)
                movehistory.append(move)
            else:#BLACK
                if x:
                    result = engine_2.play(board, chess.engine.Limit(time=0.1))
                else:
                    result = engine_1.play(board, chess.engine.Limit(time=0.1))
                move = result.move
                board.push(move)
                print ("black",count,move)
                movehistory.append(move)
        game.headers["Result"] = str(board.result(claim_draw=True))
        game.add_line(movehistory)
        print(game)
        c_score = re.split(r'-',game.headers["Result"])
        w_score = c_score[0]#
        b_score = c_score[1]
        cur.execute("INSERT INTO Parties (white,white_score,black_score,black,moves,movcount,data) VALUES (?,?,?,?,?,?,?)",
        (game.headers["White"],w_score,b_score,game.headers["Black"],str(game.mainline()),count,game.headers["Date"]))
        conn.commit()
    engine_1.quit()
    engine_2.quit()
except KeyboardInterrupt:
     print("Keyboard interrupt exception caught, Engines have been closed")
     engine_1.quit()
     engine_2.quit()
     quit()

#SVG(chess.svg.board(board=board,size=400))
#print(game, file=open("test.pgn", "w"), end="\n\n")
#Game Analysis
#1 https://blog.ebemunk.com/a-visual-look-at-2-million-chess-games/
#2 https://andreasstckl.medium.com/chessviz-graphs-of-chess-games-7ebd4f85a9b9

#SOURCES
#1 https://observablehq.com/@kerryrodden/sequences-sunburst

#http-server -p 8000 --cors
#for bypass local web security in web browser and reach to local file
