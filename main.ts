let hours = 0
let ampm = false
let minutes = 0
let adjust = 0
let time = ""
let dodo = 0
input.onButtonPressed(Button.A, function () {
    if (hours < 23) {
        hours += 1
    } else {
        hours = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    ampm = !(ampm)
})
input.onButtonPressed(Button.B, function () {
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    adjust = hours
    if (ampm) {
        if (hours > 12) {
            adjust = hours - 12
        } else if (hours == 0) {
            adjust = 12
        }
    }
    time = "" + adjust
    time = "" + time + ":"
    if (minutes < 10) {
        time = "" + time + "0"
    }
    time = "" + time + ("" + minutes)
    if (ampm) {
        if (hours > 11) {
            time = "" + time + "PM"
        } else {
            time = "" + time + "AM"
        }
    }
    led.setBrightness(255)
    basic.showString(time)
})
basic.forever(function () {
    basic.pause(60000)
    if (minutes < 59) {
        minutes += 1
    } else {
        minutes = 0
        if (hours < 23) {
            hours += 1
        } else {
            hours = 0
        }
    }
})
basic.forever(function () {
    if (hours < 8 || hours >= 20) {
        dodo = 1
        if (hours == 7 && minutes >= 40) {
            dodo = 2
        }
    } else {
        dodo = 0
    }
    if (dodo == 1) {
        led.setBrightness(33)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else {
        if (dodo == 2) {
            basic.showIcon(IconNames.Happy)
        } else {
            led.setBrightness(130)
            basic.showIcon(IconNames.Heart)
        }
    }
})
