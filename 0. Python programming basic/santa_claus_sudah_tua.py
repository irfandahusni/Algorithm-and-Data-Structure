# Reference  : https://realpython.com/python-thinking-recursively/
# At his age, santa clause is no longer able to deliver all the gifts by himself. 
# So he build a delivery startup with his elves and start delivering the gifts.
# The delivery process are explaned in in this steps : 
# 1. Assign an elf and give all the gifts delivery work for him. 
# 2. Give this little man a title and responsibilities to command other elves based on the number of houses :
#   2.1 If he is a manager, he can appoint two elves and divide the work among them 
#   2.2 If he is a worker, he has to deliver the package by himself. 

houses = ["Andika", "Kangen", "Band", "Kufaku", "Matalinga"]

#Each function call represents an elf doing his work
def deliver_gifts(houses) : 
    #If the house number is 1, then the first elf should deliver it by himself 
    if len(houses) == 1 :
        house = houses[0]
        print("Delivering presents to ", house)

    #If the house is more than one, then the first elf should delegate to the other elves
    else : 
        mid = len(houses)//2
        first_half = houses[:mid]
        second_half = houses[mid:]

        #Divide the work among two elves
        deliver_gifts(first_half)
        deliver_gifts(second_half)

deliver_gifts(houses)