
sfile = open("db.txt")

dict_state = {}
dict_seasons = {}
dict_types = {}

#process the file and build the necessary dictionaries

#currently just for type dict
def add_to_dict(new_name, the_key):
    """Adds data to dictionary if not already present"""
    if the_key not in dict_types:
        dict_types[the_key] = []
    else:
        if new_name not in dict_types[the_key]:
            dict_types[the_key].append(new_name)




for line in sfile:
    entry = line.strip()
    my_list = entry.split(",")
    vname, vtype, vseason, vstate  = my_list

    dict_state[(vstate,vseason)] = []

    add_to_dict(vname,vtype)









    # if vname not in dict_types.values():
    #     dict_types[vtype] = [vname]
    #     type_list = dict_types[vtype]
    # else:
    #     type_list.append(vname)






    # dict_types[vtype] = []
    # type_list = dict_types[vtype]

    # if vname not in dict_types.values():
    #     type_list.append(vname)



#for print debugging
print dict_state.items()
print "*" * 10
print dict_types.items()
print "*" * 10

    



# make dictionaries inside of dictionaries
#first dictionary will be the state, which then contains dictionaries seasons 
    #which then contain dictionary types with a list value of w types of food  


    #searching: I live in X state, the time frame is X, I want X# of X types of food. 
    