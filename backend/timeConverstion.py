def timeConversion(s):
    time = s.split(':')
    x = (time[1])
    if x[2:4] == "am":
        if time[0] == "12":
            return ("{}:{}".format("00",time[1][0:2]))
        else:
            return ("{}:{}".format(time[0],time[1][0:2]))
    else:
        if time[0] == "12":
            return ("{}:{}".format(time[0],time[1][0:2]))
        else:
            return ("{}:{}".format(int(time[0])+12,time[1][0:2]))

#1 if t1 > t2
#-1 if t1 < t2
#0 if t1 = t2
def compare(t1,t2):
    time1 = t1.split(':')
    time2 = t2.split(':')
    
    time1_hour = int(time1[0])
    time1_min = int(time1[1])

    time2_hour = int(time2[0])
    time2_min = int(time2[1])
    
    if(time1_hour > time2_hour):
        return 1
    if(time1_hour < time2_hour):
        return -1
    if(time1_hour == time2_hour):
        if(time1_min > time2_min):
            return 1
        if(time1_min < time2_min):
            return -1
        if(time1_min == time2_min):
            return 0
