


def booking():
    name=input("Name:")
    phone=int(input("Phone number"))
    age=int(input("Age"))
    print("Are you phyisically handicapped\n Yes : 1 \n No: 2\n ")
    pc=int(input())
    if pc == 1:
        hc= True
    else:
        hc = False


    s=(['name','name','name'],
        ['name','name','name'],
        ['name','name','name'],
        ['name''name','name'],
        ['name','name','name'],
        ['name','name','name'])
    sno=([1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12],
        [13,14,15],
        [16,17,18])
    if age > 45 and hc == False:
        for i in range(0,3):
            for j in range(0,2):
                s[i][j]=name
                break
    elif age < 45 and hc==False:
        for i in range(3,5):
            for j in range(3,2):
                    s[i][j]=name
                    break
    elif hc == True:
        for i in range(0,3):
            for j in range(0,2):
                s[i][j]=name
                
    print("Passenger Details: \n")
    print("Name:{0}\n".format(name))
    print("Contact No: {0}\n".format(phone))
    print("Age:{0}\n".format(age))
    if age>45 and hc==False:
        age_category="Senior Citizen"
    elif age<45 and hc==False:
        age_category="Young"
    elif hc==True:
        age_category="Handicaped"
    print("category:{0}\n".format(age_category))
    print("following seats acn be allocated:\n") 
    for i in range(0,5):
        for j in range(0,2):
            if s[i][j]==name:
                
                print("seat no:",sno[i][j])
                break
                
r=int(input("Press 1 to run program\nPress 0 to exit program\n"))
while r==1:
    booking()
    r=int(input("Press 1 to run program\nPress 0 to exit program\n"))
