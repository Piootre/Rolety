from machine import Pin, PWM
import utime

# Pin configuration
step_pin = Pin(2, Pin.OUT)
dir_pin = Pin(3, Pin.OUT)
enable_pin = Pin(6, Pin.OUT)

# Set the PWM frequency
pwm_frequency = 1000
pwm = PWM(Pin(12))
pwm.freq(pwm_frequency)

# Set the number of steps per revolution and the gear ratio
steps_per_rev = 200
gear_ratio = 1/64

# Set the acceleration and deceleration rates
accel_rate = 5000
decel_rate = 5000

# Set the initial speed and target speed
initial_speed = 1000
target_speed = 5000

# Set the direction
dir_pin.value(1)

# Enable the motor driver
enable_pin.value(0)

# Set the PWM duty cycle to the initial speed
pwm.duty_u16(int(initial_speed/100 * 65535))

# Set the initial step delay and the step count
step_delay = 1/initial_speed * 1000000
step_count = 0

# Rotate the motor
while True:
    # Check if the target speed has been reached
    if step_delay <= 1/target_speed * 1000000:
        break
    
    # Calculate the next step delay
    step_delay = 1/((initial_speed + accel_rate * step_count) / 1000000)
    
    # Update the PWM duty cycle
    pwm.duty_u16(int((initial_speed + accel_rate * step_count)/100 * 65535))
    
    # Step the motor
    step_pin.on()
    utime.sleep_us(int(step_delay/2))
    step_pin.off()
    utime.sleep_us(int(step_delay/2))
    
    # Update the step count
    step_count += 1
    print("1")
# Decelerate the motor
while True:
    # Calculate the next step delay
    step_delay = 1/((initial_speed + accel_rate * step_count - decel_rate * (step_count - int((target_speed-initial_speed)/accel_rate))) / 1000000)
    
    # Update the PWM duty cycle
    pwm.duty_u16(int((initial_speed + accel_rate * step_count - decel_rate * (step_count - int((target_speed-initial_speed)/accel_rate)))/100 * 65535))
    
    # Step the motor
    step_pin.on()
    utime.sleep_us(int(step_delay/2))
    step_pin.off()
    utime.sleep_us(int(step_delay/2))
    
    # Update the step count
    step_count += 1
    print("2")
# Disable the motor driver
enable_pin.value(1)

