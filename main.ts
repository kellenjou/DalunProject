input.onButtonPressed(Button.A, function () {
    mbit_小车类.CarCtrlSpeed(mbit_小车类.CarState.Car_Left, speed)
})
input.onButtonPressed(Button.AB, function () {
    mbit_小车类.CarCtrlSpeed(mbit_小车类.CarState.Car_Run, speed)
})
input.onButtonPressed(Button.B, function () {
    mbit_小车类.CarCtrlSpeed(mbit_小车类.CarState.Car_Right, speed)
})
let speed = 0
speed = 100
basic.forever(function () {
    if (mbit_小车类.Avoid_Sensor(mbit_小车类.enAvoidState.OBSTACLE)) {
        mbit_小车类.RGB_Car_Big2(mbit_小车类.enColor.Red)
    } else {
        mbit_小车类.RGB_Car_Big2(mbit_小车类.enColor.White)
    }
})
