import random

#added keyboard logic
keyboard = {'Up': False, 'Left': False, 'Down': False, 'Right': False}

def key_press(event):
    if event.keysym == 'Up':
        keyboard['Up'] = True
    if event.keysym == 'Down':
        keyboard['Down'] = True
    if event.keysym == 'Left':
        keyboard['Left'] = True
    if event.keysym == 'Right':
        keyboard['Right'] = True

def key_release(event):
    if event.keysym == 'Up':
        keyboard['Up'] = False
    if event.keysym == 'Down':
        keyboard['Down'] = False
    if event.keysym == 'Left':
        keyboard['Left'] = False
    if event.keysym == 'Right':
        keyboard['Right'] = False
    
