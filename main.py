
hours = 0
minutes = 0
adjust = 0
time = ""
ampm = False

def on_button_pressed_a():
    global hours
    if hours < 23:
        hours += 1
    else:
        hours = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global minutes
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global ampm
    ampm = not (ampm)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

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


def on_gesture_shake():
    global adjust, time
    adjust = hours
    if ampm:
        if hours > 12:
            adjust = hours - 12
        else:
            if hours == 0:
                adjust = 12
    time = "" + str(adjust)
    time = time + ":"
    if minutes < 10:
        time = time + "0"
    time = time + str(minutes)
    if ampm:
        if hours > 11:
            time = time + "PM"
        else:
            time = time + "AM"
    basic.show_string(time)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)