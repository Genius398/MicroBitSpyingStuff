from microbit import *
import radio
import log
radio.config(group=3)

while True:
    if radio.receive()=='au':
        for i in range(1,10):
            log.add({'Sound Levels':microphone.sound_level()})
            microphone.current_event()
    elif radio.receive()=='tem':
        for j in range(1,10):
            log.add({'Temperature Levels':temperature()})

    if button_a.was_pressed():
        radio.send('al')
