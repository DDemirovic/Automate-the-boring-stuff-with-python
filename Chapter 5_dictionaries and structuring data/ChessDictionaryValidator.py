#A Program that checks if a given chess board is valid or not

# King = König, Queen = Dame, Rook = Turm, Bishop = Läufer, Knight = Springer, Pawn = Bauer

#Chess Board, prefix "w" for "white", prefix "b" for "black" (simple team recognition)
chessBoard = {'A1': 'wRook' , 'A2': 'wPawn' , 'A3': '' , 'A4': '' , 'A5': '' , 'A6': '' , 'A7': 'bPawn' , 'A8': 'bRook', 
                'B1': 'wKnight' , 'B2': 'wPawn' , 'B3': '' , 'B4': '' , 'B5': '' , 'B6': '' , 'B7': 'bPawn' , 'B8': 'bKnight', 
                'C1': 'wBishop' , 'C2': 'wPawn' , 'C3': '' , 'C4': '' , 'C5': '' , 'C6': '' , 'C7': 'bPawn' , 'C8': 'bBishop', 
                'D1': 'wKing' , 'D2': 'wPawn' , 'D3': '' , 'D4': '' , 'D5': '' , 'D6': '' , 'D7': 'bPawn' , 'D8': 'bQueen', 
                'E1': 'wQueen' , 'E2': 'wPawn' , 'E3': '' , 'E4': '' , 'E5': '' , 'E6': '' , 'E7': 'bPawn' , 'E8': 'bKing', 
                'F1': 'wBishop' , 'F2': 'wPawn' , 'F3': '' , 'F4': '' , 'F5': '' , 'F6': '' , 'F7': 'bPawn' , 'F8': 'bBishop', 
                'G1': 'wKnight' , 'G2': 'wPawn' , 'G3': '' , 'G4': '' , 'G5': '' , 'G6': '' , 'G7': 'bPawn' , 'G8': 'bKnight', 
                'H1': 'wRook' , 'H2': 'wPawn' , 'H3': '' , 'H4': '' , 'H5': '' , 'H6': '' , 'H7': 'bPawn' , 'H8': 'bRook'}

# chessBoardBackup = {'A1': "wTurm" , 'A2': "wBauer" , 'A3': "" , 'A4': "" , 'A5': "" , 'A6': "" , 'A7': "sBauer" , 'A8': "sTurm", 
#                 'B1': "wSpringer" , 'B2': "wBauer" , 'B3': "" , 'B4': "" , 'B5': "" , 'B6': "" , 'B7': "sBauer" , 'B8': "sSpringer", 
#                 'C1': "wLaeufer" , 'C2': "wBauer" , 'C3': "" , 'C4': "" , 'C5': "" , 'C6': "" , 'C7': "sBauer" , 'C8': "sLaeufer", 
#                 'D1': "wKoenig" , 'D2': "wBauer" , 'D3': "" , 'D4': "" , 'D5': "" , 'D6': "" , 'D7': "sBauer" , 'D8': "sDame", 
#                 '1': "wDame" , '2': "wBauer" , '3': "" , '4': "" , '5': "" , '6': "" , '7': "sBauer" , '8': "sKoenig", 
#                 'F1': "wLaeufer" , 'F2': "wBauer" , 'F3': "" , 'F4': "" , 'F5': "" , 'F6': "" , 'F7': "sBauer" , 'F8': "sLaeufer", 
#                 'G1': "wSpringer" , 'G2': "wBauer" , 'G3': "" , 'G4': "" , 'G5': "" , 'G6': "" , 'G7': "sBauer" , 'G8': "sSpringer", 
#                 'H1': "wTurm" , 'H2': "wBauer" , 'H3': "" , 'H4': "" , 'H5': "" , 'H6': "" , 'H7': "sBauer" , 'H8': "sTurm"}                

#function that prints the board
def boardPrint(board):
    print("8", board['A8'], board['B8'], board['C8'], board['D8'], board['E8'], board['F8'], board['G8'], board['H8'])
    print("7", board['A7'], board['B7'], board['C7'], board['D7'], board['E7'], board['F7'], board['G7'], board['H7'])
    print("6", board['A6'], board['B6'], board['C6'], board['D6'], board['E6'], board['F6'], board['G6'], board['H6'])
    print("5", board['A5'], board['B5'], board['C5'], board['D5'], board['E5'], board['F5'], board['G5'], board['H5'])
    print("4", board['A4'], board['B4'], board['C4'], board['D4'], board['E4'], board['F4'], board['G4'], board['H4'])
    print("3", board['A3'], board['B3'], board['C3'], board['D3'], board['E3'], board['F3'], board['G3'], board['H3'])
    print("2", board['A2'], board['B2'], board['C2'], board['D2'], board['E2'], board['F2'], board['G2'], board['H2'])
    print("1", board['A1'], board['B1'], board['C1'], board['D1'], board['E1'], board['F1'], board['G1'], board['H1'])

