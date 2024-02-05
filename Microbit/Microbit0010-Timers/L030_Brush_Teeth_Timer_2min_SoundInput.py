# (C) 2024. mastershin at gmail.com
# https://github.com/mastershin/learn-microbit-101

def on_button_pressed_a():
    global timer_sec
    timer_sec = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global timer_sec
    if timer_sec < max_seconds:
        timer_sec = max_seconds
        update_display()
def update_display():
    for i in range(5):
        for j in range(5):
            if timer_sec / second_per_LED > i * 5 + j:
                led.plot(j, i)
            else:
                led.unplot(j, i)
timer_sec = 0
second_per_LED = 0
max_seconds = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

# set for 2 minutes (125 seconds)
max_seconds = 125

# each LED represents 5 seconds since there are 25 leds
second_per_LED = 5

def on_every_interval():
    global timer_sec
    if timer_sec > 0:
        timer_sec += 0 - 1
        update_display()
        if timer_sec <= 0:
            basic.show_icon(IconNames.HEART)
            music.play_melody("E B C5 A B G A F", 200)
        else:
            music.play_melody("G4", 1000)
    else:
        timer_sec += 0 - 1
        if timer_sec < -10:
            timer_sec = 0
            basic.clear_screen()
loops.every_interval(1000, on_every_interval)

def on_forever():
    # Check for sound to initiate the timer
    if input.sound_level() > 180:
        on_button_pressed_b()
basic.forever(on_forever)

