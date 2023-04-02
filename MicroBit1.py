from microbit import *
import radio
import music
radio.config(group=3)

while True:
    if button_a.was_pressed():
        radio.send("au")
    elif button_b.was_pressed():
        radio.send("tem")

    if radio.receive():    
        music.play(['d','a','d','a'])
        music.stop()
