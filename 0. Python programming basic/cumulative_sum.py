def cumsum_rec(start_num, end_num):
    if start_num == end_num :
        return end_num
    else :
        return end_num + cumsum_rec(start_num, end_num-1)

start_num = 1
end_num = 5
total = 0
def cumsum_encapsulation():
    global start_num
    global end_num
    global total

    if end_num == start_num:
        total = total + end_num
        return total
    else : 
        total = total + end_num
        end_num = end_num - 1
        return cumsum_encapsulation()

print(cumsum_encapsulation() == cumsum_rec(1,5))