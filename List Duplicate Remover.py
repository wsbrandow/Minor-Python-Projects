def remove_duplicates(init_list):
    white_list = []
    for i in init_list:
        if i not in white_list:
            white_list.append(i)
    return white_list
    
