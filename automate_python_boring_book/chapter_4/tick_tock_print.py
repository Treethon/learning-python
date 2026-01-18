import time

def tick_tock(seconds):
        while seconds >= 1:
            print('Tick...')
            seconds -= 1
            time.sleep(1)
            if seconds >= 1:
                print('Tock...')
                seconds -= 1
                time.sleep(1)
            else:
                 break
        return 'Times up!'
             
user_input = input('How many seconds?: ')
print(tick_tock(int(user_input)))
