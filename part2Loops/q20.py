import time

def countdown(secs):
    while secs > 0:
        mins, secs_remaining = divmod(secs, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs_remaining)  
        print(time_format)  
        time.sleep(1)
        secs -= 1
    print("Time's up!") 

countdown(200)

