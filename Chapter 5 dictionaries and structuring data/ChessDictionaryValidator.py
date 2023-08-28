#A Program that checks if a given chess board is valid or not

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

#function that checks if the amount of pieces does not exceed the maximum allowed amount of pieces per team
def checkPieces(board):
    #dictionary that contains every possible piece
    pieceCount = {
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

    piecesValidity = True
    #pieceCount dictionary values are counted
    for piece in board.values():
        if piece != "":
            pieceCount[piece] += 1
    
    #check if one or more pieces exceed the max. amount per team        
    for pieceType, count in pieceCount.items():
        if count < 2:   #Max number of king/queen per team = 1, so if the number is lower than 2 (=1), nothing happens, usual amount of number for king/queen
            continue
        elif (("wQueen" == pieceType) or ("wKing"== pieceType) or ("bQueen"== pieceType) or ("bKing" == pieceType)) and (count >= 2): #case for more than max w/b queens/kings
            color = pieceType[0] #team color can be extracted from the first letter of the piece, that's why piece_type[0] = first letter of that string
            pieceName = pieceType[1:].lower() #the origin string gets separated into two pieces, color and piece_name (this and the line above)
            print(color.capitalize(), "team has more than the usual amount of", str(pieceName + "s:"), pieceCount[pieceType])
            piecesValidity = False
            continue
        elif count > 2: #Max number of rook/bishop/knight per team = 2, max number of pawn per team = 8, we get here if the number of rook/bishop/knight exceeds 2 and/or if there are the starting amount or more of pawns
            if (("wPawn" == pieceType) or ("bPawn" == pieceType)) and (count <= 8): #check for white or black pawns, if the number is equal or less than 8 = ok
                continue
            elif (("wPawn" == pieceType) or ("bPawn" == pieceType)) and (count > 8): #number of pawns per team is greater than 8 = not ok
                color = pieceType[0] 
                pieceName = pieceType[1:].lower() 
                print(color.capitalize(), "team has more than the usual amount of", str(pieceName + "s:"), pieceCount[pieceType])
                piecesValidity = False
                continue
            else:
                color = pieceType[0] 
                pieceName = pieceType[1:].lower() 
                print(color.capitalize(), "team has more than the usual amount of", str(pieceName + "s:"), pieceCount[pieceType])
                piecesValidity = False
                continue
            #das kleine f um f-Strings zu erstellen. F-Strings ermöglichen es, Variablen und Ausdrücke direkt in den String einzufügen, anstatt sie als separate Argumente an die Print-Funktion zu übergeben.
            #print(f"My name is {name} and I am {age} years old.")
            
    return piecesValidity 

#function that checks if the spots on the board are valid
def checkSpots(board):
    #dictionary that contains every valid chess board position
    validChessBoardPositions = {
    'A1': '' , 'A2': '' , 'A3': '' , 'A4': '' , 'A5': '' , 'A6': '' , 'A7': '' , 'A8': '', 
    'B1': '' , 'B2': '' , 'B3': '' , 'B4': '' , 'B5': '' , 'B6': '' , 'B7': '' , 'B8': '', 
    'C1': '' , 'C2': '' , 'C3': '' , 'C4': '' , 'C5': '' , 'C6': '' , 'C7': '' , 'C8': '', 
    'D1': '' , 'D2': '' , 'D3': '' , 'D4': '' , 'D5': '' , 'D6': '' , 'D7': '' , 'D8': '', 
    'E1': '' , 'E2': '' , 'E3': '' , 'E4': '' , 'E5': '' , 'E6': '' , 'E7': '' , 'E8': '', 
    'F1': '' , 'F2': '' , 'F3': '' , 'F4': '' , 'F5': '' , 'F6': '' , 'F7': '' , 'F8': '', 
    'G1': '' , 'G2': '' , 'G3': '' , 'G4': '' , 'G5': '' , 'G6': '' , 'G7': '' , 'G8': '', 
    'H1': '' , 'H2': '' , 'H3': '' , 'H4': '' , 'H5': '' , 'H6': '' , 'H7': '' , 'H8': ''
    }

    boardValidity = True

    #check if at least one spot of "board" is invalid
    for spots in board.keys():
        if None == validChessBoardPositions.get(spots): #if the current spot from "board" doesn't match any spot from validChessBoardPositions = invalid board
            print(str(spots) + " is an invalid Spot")
            boardValidity = False
    
    return boardValidity

def isValidChessBoard(toCheckPieces, toCheckSpots):
    if (True == toCheckPieces) and (True == toCheckSpots):
        return True
    else:
        return False

#testing area
# King = König, Queen = Dame, Rook = Turm, Bishop = Läufer, Knight = Springer, Pawn = Bauer
#Chess Board, prefix "w" for "white", prefix "b" for "black" (simple team recognition)
chessBoard = {
    'A1': 'wRook' , 'A2': 'wPawn' , 'A3': '' , 'A4': '' , 'A5': '' , 'A6': '' , 'A7': 'bPawn' , 'A8': 'bRook', 
    'B1': 'wKnight' , 'B2': 'wPawn' , 'B3': '' , 'B4': '' , 'B5': '' , 'B6': '' , 'B7': 'bPawn' , 'B8': 'bKnight', 
    'C1': 'wBishop' , 'C2': 'wPawn' , 'C3': '' , 'C4': '' , 'C5': '' , 'C6': '' , 'C7': 'bPawn' , 'C8': 'bBishop', 
    'D1': 'wKing' , 'D2': 'wPawn' , 'D3': '' , 'D4': '' , 'D5': '' , 'D6': '' , 'D7': 'bPawn' , 'D8': 'bQueen', 
    'E1': 'wQueen' , 'E2': 'wPawn' , 'E3': '' , 'E4': '' , 'E5': '' , 'E6': '' , 'E7': 'bPawn' , 'E8': 'bKing', 
    'F1': 'wBishop' , 'F2': 'wPawn' , 'F3': '' , 'F4': '' , 'F5': '' , 'F6': '' , 'F7': 'bPawn' , 'F8': 'bBishop', 
    'G1': 'wKnight' , 'G2': 'wPawn' , 'G3': '' , 'G4': '' , 'G5': '' , 'G6': '' , 'G7': 'bPawn' , 'G8': 'bKnight', 
    'H1': 'wRook' , 'H2': 'wPawn' , 'H3': '' , 'H4': '' , 'H5': '' , 'H6': '' , 'H7': 'bPawn' , 'H8': 'bRook'
}    

checker1 = checkPieces(chessBoard)
checker2= checkSpots(chessBoard)
print(isValidChessBoard(checker1, checker2))