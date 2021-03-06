hours = 0
ampm = False
minutes = 0
adjust = 0
time = ""
dodo = 0

def on_button_pressed_a():
    global hours
    if hours < 23:
        hours += 1
    else:
        hours = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ampm
    ampm = not (ampm)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global minutes
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global adjust, time
    adjust = hours
    if ampm:
        if hours > 12:
            adjust = hours - 12
        elif hours == 0:
            adjust = 12
    time = "" + str(adjust)
    time = "" + time + ":"
    if minutes < 10:
        time = "" + time + "0"
    time = "" + time + ("" + str(minutes))
    if ampm:
        if hours > 11:
            time = "" + time + "PM"
        else:
            time = "" + time + "AM"
    led.set_brightness(255)
    basic.show_string(time)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global minutes, hours
    basic.pause(60000)
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
        if hours < 23:
            hours += 1
        else:
            hours = 0
basic.forever(on_forever)

def on_forever2():
    global dodo
    if hours < 8:
        dodo = 1
    else:
        if hours >= 20:
            dodo = 1
        else:
            dodo = 0
    if dodo == 1:
        led.set_brightness(33)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    else:
        led.set_brightness(130)
        basic.show_icon(IconNames.HEART)
basic.forever(on_forever2)
