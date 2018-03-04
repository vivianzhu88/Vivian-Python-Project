from gpiozero import Button
from gpiozero import Motor
from time import sleep

motor = Motor(forward=17, backward=18)

sensor = Button(4)
start  = Button(3)



while True:
	if start.is_pressed and not (sensor.is_pressed):
		print ("Sensor not active and moving foward")
		motor.forward()
		

	elif start.is_pressed and sensor.is_pressed:
		motor.stop()
		
		print ("sensor active")
		print ("End point reached")
		sleep (2)
		motor.backward()
		sleep (10)
	#elif start.is_pressed:
	#	print ("Motor rotating in reverse direction")
	#	motor.backward()
	else:
		print ("Motor stopped, unknown state")
		motor.stop()


