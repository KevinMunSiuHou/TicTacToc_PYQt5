from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import itertools

app = QApplication([])
my_win = QWidget()
MainWindow = QMainWindow()

#General
Button_Title = [[{'But_name':'1'},{'But_name':'2'},{'But_name':'3'}],[{'But_name':'4'},{'But_name':'5'},{'But_name':'6'}],[{'But_name':'7'},{'But_name':'8'},{'But_name':'9'}]]
Result = ['','','','','','','','','']
Player_details = [{'Name':'','Selection':''},{'Name':'','Selection':''}]
game_sol = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]

#Function
def but_fun():
    curr_player = check_turn()
    sender_button = MainWindow.sender()
    if sender_button.text() == 'X' or sender_button.text() == 'O':
        button_display.setText('Invalid input! '+Player_details[curr_player]['Name']+', please re-enter')
    else:
        Result[int(sender_button.text())-1] = Player_details[curr_player]['Selection']
        buttons[sender_button.text()].setText(Player_details[curr_player]['Selection'])
        check_result(curr_player)

def p_details():
    if Player_details[0]['Name'] == '':
        Player_details[0]['Name'] = text_fill.text()
        text_label.setText(Player_details[0]['Name']+', please select the symbol.')
        button_display.setText(Player_details[0]['Name']+', turns!')
        text_fill.clear()
        text_fill.setPlaceholderText('Enter Player 2 Name...')
        text_fill.hide()
        sym_group.show()
    else:
        Player_details[1]['Name'] = text_fill.text()
        if Player_details[0]['Selection'] == 'X':
            Player_details[1]['Selection'] = 'O'
        else:
            Player_details[1]['Selection'] = 'X'
        Intro_Group.hide()
        Button_Group.show()

def btn_sel():
    sender_button = MainWindow.sender()
    Player_details[0]['Selection'] = sender_button.text()
    sym_group.hide()
    text_label.setText('Name :')
    text_fill.show()
    text_label.show()

def check_turn():
    freq = {x:Result.count(x) for x in Result}
    if freq['']%2 != 0:
        curr_player = 0
        button_display.setText(Player_details[1]['Name']+', turns!')
    else:
        curr_player = 1
        button_display.setText(Player_details[0]['Name']+', turns!')
    return(curr_player)

def check_result(curr):
    X = []
    O = []
    for i in [i for i,x in enumerate(Result) if x == 'X']:
        X.append(i+1)
    for i in [i for i,x in enumerate(Result) if x == 'O']:
        O.append(i+1)
    a = [list(x) for x in itertools.combinations(X, 3)]
    b = [list(x) for x in itertools.combinations(O, 3)]
    for n in range(0,len(a)):
        if a[n] in game_sol:
            Button_Group.hide()
            detail_result.setText(Player_details[curr]['Name']+' WIN!!')
            Result_Group.show()
        else:
            pass
    for n in range(0,len(b)):
        if b[n] in game_sol:
            Button_Group.hide()
            detail_result.setText(Player_details[curr]['Name']+' WIN!!')
            Result_Group.show()
        else:
            pass
    if not '' in Result:
        Button_Group.hide()
        detail_result.setText('IS A TIE GAME!!')
        Result_Group.show()

#Info
text_label = QLabel('Name :')
text_fill = QLineEdit('')
text_fill.setPlaceholderText('Enter Player 1 Name...')
but_x = QPushButton('X')
but_o = QPushButton('O')
but_x.clicked.connect(btn_sel)
but_o.clicked.connect(btn_sel)
text_fill.returnPressed.connect(p_details)
Intro_Group = QGroupBox()
sym_group = QGroupBox()

#Button
buttons = {}
Button_Group = QGroupBox()
for n in Button_Title:
    for m in n:
        buttons[m['But_name']] = QPushButton(m['But_name'])
        buttons[m['But_name']].clicked.connect(but_fun)
button_display = QLabel('')

#Result
title_result = QLabel('Results')
detail_result = QLabel('Results show here')
Result_Group = QGroupBox()

#Info Position
H_layout = {}
H_layout[0] = QHBoxLayout()
H_layout[1] = QHBoxLayout()
H_layout[0].addWidget(text_label)
H_layout[0].addWidget(text_fill)
H_layout[1].addWidget(but_x)
H_layout[1].addWidget(but_o)

V_layout = {}
V_layout[0] = QVBoxLayout()
V_layout[1] = QVBoxLayout()
V_layout[0].addLayout(H_layout[0])
V_layout[1].addLayout(H_layout[1])
Intro_Group.setLayout(V_layout[0])
sym_group.setLayout(V_layout[1])

#Button Position
H_layout[2] = QHBoxLayout()
H_layout[3] = QHBoxLayout()
H_layout[4] = QHBoxLayout()
H_layout[5] = QHBoxLayout()
H_layout[2].addWidget(button_display)
for n in range(1,4):
    H_layout[3].addWidget(buttons[str(n)])
for n in range(4,7):
    H_layout[4].addWidget(buttons[str(n)])
for n in range(7,10):
    H_layout[5].addWidget(buttons[str(n)])
V_layout[2] = QVBoxLayout()
V_layout[2].addLayout(H_layout[2])
V_layout[2].addLayout(H_layout[3])
V_layout[2].addLayout(H_layout[4])
V_layout[2].addLayout(H_layout[5])
Button_Group.setLayout(V_layout[2])

#Position Result
H_layout[6] = QHBoxLayout()
H_layout[6].addWidget(title_result)
H_layout[7] = QHBoxLayout()
H_layout[7].addWidget(detail_result,alignment=Qt.AlignCenter)
V_layout[3] = QVBoxLayout()
V_layout[3].addLayout(H_layout[6])
V_layout[3].addLayout(H_layout[7])
Result_Group.setLayout(V_layout[3])

#Final 
V_F_Line = QVBoxLayout()
V_F_Line.addWidget(Intro_Group)
V_F_Line.addWidget(sym_group)
V_F_Line.addWidget(Button_Group)
V_F_Line.addWidget(Result_Group)

sym_group.hide()
Button_Group.hide()
Result_Group.hide()

my_win.setLayout(V_F_Line)
my_win.show()
app.exec_()