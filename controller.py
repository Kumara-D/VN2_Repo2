from input_file import user_input
user_data = user_input()

user_name = user_data['response']['Name']
user_id = user_data['response']['ID']
user_loc = user_data['response']['Location']

def validate_data():
    val_dict = {}
    val_dict['Name'] = user_name
    if user_id > 99:
        val_dict['ID'] = user_id * 3
    else:
        raise ValueError('Id should be of minimum 3 characters')
    if user_loc == "Bengaluru": 
        val_dict['Location'] = user_loc
    else:
        raise ValueError('Your location must be Bengaluru')
    return val_dict

        
        