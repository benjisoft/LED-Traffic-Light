import RPi.GPIO as GPIO
import time

answer = "y"
while (answer == "y")

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)

    print "Red Light"

    GPIO.output(17,GPIO.HIGH)

    time.sleep(2)

    print "Yellow Light"

    GPIO.output(18,GPIO.HIGH)

    time.sleep(2)

    print "Green Light"

    GPIO.output(17,GPIO.LOW)

    time.sleep(2)

    print "Do you want to continue? (y/n)"
    answer = raw_input()

print "Thank You"
