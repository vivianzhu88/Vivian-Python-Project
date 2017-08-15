from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(2)
led3 = LED(3)
led4 = LED(4)

def blink_led1():
    for i in range (1,4):
        led1.on()
        sleep(0.5)
        led1.off()
        sleep(0.5)

def blink_led2():
    for i in range (1,4):
        led2.on()
        sleep(0.5)
        led2.off()
        sleep(0.5)
def blink_led3():
    for i in range (1,4):
        led3.on()
        sleep(0.5)
        led3.off()
        sleep(0.5)
def blink_led4():
    for i in range (1,4):
        led4.on()
        sleep(0.5)
        led4.off()
        sleep(0.5)

sentence = "We are all eager to see the LED blink"

for letter in sentence:
    if (letter == "a"):
        print ("found an 'a'")
        blink_led1()
    elif (letter == "e"):
        print ("found an 'e'")
        blink_led2()
    elif (letter == "i"):
        print ("found an 'i'")
        blink_led3()
    elif (letter == "o"):
        print ("found an 'o'")
        blink_led4()
    sleep(2)
print ("We are done")
        
