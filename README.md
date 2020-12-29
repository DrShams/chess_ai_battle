# Chess AI battle: komodo vs stockfish
Simple alghorythm to use:

I. Copy that repository on your pc:
  1) (terminal) git clone https://github.com/DrShams/chess_ai_battle
  2) (terminal) cd chess_ai_battle
II. Use python scripts to create database of chess games between two AI chess engines, 
test.pgn file wil be final output file which will be used further.
  1) At first download chess engines from official website:
  https://stockfishchess.org/download/
  https://komodochess.com/
  In my case I've used 32bit version of these engines
  2) (terminal) py chess_to_db.py
  - in my case, here I used stockfish_20090216_32bit.exe and komodo-12.1.1-32bit.exe
  - Enter the number of chess game you want to store in database:
  - for instance: 100
  - in the file chessdb.sqlite will be added 100 games with SAN notation of the games
  - check https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
  - in any time you can interrupt that script with Ctrl+C
  3) (terminal) py chess_db_to_pgn.py
  - that script converts games from database chessdb.sqlite to test.pgn file
  - move test.pgn file to the pgnstats folder
  - (terminal) cd pgnstats
III. Install https://golang.org/ and use goLang script to convert test.pgn to "youname".json file,
Usage example:
  - (terminal) go run . -f test.pgn -o test.json
  or
  - (terminal) go run pgnstats.go Gamestats.go Heatmap.go file.go movetrack.go openingmove.go getstats.go stats.go -f test.pgn -o test.json
  (both variants are correct)
  ! Kludge: open test.json in your text editor and change "Openings" to "openings"
  - move that .json file in the previous (chess_ai_battle) folder
  - (terminal) cd chess_ai_battle
IV. Launch http-server being inside chess_ai_battle folder
  1) install https://nodejs.org/en/
  2) (terminal) npm install http-server -g
  3) (terminal) http-server -p 8000 --cors
  (that launches http-server with open port 8000 with cross-origin resource sharing, it
  needs for bypass d3.json browser security function which are the part of chess_2.html file)
V. Open chess_2.html file in your browser
(here will be sunburst visualisation of all the games from PGN.file, you can use any PGN.file for that purpose)

Contributions:
- https://github.com/ebemunk/chess-dataviz
- https://github.com/ebemunk/pgnstats
- also huge thanks Fr3nch for making corrections and advices
