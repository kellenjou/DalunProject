def on_button_pressed_a():
    mbit_小车类.car_ctrl_speed(mbit_小车类.CarState.CAR_LEFT, SPEED)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    mbit_小车类.car_ctrl_speed(mbit_小车类.CarState.CAR_RUN, SPEED)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    mbit_小车类.car_ctrl_speed(mbit_小车类.CarState.CAR_RIGHT, SPEED)
input.on_button_pressed(Button.B, on_button_pressed_b)

SPEED = 0
SPEED = 100

def on_forever():
    if mbit_小车类.Avoid_Sensor(mbit_小车类.enAvoidState.OBSTACLE):
        mbit_小车类.RGB_Car_Big2(mbit_小车类.enColor.RED)
    else:
        mbit_小车类.RGB_Car_Big2(mbit_小车类.enColor.WHITE)
basic.forever(on_forever)
