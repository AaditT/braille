import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)



# INITIALIZE PWM

a = GPIO.PWM(7, 50)
b = GPIO.PWM(8, 50)

# START PWM

a.start(7.5)
b.start(7.5)

a1.ChangeDutyCycle(2.5)
a2.ChangeDuty

class Servo:
    def __init__(self, pwm_sig):
        self.pwm_sig = pwm_sig
        self.isOn = False

    def off(self):
        if self.isOn == False:
            self.pwm_sig.ChangeDutyCycle(2.5)
            time.sleep(0.3)
            self.isOn = True
        else:
            pass

    def on(self):
        if self.isOn == True:
            self.pwm_sig.ChangeDutyCycle(7.5)
            time.sleep(0.3)
            self.isOn = False
        else:
            pass

    def hundredeighty_deg(self):
        self.pwm_sig.ChangeDutyCycle(12.5)
        time.sleep(0.3)

    def reset(self):
        self.off()

    def stop(self):
        self.pwm_sig.stop()


a1 = Servo(a)
a2 = Servo(b)
a3 = Servo(c)
b1 = Servo(d)
b2 = Servo(e)
b3 = Servo(f)


def output(big_array):
    for letters in big_array:

        if letters[0][0] == 0:
            a1.off()
        elif letters[0][0] == 1:
            a1.on()
#        if letters[0][1] == 0:
#            b1.off()
#        elif letters[0][1] == 1:
#            b1.on()

        if letters[1][0] == 0:
            a2.off()
        elif letters[1][0] == 1:
            a2.on()
#        if letters[1][1] == 0:
#            b1.off()
#        elif letters[1][1] == 1:
#            b1.on()

#        if letters[2][0] == 0:
#            a3.off()
#        elif letters[2][0] == 1:
#            a3.on()
#        if letters[2][1] == 0:
#            b3.off()
#        elif letters[2][1] == 1:
#            b3.on()

    a1.reset()
    a2.reset()
#    a3.reset()
#    b1.reset()
#    b2.reset()
#    b3.reset()

# def listenForTrigger():
#    button_state = GPIO.input(23)
#    if button_state == False:
#        os.system("fswebcam img.jpg")
#        output(imgToBraille("img.jpg"))


try:
    while True:
        print("Listening for trigger...")
#        listenForTrigger()

except KeyboardInterrupt:
#    a1.stop()
#    a2.stop()
#    a3.stop()
#    b1.stop()
#    b2.stop()
#    b3.stop()

    GPIO.cleanup()
