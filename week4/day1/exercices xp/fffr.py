amily = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
prix1 = 0
prix2 = 10
prix3 = 15
for i in family.values():

    if(i<3):
        prix1=0
    elif(3<=i<12):
        prix2=10

    elif(i>=12):
        prix3=15

    s = prix1 + prix2 + prix3
    print(s)
