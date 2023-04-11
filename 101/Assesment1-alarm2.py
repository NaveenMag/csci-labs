#   Naveen Maghbouleh
        #   CSCI 101 – Section I
        #   Python Assessment 1
        #   References: no one
        #   Time: 1hr 10 minutes 



earlytime = int(input('EARLY> '))
awake_hours = int(input('HOURS> '))
awake_mins = int(input('MINS> '))
awaketime = (awake_hours * 60 + awake_mins - earlytime) % 1440
earlytime_hours = awaketime // 60
earlytime_mins = awaketime % 60
print(f'OUTPUT {earlytime_hours:02d} {earlytime_mins:02d}')