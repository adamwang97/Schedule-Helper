from .timeConverstion import *
class Section:
    section_id = 1
    course_id = 1
    instructors = 1
    seats = 1
    dates = 1
    start_time = 1
    end_time = 1

    def __init__(self,section_id,course_id,instructors,seats,dates,start_time,end_time):
        self.section_id = section_id
        self.course_id = course_id
        self.instructors = instructors
        self.seats = seats
        self.dates = dates
        if(start_time != ""):
            self.start_time = timeConversion(start_time)
        else:
            self.start_time = start_time
        if(end_time != ""):
            self.end_time = timeConversion(end_time)
        else:
            self.end_time = end_time
    
    def toString(self):
        print(self.section_id + "\n")
        print(self.course_id + "\n")
        print(self.instructors + "\n")
        print(self.seats + "\n")
        print(self.dates + "\n")
        print(self.start_time + "\n")
        print(self.end_time + "\n")

    def get_section_id(self):
        return self.section_id

    def get_course_id(self):
        return self.course_id

    def get_instructors(self):
        return self.instructors

    def get_seats(self):
        return self.seats

    def get_dates(self):
        return self.dates

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
    
def valid(s1,s2):
    if(s1.get_seats() == 0 or s2.get_seats() == 0):
        return False
    if(s1.get_course_id() == s2.get_course_id()):
        return False
    start = compare(s1.get_start_time(),s2.get_start_time())
    end = compare(s1.get_end_time(),s2.get_end_time())
    checker = False
    s1_dates = s1.get_dates()
    s2_dates = s2.get_dates()
    if(("M" in s1_dates) and ("M" in s2_dates)):
        checker = True
    if(("W" in s1_dates) and ("W" in s2_dates)):
        checker = True
    if(("Tu" in s1_dates) and ("Tu" in s2_dates)):
        checker = True
    if(("Th" in s1_dates) and ("Th" in s2_dates)):
        checker = True
    if(("F" in s1_dates) and ("F" in s2_dates)):
        checker = True
    if(checker == True):
        if(start == 0 or end == 0):
            return False
        if(end != start):
            return False
    return True
def filter(possible_comb_list):

    toReturn = []
    for i in possible_comb_list:
        ctr = True
        for j in range(0,len(i)):
            cur = i[j]
            for k in range(j+1,len(i)):
                second = i[k]
                if(valid(cur,second) == False):
                    ctr = False
        if(ctr == True):
            toReturn.append(i)
    return toReturn
