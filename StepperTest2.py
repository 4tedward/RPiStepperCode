# Operational Test for RPi SBC Stepper Hat 

import PiMotor
import time

m1 = PiMotor.Stepper("STEPPER1")

# Rotate Stepper 1 Contiously in forward/backward direction
while True:
    m1.forward(0.1,20)  # Delay and rotations
    time.sleep(2)
    m1.backward(0.1,20)
    time.sleep(2)
    
    m1.forward(0.1,100)  # Delay and rotations
    time.sleep(2)
    m1.backward(0.1,100)
    time.sleep(2)
    
     m1.forward(0.01,600)  # Delay and rotations
    time.sleep(2)
    m1.backward(0.01,600)
    time.sleep(2)
