import urllib.request, json
from .Section import *
from  .timeConverstion import *
import itertools
from .Ranking import *

def schedule(courses):
    course_ids = courses
    with urllib.request.urlopen("http://api.umd.io/v0/courses/"+course_ids) as url:
        c = url.read()

    course_json = json.loads(c)
    possible_sections = []
    ctr = len(course_ids.split(","))
    for i in course_json:
        current_course = i["course_id"]
        sections = i["sections"]
        for k in sections:
            with urllib.request.urlopen("http://api.umd.io/v0/courses/sections/"+k) as url:
                section_info = json.loads(url.read())

            meetings = section_info["meetings"][0]
            dates = meetings["days"]
            start_time = meetings["start_time"]
            end_time = meetings["end_time"]
            instructors = section_info["instructors"][0]
            seats = section_info["seats"]
            course_id = section_info["course"]
            section_id = section_info["section_id"]
            toAdd = Section(section_id,course_id,instructors,seats,dates,start_time,end_time)
            possible_sections.append(toAdd)
            
    possible_comb = itertools.combinations(possible_sections,ctr)
    possible_comb_list = []
    for i in possible_comb:
        toAdd = []
        for k in i:
            toAdd.append(k)
        possible_comb_list.append(toAdd)

    d = filter(possible_comb_list)
    ranked_list = rank(d)

    sorted_list = sorted(ranked_list,key=lambda x: x[1], reverse=True)
    o,p = sorted_list[0]
    return o

for i in schedule("CMSC250,CMSC422"):
    print(i.get_section_id())
