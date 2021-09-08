def list_sum_recursive(input_list):
    if input_list == []:
        return 0
    
    else :
        head = input_list[0]
        tail = input_list[1:]
        return head + list_sum_recursive(tail)
        