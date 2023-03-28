P = int(input("Enter Tot. rent: "))
util = int(input("Enter Tot. utility charge: "))
n = int(input("No. of people: "))
u = util/n
D = input('Do you want to enter the names of people?[y/n]: ')
C = input('Do you want to split the rent equally?[y/n]: ')
if (D.lower() == 'n'):
    if (C.lower() == 'y'):
        def equal(n):
            return P/n
        for a in range(n):
            print("The rent for person{} is".format(a+1), equal(n) + u)
    elif (C.lower() == 'n'):
        l = []
        for p in range(n):
            if sum(l) > 100:
                raise Exception('Check percentages'.upper())
            else:
                l.append((int(input("Remaining share:{} \n Percentage for person{}:".format((100 - sum(l)), p + 1)))))


        if sum(l) != 100:
            print("Check percentages".upper())
        else:
            def unequal(l):
                R = []
                for i in range(n):
                    R.append((l[i]/100)*P)
                return R,sum(R)

            for a in range(n):
                print("The rent for person{} is".format(a+1), unequal(l)[0][a] + u)
    else:
        print("Answer 'y' to split equally and 'n' to split unequally")
elif (D.lower() == 'y'):
    p = []
    for i in range(n):
        p.append(input('Enter name of person{}: '.format(i+1)))
    if (C.lower() == 'y'):
        def equal(n):
            return P/n
        for a in range(n):
            print("The rent for {} is".format(p[a]), equal(n) + u)
    elif (C.lower() == 'n'):
        l = []
        for b in range(n):
            if sum(l) > 100:
                raise Exception('Check percentages'.upper())
            else:
                l.append((int(input("Remaining share:{} \n Percentage for {}:".format((100 - sum(l)), p[b])))))


        if sum(l) != 100:
            print("Check percentages".upper())
        else:
            def unequal(l):
                R = []
                for c in range(n):
                    R.append((l[c]/100)*P)
                return R,sum(R)

            for d in range(n):
                print("The rent for {} is".format(p[d]), unequal(l)[0][d] + u)
    else:
        print("Answer 'y' to split equally and 'n' to split unequally")