def check_board(board):
    piece_count = {
        "wRook": 0,
        "wBishop": 0,
        "wKnight": 0,
        "wKing": 0,
        "wQueen": 0,
        "wPawn": 0,
        "bRook": 0,
        "bBishop": 0,
        "bKnight": 0,
        "bKing": 0,
        "bQueen": 0,
        "bPawn": 0
    }
    
    for piece in board.values():
        if piece != "":
            piece_count[piece] += 1
            
    for piece_type, count in piece_count.items():
        if count > 2:
            if ((piece_type == "wPawn") or (piece_type == "bPawn")) and (count <= 8):
                # color = piece_type[0]
                # piece_name = piece_type[1:].lower()
                # print(color.capitalize(), "team has more than the usual amount of", str(piece_name + "s.A"))
            else:
                color = piece_type[0]
                piece_name = piece_type[1:].lower()
                print(color.capitalize(), "team has more than the usual amount of", str(piece_name + "s.B"))
                #das kleine f um f-Strings zu erstellen. F-Strings ermöglichen es, Variablen und Ausdrücke direkt in den String einzufügen, anstatt sie als separate Argumente an die Print-Funktion zu übergeben.
                #print(f"My name is {name} and I am {age} years old.") 

#functions that checks validity of a board // number of chess pieces (e.g not more than one king per team) & real spots on the board (e.g X3 is not a spot on a usual chess board)
# def validityCheck(board):
#     wRookChecker = 0
#     wBishopChecker = 0
#     wKnightChecker = 0
#     wKingChecker = 0
#     wQueenChecker = 0
#     wPawnChecker = 0

#     bRookChecker = 0
#     bBishopChecker = 0
#     bKnightChecker = 0
#     bKingChecker = 0
#     bQueenChecker = 0
#     bPawnChecker = 0

#     for key, value in board.items():
#         if board[key] != "":
#             if board[key] == "wRook":
#                 wRookChecker += 1
#             if board[key] == "wBishop":
#                 wBishopChecker += 1
#             if board[key] == "wKnight":
#                 wKnightChecker += 1
#             if board[key] == "wKing":
#                 wKingChecker += 1
#             if board[key] == "wQueen":
#                 wQueenChecker += 1
#             if board[key] == "wPawn":
#                 wPawnChecker += 1
#             if board[key] == "bRook":
#                 bRookChecker += 1
#             if board[key] == "bBishop":
#                 bBishopChecker += 1
#             if board[key] == "bKnight":
#                 bKnightChecker += 1
#             if board[key] == "bKing":
#                 bKingChecker += 1
#             if board[key] == "bQueen":
#                 bQueenChecker += 1
#             if board[key] == "bPawn":
#                 bPawnChecker += 1
#     if wRookChecker > 2:
#         print("White team has more than the usual amount of rooks.")
#     if wBishopChecker > 2:
#         print("White team has more than the usual amount of bishops.")
#     if wKnightChecker > 2:
#         print("White team has more than the usual amount of knights.")
#     if wKingChecker > 2:
#         print("White team has more than the usual amount of kings.")
#     if wQueenChecker > 2:
#         print("White team has more than the usual amount of queens.")
#     if wPawnChecker > 8:
#         print("White team has more than the usual amount of pawns.")
#     if bRookChecker > 2:
#         print("Black team has more than the usual amount of rooks.")
#     if bBishopChecker > 2:
#         print("Black team has more than the usual amount of bishops.")
#     if bKnightChecker > 2:
#         print("Black team has more than the usual amount of knights.")
#     if bKingChecker > 2:
#         print("Black team has more than the usual amount of kings.")
#     if bQueenChecker > 2:
#         print("Black team has more than the usual amount of queens.")
#     if bPawnChecker > 8:
#         print("Black team has more than the usual amount of pawns.")

#function that checks if the board is a valid board (if the placement of a chess piece is actually a real spot on the board, e.g A7 = on the board, J9 = not on the board)
def isValid(board, spot):
    if board.get(spot) == None:
        print("Invalid spot")
    else:
        print("Valid spot")

#Function that takes an input in order to place a piece
def whichSpot():
    pieceSpot = input()
    piecePlacer(piece, pieceSpot)     #playerTeam as of right now is a global variable, defined way down in the "initialize area"

#function that places the chosen piece
def piecePlacer(piece, pieceSpot):
    return

# To do: whichSpot als erstes aufrufen, dadrin abfragen ob isValid, 
# falls ja => whichPiece => piecePlacer (dann für das neue piece eine alte löschen, überlegen wie am besten), vlt. mit get() den Spot besetzen
# falls nein => Ausgabe machen das der gewählte Spot invalid ist

check_board(chessBoard)
#print(boardPrint(chessBoard))
#piece = input()
#isValid(chessBoard, 'X3')