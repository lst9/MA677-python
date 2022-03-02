# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat Feb 26 16:07:56 2022

# @author: shutingli
# """

def read_file(f): 
    first_every_2 = ()
    second_every_2 = ()
    line_count = 0

    with open(f,'r') as friends:
        content=friends.readlines()
    for row in content:
        stripped_line = row.replace("\n", "") 
        if line_count%2 == 0:
            first_every_2 += (stripped_line,)
            
        elif line_count%2 == 1:
            second_every_2 += (stripped_line,) 
            
        line_count += 1
    return (first_every_2, second_every_2)

name, phone = read_file(f='friends.txt')

def change_format_phone(phone):
    clean_phone=()
    for i in phone:
        line=i.replace("-","")
        line=line.replace(" ","")
        line=line.replace("(","")
        line=line.replace(")","")
        clean_phone += (line,)
    return clean_phone

clean_phone = change_format_phone(phone)

start_phone = ()
for i in clean_phone:
    state = i[:3]
    start_phone += (state,)


############
code, area = read_file(f='map_areacodes_states.txt')

mapping = dict(zip(code, area))

friendarea=()
for i in start_phone:
    state = mapping[i]
    friendarea += (state,)

print('You have {} friends!'.format(len(set(name))))
print('They live in {}'.format(set(friendarea)))
