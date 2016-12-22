from locations import location_dict

# Write your code below this line.

def GetLocationPath():

    input_location = input('Enter Location :')
    key = input_location

    if key in location_dict:
        print(key)
        print(location_dict[key])
    
        for val in location_dict:
            if location_dict[key] == val:
                print(location_dict[val])
            
                for val_2 in location_dict:
                    if location_dict[val] == val_2:
                        print(location_dict[val_2])

                        for val_3 in location_dict:
                            if location_dict[val_2] == val_3:
                                print(location_dict[val_3])
    else:
        print('Not in the Dictionary. You tried it though.')
GetLocationPath()


#input should be a key
#key should have value
#value should be a key 

#does not print location path on same line
