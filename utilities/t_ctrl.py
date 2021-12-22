from time import time

last_time = time()
dt = 1

def adjust_delta_time():
    global last_time
    global dt

    dt = time() - last_time
    dt *= 60
    last_time = time()