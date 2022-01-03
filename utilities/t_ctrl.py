from pygame import time

last_time = time.get_ticks()
dt = 1

def adjust_delta_time():
    global last_time
    global dt
    
    new_time = time.get_ticks()
    dt = new_time - last_time
    last_time = new_time
    dt = (dt/1000) * 60