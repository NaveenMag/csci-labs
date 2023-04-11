#   Naveen Maghbouleh
        #   CSCI 101 – Section I
        #   Python Assessment 1
        #   References: no one
        #   Time: 50 minutes 

earlytime = 0
ealrytime_hours = 0
earlytime_mins = 0
awake_hours = 0
awake_mins = 0
current_time_mins = 60
current_time_hours = 23
fixedtime_mins = 0
fixedtime_hrs = 0
earlytime = int(input('EARLY> '))
awake_hours = int(input('HOURS> '))
awake_mins = int(input('MINS> '))
awaketime = awake_hours * 60 + awake_mins
earlytime_hours = earlytime // 60
earlytime_mins = earlytime % 60
if awaketime < earlytime:
    fixedtime_hrs = (earlytime - awaketime) // 60
    fixedtime_mins = (earlytime - awaketime) % 60
    current_time_mins = (current_time_mins - fixedtime_mins) % 60
    current_time_hours = current_time_hours - fixedtime_hrs + (current_time_mins // 60)
    print(f'OUTPUT {current_time_hours:02d} {current_time_mins:02d}')
else:
    fixedtime_hrs = (awaketime - earlytime) // 60
    fixedtime_mins = (awaketime - earlytime) % 60
    print(f'OUTPUT {fixedtime_hrs:02d} {fixedtime_mins:02d}')