#start- 7:20:00
#ends-8:03:00
#working with lists
#follow this syntax. you can store a number of data types in lists.



#guests=['Satya', 'Bill', 'Marsha']
#print(guests)
##getting values in the list is done by indexing e.g. print(guest[-1])- couting backwards.
#print(guests[-1])
##print(guests[0])- counting from the start
#print(guests[0])
##append- adding a value to a list
#guests.append('Charles')
#print(guests)
##remove- removing a value from the list- 
##it removes the first value if one value occurs multiple times
#guests.remove('Bill')
#print(guests)
##del- deletes a value from the list
#del guests[2]
#print(guests)
##insert- inserting a value into the list
#guests.insert(1, 'Tommy')
#print(guests)
##update a value in the list
#guests[1]='Derreck'
#print(guests)
##searching a list
#print(guests.index('Marsha'))

##loops with lists
##use the len() function to get the size of an array/list
#current_guests= len(guests)
#for people in range(current_guests):
#    print(people)

##you can also use the for loop; e.g. for guests in guests:
#for people in guests:
#    print(people)

##sorting through a lists
#guests.sort( )

#challenge
#the party challenge

guestList=['']
coming=''
main_guest=''
plus_one=''
people_bring=''
counter=0

print('Are you coming to the party on saturday night? (yes/no)')
coming=input('').capitalize()
if coming == 'Yes':
    print('what is your name?')
    main_guest=input('')
    guestList.append(main_guest)
    print('How many people do you want to bring? (please use digits e.g. 1,2,3)')
    people_bring=input('')
    people_bring=int(people_bring)

    while counter<people_bring:
        print('kindly tell us their name/s')
        plus_one= input('')
        guestList.append(plus_one)
        counter+=1
       
    for guests in guestList:
        sorted(guests)
        print(guests)
        
    sorted(guests)
    print('See you on Saturday night lol!! ;-)')
else:
    print('You\'re gonna miss out on Saturday night.')
    print('Try again if you change your mind, and bring someone if you can')
    print('Everybody is invited')

print('Good day')

#slicing a list
mylist=[0,1,2,3,4,5,6,7,8,9]
mylist[4:8]