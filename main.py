# IMPORTS
import tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
    
# MAIN FRAME
root = tkinter.Tk()
root.geometry("650x400+0+0")
root.wm_title("Cálculo de Área")

# FUNCTIONS
def lados():
    global ladoss
    ladoss = int(inputComment.get())
    return ladoss

def pontos():    
    global pontoslist
    pontos = list(inputPoint.get())
    pontoslist = []
    
    for i in range(len(pontos)):
        try:
            if (pontos[i + 1] == ' ') and (pontos[i + 2] == ' '):
                pontoslist.append((f'{pontos[i]}{pontos[i - 2]}'))
        except:
            continue
    pontoslist.append((f'{pontos[len(pontos) - 1]}{pontos[len(pontos) - 3]}'))

    for i in range(len(pontoslist)):
        pontoslist[i] = list(pontoslist[i])
    for i in range(len(pontoslist)):
        for j in range(0, 2):
            pontoslist[i][j] = int(pontoslist[i][j])

    return pontoslist

def area():
    global Area
    coordenadas = pontoslist

    soma1 = 0    
    for i in range(0, ladoss):
        if i == ladoss - 1:
            soma1 += coordenadas[ladoss - 1][0] * coordenadas[0][1] 
            break
        soma1 += (coordenadas[i][0] * coordenadas[i+1][1])
    
    soma2 = 0    
    for i in range(0, ladoss):
        if i == ladoss - 1:
            soma2 += coordenadas[ladoss - 1][1] * coordenadas[0][0]
            break
        soma2 += (coordenadas[i][1] * coordenadas[i+1][0])

    area = abs(soma1 - soma2) / 2
    Area = (f'O polígono de {ladoss} lados e pontos {inputPoint.get()} tem uma área de {area:.2f} unidades de área')

    return area #print(f'{AreaPoligono:.2f}')

def addArea():
    pontos()
    area()
    areaList.insert(0, Area)

# FRAME APP 
appFrame = tkinter.LabelFrame(root, text="Cálculo de Área de um Polígono")
appFrame.place(relwidth=1, relheight=1, rely=0)

'''
Esta parte é para os inputs.
'''
#FRAME LADOS
inputCommentFrame = tkinter.LabelFrame(appFrame, text="Número de lados do polígono:")
inputCommentFrame.place(relwidth=1, relheight=0.1)

inputComment = tkinter.Entry(inputCommentFrame)
inputComment.place(relwidth=1, relheight=1)

#FRAME PONTOS
inputPointFrame = tkinter.LabelFrame(appFrame, text="Pontos do polígono no plano cartesiano em sentido horário ou anti-horário (Exemplo: 2 2  7 7  4 7):")
inputPointFrame.place(relwidth=1, relheight=0.1, rely=0.1)

inputPoint = (tkinter.Entry(inputPointFrame))
inputPoint.place(relwidth=1, relheight=1)

# BUTTONS
btnComment = tkinter.Button(inputCommentFrame, text="Confirmar", command=lados)
btnComment.place(relwidth=0.25, relheight=1, relx=0.75)

btnComment = tkinter.Button(inputPointFrame, text="Confirmar", command=addArea)
btnComment.place(relwidth=0.25, relheight=1, relx=0.75)

'''
Esta parte é para o output
'''
# FRAME AREA 
areaFrame = tkinter.LabelFrame(root, text="A área do polígono é:")
areaFrame.place(relwidth=1, relheight=0.5, rely=0.3)

areaList = tkinter.Listbox(areaFrame)
areaList.place(relwidth=1, relheight=1)

# START APP
root.mainloop()