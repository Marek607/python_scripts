
def printBoard(board):
    print(board['1'], "|", board['2'], "|", board['3'])
    print("--+---+--")
    print(board['4'], "|", board['5'], "|", board['6'])
    print("--+---+--")
    print(board['7'], "|", board['8'], "|", board['9'])

def printBoardexample():
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

def win(board,kto):
    if ((board['1'] == board['2'] == board['3'] == kto) or (board['4'] == board['5'] == board['6']==kto) or (board['7'] == board['8'] == board['9'] == kto) or (board['1'] == board['4'] == board['7'] ==kto)
    or (board['2'] == board['5'] == board['8'] ==kto) or (board['3'] == board['6'] == board['9'] ==kto) or (board['1'] == board['5'] == board['9'] == kto) or (board['3'] == board['5'] == board['7']) ==kto):
        return True
    else:
        return False

board = {'1': ' ','2': ' ','3': ' ','4' : ' ','5': ' ','6': ' ','7': ' ','8':' ','9': ' '}


print("Oto plansza z numerami pól przypadającymi dla gracza")
printBoardexample()
kto = 'x'

for i in range(9):
    gdzie = input("Podaj numer pola gdzie mam wstawić znak dla {}: ".format(kto))
    board[gdzie] = kto
    if win(board,kto) == True:
        print("Gratulacje", kto,"wygrałeś!")
        printBoard(board)
        break
    if kto == 'x':
        kto = 'o'
    else:
        kto = 'x'
    printBoard(board)
