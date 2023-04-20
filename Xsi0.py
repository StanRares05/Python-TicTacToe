tabla = [[".",".","."],
         [".",".","."],
         [".",".","."]]


#citim afisare tabla

for i in range(3):
    for j in range(3):
        print(tabla[i][j], end=" ")
    print("\n")
a=0
GameOn = True
while GameOn==True :
    if a%2==0:
        print("PlayerOne(x)")
        rand = int(input("Care este randul dorit?(0,1,2) "))
        coloana = int(input("Care este termenul dorit?(0,1,2) "))
        if rand >= 0 and rand < 3 and coloana >= 0 and coloana < 3 and tabla[rand][coloana]==".":
            tabla[rand][coloana] = "x"
            a+=1
            for i in range(3):
                for j in range(3):
                    print(tabla[i][j], end=" ")
                print("\n")
        else:
            print("incearca din nou")
    else:
        print("PlayerTwo(0)")
        rand = int(input("Care este randul dorit?(0,1,2) "))
        coloana = int(input("Care este termenul dorit?(0,1,2) "))
        if rand>=0 and rand<3 and coloana>=0 and coloana<3 and tabla[rand][coloana]==".":
            tabla[rand][coloana] = "0"
            a+=1
            for i in range(3):
                for j in range(3):
                    print(tabla[i][j], end=" ")
                print("\n")


        else:
            print("incearca din nou")
    #matricefull
    if tabla[0][0]!="." and tabla[0][1]!="." and tabla[0][2]!="." and tabla[1][0]!="." and tabla[1][1]!="." and tabla[1][2]!="." and tabla[2][0]!="." and tabla[2][1]!="." and tabla[2][2]!=".":
        GameOn=False
        #diagonala1
    if tabla[0][0] == "x" and tabla[1][1] == "x" and tabla[2][2] == "x":
        GameOn = False
    if tabla[0][0] == "0" and tabla[1][1] == "0" and tabla[2][2] == "0":
        GameOn = False
        #diagonala2
    if tabla[0][2] == "x" and tabla[1][1] == "x" and tabla[2][0] == "x":
        GameOn=False
    if tabla[0][2] == "0" and tabla[1][1] == "0" and tabla[2][0] == "0":
        GameOn=False
        #rand 1
    if tabla[0][0] == "x" and tabla[1][0] == "x" and tabla[2][0] == "x":
        GameOn = False
    if tabla[0][0] == "0" and tabla[1][0] == "0" and tabla[2][0] == "0":
        GameOn = False
    #rand 2
    if tabla[0][1] == "x" and tabla[1][1] == "x" and tabla[2][1] == "x":
        GameOn = False
    if tabla[0][1] == "0" and tabla[1][1] == "0" and tabla[2][1] == "0":
        GameOn = False
    #rand 3
    if tabla[0][2] == "x" and tabla[1][2] == "x" and tabla[2][2] == "x":
        GameOn = False
    if tabla[0][2] == "0" and tabla[1][2] == "0" and tabla[2][2] == "0":
        GameOn = False
    #coloana 1
    if tabla[0][0] == "x" and tabla[0][1] == "x" and tabla[0][2] == "x":
        GameOn = False
    if tabla[0][0] == "0" and tabla[0][1] == "0" and tabla[0][2] == "0":
        GameOn = False
    #coloana 2
    if tabla[1][0] == "x" and tabla[1][1] == "x" and tabla[1][2] == "x":
        GameOn = False
    if tabla[1][0] == "0" and tabla[1][1] == "0" and tabla[1][2] == "0":
        GameOn = False
    #coloana 3
    if tabla[2][0] == "x" and tabla[2][1] == "x" and tabla[2][2] == "x":
        GameOn = False
    if tabla[2][0] == "0" and tabla[2][1] == "0" and tabla[2][2] == "0":
        GameOn = False
