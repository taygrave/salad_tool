



# dict_state = {}
# dict_types = {}


# #currently just for type dict
# def add_to_dict(new_name, the_key):
#     """Adds data to dictionary if not already present"""
#     if the_key not in dict_types:
#         dict_types[the_key] = []
#     else:
#         if new_name not in dict_types[the_key]:
#             return dict_types[the_key].append(new_name)

# for line in sfile:
#     my_list = line.strip().split(",")
#     vname, vtype, vseason, vstate  = my_list
#     for k,v in dict_state:
#         add_to_dict(vname,vtype)
    
#     dict_state[(vstate,vseason)] = dict_types
       
# print dict_state[('CA', 'Late January')]

# # make dictionaries inside of dictionaries
# #first dictionary will be the state, which then contains dictionaries seasons 
#which then contain dictionary types with a list value of w types of food  
