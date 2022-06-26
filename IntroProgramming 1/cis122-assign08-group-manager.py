'''
Assignment: CIS 122 Assignment 07
Author: Edison Nayland Mielke
Description: Make a dictionary
'''
print(">> Welcome to Group Manager <<")
d = {}
group = {}
def create_groups(d):
    group_name_inp2 = ""
    print()
    keys = []
    while True:
        group_name_inp = input("Enter group name (empty to cancel): ")
        if group_name_inp == "":
            break
        group_name_inp2 = group_name_inp
        while True:
            keys_inp = input("Enter field name (empty to stop): ")
            if keys_inp == "":
                break
            keys.append(keys_inp)
    tuple(keys)
    global group
    if len(group) > 0:
        group[group_name_inp2] = keys
    else:
        group = {group_name_inp2: keys}   
print()
def list_groups(d):
    print()
    print("** List of groups **")
    key = sum(map(len, group.values()))
    for key2 in group:
        print (key2,":",key, "properties", group[key2])

    print()
def add_group_data(d):
    print()
    print("**Add group data**")
    list_groups(d)
    while True:
        group_name = input("Enter group (empty to cancel): ")
        if group_name == "":
            break
        for key2 in group:
            if group_name == key2:
                no1 = ((group[key2])[0])
                no2 = ((group[key2])[1])
            else:
                print("please enter valid group")
        ent1 = input("Enter "+ str(no1)+" : ")
        ent2 = input("Enter "+ str(no2)+" : ")
        group['data'] = {no1:ent1,no2:ent2}
        
        print(group)
def list_group_data(d):
    print()
    print("**List group data**")
    list_groups(d)
    while True:
        group_name = input("Enter group (empty to cancel): ")
        if group_name == "":
            break
        for key2 in group:
            if group_name == key2:
                print ((group[key2])[0],"=",((group['data'])[0])[0],(group[key2])[1],"=",((group['data'])[1])[0])
                
                
                
def start():
    grp_mng = True
    while grp_mng:
        command = input("Command (empty or X to quit, ? for help): ")
        if command == "?":
            print("?: List Commands")
            print("C: Create a new group")
            print("A: Add data to a group")
            print("G: List Groups")
            print("L: List data for a group")
            print("X: Exit")
        if command == "a":
            add_group_data(d)
        if command == "g":
            list_groups(d)
        if command == "c":
            create_groups(d)
        if command == "l":
            list_group_data(d)
        if command == "x":
            print ("Exiting group manager")
            break

start()
