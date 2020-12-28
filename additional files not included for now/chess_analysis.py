import chess.pgn
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
pgnfile="test.pgn" # cat alphazero_vs_stockfish_all.pgn alphazero_vs_stockfish_tcec_positions_all.pgn > alphazero-all.pgn

## basically analysis of PGN
def nb_moves(g):
    nbmove = 0
    for move in g.mainline_moves():
        if (move is not None):
            nbmove = nbmove + 1
    return nbmove / 2

pgn = open(pgnfile)
df = pd.DataFrame(columns=['nbmoves', "AZresult", "AZwhite"])
idg = 0
while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    whiteplayer = game.headers.get("White") == 'AlphaZero'
    result = "WIN" if (whiteplayer and game.headers.get('Result') == '1-0') else ("LOSE" if (whiteplayer and game.headers.get('Result') == '0-1') else "DRAW")
    df.loc[idg] = (int(nb_moves(game)), result, whiteplayer)
    idg = idg + 1

df['AZresult'].value_counts()
plt.figure()
plt.boxplot(pd.to_numeric(df['nbmoves']))
plt.title("number of moves")
# df.boxplot(column=['nbmoves'])
plt.show()

#df.boxplot(pd.to_numeric(df['nbmoves']))
#df[df['AZresult'] == 'WIN']
#df
df.sort_values(by="nbmoves")[:20]
