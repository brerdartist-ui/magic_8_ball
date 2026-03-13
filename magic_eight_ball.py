import random
import time
import PySimpleGUI as sg

answer = [
    'It is certain',
    'Reply hazy', 
    'Try again',
    "Don’t count on it",
    'It is decidedly so',
    'Ask again later',
    'My reply is no',
    'Without a doubt',
    'Better not tell you now',	
    'My sources say no',
    'Yes definitely',
    'Cannot predict now',	
    'Outlook not so good',
    'You may rely on it',	
    'Concentrate and ask again',	
    'Very doubtful',
    'As I see it, yes',		
    'Most likely',		
    'Outlook good',		
    'Yes',		
    'Signs point to yes'
]



eight_ball = print(random.choice(answer))
layout = [[sg.Text(eight_ball)], [sg.Button("OK")]]
window = sg.Window(title="Magic 8 Ball", layout=[[]])

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()