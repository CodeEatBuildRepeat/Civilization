print("  ____                                         ___      _     _______         ____    ")
print(" |        ||   |     |     ||   |        ||   |        | |       |      ||   |    |   |\   |   ")
print(" |        ||    |   | _    ||   |        ||   |___    |   |      |      ||   |    |   | \  |   ")
print(" |        ||     | | |-|   ||   |        ||       |   |___|      |      ||   |    |   |  \ |   ")
print(" |____    ||      | ^|-|^^ ||   |_____   ||    ___|   |   |      |      ||   |____|   |   \| alfa v2.5 INCREMENTING DEPT")
print("                                                                                                        by text game studios")
print("                                         Loading...          ")
import time
import random
import pickle 
import pygame
world = []
worldadd = []
CITY_SIZE = 0
SHOP_SIZE = 0
houses = 1
population = 4
money = 5000
shops = 0
roads = 0
trees = 0
log = 3
print(log)
Xwat = []
Ywat = []
Xl=8
Yl=8
curl=("^")
X = 4
Y = 4
x = 0
c = 0
xfw = 0
yfw = 0
save = []
power = 0
powerneed = 0
polution = 0
POWER_SIZE = 0
Technology = 0.1
resersh_staitions = 0
deptscor = 1

            
#while x in range(0,(len(Xwat) - 1)):
#    print("hi")
time.sleep(1)
print(len(world))
print("WELCOME TO CITY.py!")
if input("Would you like to read the instructions!(y/n)? ") == "y":
    input("First you will see the world load up and the programme will ask you to chose one of the options (1,2,3,4,5 or 6) (press enter to move on)")
    input("then you can choose if you want to build a house, shop, road, plant a tree, demolish or exit the menu (press enter to move on) ")
    input("If you exit the menu you will be able to move the cursor.(press enter to move on)")
    input("and change how far you want to move it in the length option! (press enter to move on)")
    input("The cursor is represented by brakets , '( )', . To move the cursor enter the direction up, down, left or right (press enter to move on)")
    input("Building costs in-game money however you will get tax income if you have the right ratio of houses to everything else. (press enter to move on)")
    input("(you can also only build on a blank space) (press enter to move on) ")
    input("The ratios are 5+ houses to 1 shop, 2+ houses to one road and 0.75+ houses to planted trees! You also get income from houses. (press enter to move on)")
    input("Income is recieved at the end of each go. (press enter to move on)")
    input("this is the key for the map: ' 'blank space,'|'natral tree,'t' planted tree,'^' house, 's'shop, 'r'road.(press enter to move on)")
    
#load
if input("Would you like to load a save(y/n)? ") == "y":
    #https://stackoverflow.com/questions/27745500/how-to-save-a-list-to-a-file-and-read-it-as-a-list-type
    name = input("filename:")
    with open('saves/' + name, "rb") as fp:   # Unpickling
        save = pickle.load(fp)
    if(len(save)<17):
        print("Testing unknown file file, may fail!")
        ver = save[0]
        world = save [0]
        CITY_SIZE = save[1]
        SHOP_SIZE = save[2]
        houses = save[3]
        population = save[4]
        money = save[5]
        shops = save[6]
        roads = save[7]
        trees = save[8]
        Xl = save[9]
        Yl = save[10]
        curl = save[11]
        X = save[12]
        Y = save[13]
        x = save[14]
        c = save[15]
        hight = 32
        width = 22
        if input("Do you want to inject water. this wont damage develipment.(y/n)") == "y":
            print("injecting water")
            #injecting water
            A= random.randint(2,6)
            x = 0
            for x in range(0,A):
                Xwat.append(random.randint(0,18))
                Ywat.append(random.randint(0,28))
            x = 0
            print (len(Xwat))
            for x in range (0,len(Xwat)):
                xfw = Xwat[x]
                yfw = Ywat[x]
                A = random.randint(10,40)
                c = 0
                for c in range(0,A):
                    B = random.randint(0,3)
                    if (B == 0):
                        if (xfw < 21):
                            # TODO: write code...
                            xfw = xfw + 1
                    if (B == 1):
                        if (xfw > 1):
                            xfw = xfw - 1
                    if (B == 2):
                        if (yfw < 35):
                            yfw = yfw + 1
                    if (B == 3):
                        if (yfw > 1):
                            yfw = yfw - 1
                    #replace square
                    #remove curesser
                    if(world[yfw][xfw] == " " or world[yfw][xfw] == "|"):
                        worldadd = world[yfw]
                        varforw = worldadd[xfw]
                        worldaddd=[]
                        worldadddd = []
                        c = 0
                        for c in range(0,32):
                            if (c == xfw):
                                worldaddd.append("~")
                            else: 
                                worldaddd.append(worldadd[c])
                        x = 0
                        for x in range (0,22):
                            if (x == yfw):
                                  worldadddd.append(worldaddd)
                            else:
                                
                                worldadddd.append(world[x])
                    world = worldadddd
          
    else:

        print("checking version will be ported to current")
        if(save[16] == 2.1):
            print("old. all fine.")
            ver = save[0]
            world = save [0]
            CITY_SIZE = save[1]
            SHOP_SIZE = save[2]
            houses = save[3]
            population = save[4]
            money = save[5]
            shops = save[6]
            roads = save[7]
            trees = save[8]
            Xl = save[9]
            Yl = save[10]
            curl = save[11]
            X = save[12]
            Y = save[13]
            x = save[14]
            c = save[15]
            logs = save[17]
            hight = 32
            width = 22
        elif(save[16] == 2.2):
            print("old. all fine.")
            ver = save[0]
            world = save [0]
            CITY_SIZE = save[1]
            SHOP_SIZE = save[2]
            houses = save[3]
            population = save[4]
            money = save[5]
            shops = save[6]
            roads = save[7]
            trees = save[8]
            Xl = save[9]
            Yl = save[10]
            curl = save[11]
            X = save[12]
            Y = save[13]
            x = save[14]
            c = save[15]
            logs = save[17]
            power = save[18]
            hight = 32
            width = 22
        elif(save[16] == 2.3):
            print("old. all fine")
            ver = save[0]
            world = save [0]
            CITY_SIZE = save[1]
            SHOP_SIZE = save[2]
            houses = save[3]
            population = save[4]
            money = save[5]
            shops = save[6]
            roads = save[7]
            trees = save[8]
            Xl = save[9]
            Yl = save[10]
            curl = save[11]
            X = save[12]
            Y = save[13]
            x = save[14]
            c = save[15]
            logs = save[17]
            power = save[18]
            POWER_SIZE = save[19]
            Technology = save[20]
            resersh_staitions = save[21]
            hight = 32
            width = 22
        elif(save[16] == 2.4):
            print("old. all fine")
            ver = save[0]
            world = save [0]
            CITY_SIZE = save[1]
            SHOP_SIZE = save[2]
            houses = save[3]
            population = save[4]
            money = save[5]
            shops = save[6]
            roads = save[7]
            trees = save[8]
            Xl = save[9]
            Yl = save[10]
            curl = save[11]
            X = save[12]
            Y = save[13]
            x = save[14]
            c = save[15]
            logs = save[17]
            power = save[18]
            POWER_SIZE = save[19]
            Technology = save[20]
            resersh_staitions = save[21]
            hight = save[22]
            width = save[23]
        elif(save[16] == 2.5):
            print("YAY NEW!")
            ver = save[0]
            world = save [0]
            CITY_SIZE = save[1]
            SHOP_SIZE = save[2]
            houses = save[3]
            population = save[4]
            money = save[5]
            shops = save[6]
            roads = save[7]
            trees = save[8]
            Xl = save[9]
            Yl = save[10]
            curl = save[11]
            X = save[12]
            Y = save[13]
            x = save[14]
            c = save[15]
            logs = save[17]
            power = save[18]
            POWER_SIZE = save[19]
            Technology = save[20]
            resersh_staitions = save[21]
            hight = save[22]
            width = save[23]
            deptscor = save[24]
        else:
            print("FILE UNSUPPORTED! NOW QUITING!")
            
else:
    #generaits world
    width = int(input("width:"))
    hight = int(input("hight:"))
    world = []
    #creating world
    for x in range (0,hight):
        for c in range(0,width):
            A = random.randint(0,1)
            if (A == 1):
                worldadd.append(" ")
            else:
                B = random.randint(0,width)
                if (B == 1):
                    worldadd.append("~")
                    Xwat.append(len(worldadd) - 1)
                    Ywat.append(len(world))
                else:
                    worldadd.append("|")
                
        world.append(worldadd)
        worldadd = []
    #spreading water
    x = 0
    print (len(Xwat))
    for x in range (0,len(Xwat)):
        xfw = Xwat[x]
        yfw = Ywat[x]
        A = random.randint(10,40)
        c = 0
        for c in range(0,A):
            B = random.randint(0,3)
            if (B == 0):
                if (xfw < 49):
                    # TODO: write code...
                    xfw = xfw + 1
            if (B == 1):
                if (xfw > 1):
                    xfw = xfw - 1
            if (B == 2):
                if (yfw < 21):
                    yfw = yfw + 1
            if (B == 3):
                if (yfw > 1):
                    yfw = yfw - 1
            #replace square
            #remove curesser
            worldadd = world[yfw]
            varforw = worldadd[xfw]
            worldaddd=[]
            worldadddd = []
            c = 0
            for c in range(0,width):
                if (c == xfw):
                    worldaddd.append("~")
                else:
                    worldaddd.append(worldadd[c])
            x = 0
            for x in range (0,hight):
                if (x == yfw):
                    worldadddd.append(worldaddd)
                else:
 
                    worldadddd.append(world[x])
            world = worldadddd
        
        
#makes it lopp infinitaly
while (1 == 1):
    
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("You have " + str(money) + " and " + str(log) + " logs and you technoligy score is " + str(Technology))
    
             
    #acheivments!
    #house counter    
    if (houses == 6)and(CITY_SIZE == 0):
        print("CITY SIZE: LODGE - You have built 5 houses, have !500!")
        money = money + int(500)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 11)and(CITY_SIZE == 1):
        print("CITY SIZE: VILLAGE - You have built 10 houses, have !1,000!")
        money = money + int(1000)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 51)and(CITY_SIZE == 2):
        print("CITY SIZE: TOWN - You have built 50 houses, have !2,500!")
        money = money + int(5000)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 101)and(CITY_SIZE == 3):
        print("CITY SIZE: CITY - You have built 100 houses, have !10,000!")
        money = money + int(10000)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 301)and(CITY_SIZE == 4):
        print("CITY SIZE: CITY - You have built 300 houses, have !30,000!")
        money = money + int(30000)
        CITY_SIZE = CITY_SIZE + 1
    #shop counter
    if (shops == 1)and(SHOP_SIZE == 0):
        print("SHOPS SIZE: CORNER SHOP - You have built 1 shop, have !500!")
        money = money + int(500)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 3)and(SHOP_SIZE == 1):
        print("SHOP SIZE: MINI-MARKET - You have built 3 shops, have !1,000!")
        money = money + int(1000)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 10)and(SHOP_SIZE == 2):
        print("SHOP SIZE: SUPER-MARKET - You have built 11 shops, have !2,500!")
        money = money + int(5000)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 21)and(SHOP_SIZE == 3):
        print("SHOP SIZE: CITY MARKET - You have built 21 shops, have !10,000!")
        money = money + int(10000)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 61)and(SHOP_SIZE == 4):
        print("SHOP SIZE: INTERNATIONAL MARKET - You have built 61 shops, have !30,000!")
        money = money + int(30000)
        SHOP_SIZE = SHOP_SIZE + 1
    #power counter    
    if (power == 3000)and(POWER_SIZE == 0):
        print("POWER SUPPLY: WHISTLING - You have 3 KW, have !500!")
        money = money + int(500)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 3)and(POWER_SIZE == 1):
        print("POWER SUPPLY: BREZZE - You have 6 KW, have !1,000!")
        money = money + int(1000)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 10)and(POWER_SIZE == 2):
        print("POWER SUPPLY: SOLAR WIND - You have 12 KW, have !2,500!")
        money = money + int(5000)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 20)and(POWER_SIZE == 3):
        print("POWER SUPPLY: CENTRAL STATION - You have 20 KW , have !10,000!")
        money = money + int(10000)
        POWER_SIZE = POWER_SIZE + 1
    if (shops == 60)and(POWER_SIZE == 4):
        print("POWER SUPPLY: INTERNATIONAL STATION - You have 50 KW , have !30,000!")
        money = money + int(30000)
        POWER_SIZE = POWER_SIZE + 1
    #tree counter
    if (power == 3000)and(POWER_SIZE == 0):
        print("POWER SUPPLY: WHISTLING - You have 3 KW, have !500!")
        money = money + int(500)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 3)and(POWER_SIZE == 1):
        print("POWER SUPPLY: BREZZE - You have 6 KW, have !1,000!")
        money = money + int(1000)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 10)and(POWER_SIZE == 2):
        print("POWER SUPPLY: SOLAR WIND - You have 12 KW, have !2,500!")
        money = money + int(5000)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 20)and(POWER_SIZE == 3):
        print("POWER SUPPLY: CENTRAL STATION - You have 20 KW , have !10,000!")
        money = money + int(10000)
        POWER_SIZE = POWER_SIZE + 1
    if (shops == 60)and(POWER_SIZE == 4):
        print("POWER SUPPLY: INTERNATIONAL STATION - You have 50 KW , have !30,000!")
        money = money + int(30000)
        POWER_SIZE = POWER_SIZE + 1
    #income
    income = 50 * houses
    income = income +(population*10)
    powerneed = 200 * houses
    powerneed = powerneed + population * 100
    powerneed = powerneed + resersh_staitions * 2000
    powerneed = powerneed + (powerneed*(Technology/2))
    Technology = Technology + (0.005*resersh_staitions)
    if shops>0:
        # TODO: write code...
        if (houses/shops>4.999):
            income = income + (120*shops)
            powerneed = powerneed + shops * 600
    if roads>0:
        if ((houses + shops)/roads>1.999):
            income = income + (40*roads)
            powerneed = powerneed + 10*roads
    if trees> 0:
        if (trees/houses>0.74999):
            income = income + (30*trees)
    
    
    if not(powerneed < (power * Technology)):
        print("more power")
        income = income/10 
    print("Your income is !" + str(income))
    money = money + income
    print("power:" + str(power * Technology))
    print("power nedded:" + str(powerneed))

    if(money < 0):
        deptscor = deptscor + (deptscor/7)
        print("YOU IN DEPT Interst:" + str(money/6000*deptscor) + "% and you deptscor is " + str(deptscor) + "If you dont get into positives before dept score is higher than 3.728..." )
        money = money - (money/100*(money/1000*deptscor))
        if(deptscor >= 3.728330206437307):
            while(1==1):
                print("GAME END YOU GOT TO FAR INTO DEPT")
    else:
        deptscor = 1
    #remove curesser
    worldadd = world[Yl]
    cur = worldadd[Xl]
    worldaddd=[]
    worldadddd = []
    c = 0
    print("cur:" + str(cur))
    for c in range(0,width):
        if (c == Xl):
            worldaddd.append(curl)
        else:
            worldaddd.append(worldadd[c])
    x = 0
    for x in range (0,hight):
        if (x == Yl):
            worldadddd.append(worldaddd)
        else:

            worldadddd.append(world[x])
    world = worldadddd   
    
    #add curesser
    worldadd = world[Y]
    cur = worldadd[X]
    worldaddd=[]
    worldadddd = []
    curl=cur
    c = 0
    for c in range(0,width):
        if (c == X):
            worldaddd.append("O")# + cur + ")")
        else:
            worldaddd.append(worldadd[c])
    x = 0
    for x in range (0,hight):
        if (x == Y):
            worldadddd.append(worldaddd)
        else:

            worldadddd.append(world[x])
    world = worldadddd
    #save where cureser is to remove
    Xl = X
    Yl = Y
    
    #prints out the world
    px = 0
    py = 0
    for py in range(0,hight):
        for px in range(0,width):
            if (world[py][px] == " "):
                print("-",end='')
            else:
             print (world[py][px], end='')
        print("")
    print(X)
    print(Y)
    #givves opptions
    bs = input("0:exit menu 1:place house(!5000 and 1 log) 2:place shop(!5000) 3:place road(!1000) 4:plant tree(!50) 5:remove + 2 log per tree(!2000) 7:Brige(!1000 and 2 logs) 8:windmill small(!2000 and 2 logs) 9:windmill large(!10000 and 5 logs) 10:Build reserch staition(!10000 and 4 logs) 11:skip movement 12:save | Enter your choice:")
    if not(bs == "11"):
        if (bs == "1"):
            if cur == (" "):
                # TODO: write code...
                money = money - 5000
                population = population + 4
                houses = houses + 1
                log = log - 1
                print("You have built a house")
                print("Your population has grown by 4, have spent !5000 and 1 log and now have:")
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
                curl = ("^")
            else:
                print("You need to clear that land first!")
            
        if (bs == "2"):
            if cur == (" "):
                money = money - 5000
                population = population + (population / 100 * 20)
                shops = shops + 1
                print("You have built a shop")
                print("Your population has grown by 20%, have spent !5000 and now have:")
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
                curl = ("s")
            else:
                print("You need to clear that land first!")
        if (bs == "3"):
            if cur == (" "):
                money = money - 1000
                population = population + (population / 100 * 15)
                roads = roads + 1
                print("You have built a road")
                print("Your population has grown by 15%, have spent !1000 and now have:")
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
                curl = ("r")
            else:
                print("You need to clear that land first!")
        if (bs == "4"):
            if cur == (" "):
                trees = trees + 1
                money = money - 50
                population = population + (population / 100 * 2)
                print("You have planted a tree")
                print("Your population has grown by 2%, have spent !50 and now have:")
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
                curl = ("t")
            else:
                print("You need to clear that land first!")
        if (bs == "5"):
            if(cur == "~"):
                print("You can't clear water like that!!")
            else:
                print("You have destroyed a place")
                print("You now have:")
                if cur == "^":
                    houses = houses - 1
                    population = population - 4
                if cur == "s":
                    shops = shops - 1
                    population = population/6*5
                if cur == "r":
                    roads = roads - 1
                    population/115*100
                if cur == "t":
                    trees = trees - 1
                    log = log + 2
                    population = population/102*100
                if cur == "|":
                    log = log + 2
                if cur == "x":
                    power = power-3000
                    population = population-3
                if cur == "X":
                    power = power-15000
                    population = population-6
                money = money - 2000
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
    
                curl = (" ")
        if (bs == "12"):
            name = input("filename:")
            save = []
            save.append(world)
            save.append(CITY_SIZE)
            save.append(SHOP_SIZE)
            save.append(houses)
            save.append(population)
            save.append(money)
            save.append(shops)
            save.append(roads)
            save.append(trees)
            save.append(Xl)
            save.append(Yl)
            save.append(curl)
            save.append(X)
            save.append(Y)
            save.append(x)
            save.append(c)
            save.append(2.5)
            save.append(log)
            save.append(power)
            save.append(POWER_SIZE)
            save.append(Technology)
            save.append(hight)
            save.append(width)
            save.append(deptscor)
            with open('saves/' + name, "wb") as fp:   #Pickling
                pickle.dump(save, fp)
            print ("saved as '" + name + "' succsefly")
            if input("do you want to exit(y/n):") == "y":
                exit()
        if (bs == "7"):
            if cur == (" "):
                money = money - 1000                    
                log = log - 2
                population = population + (population / 100 * 2)
                print("You have built a bridge")
                print("Your population has grown by 2%,you have spent !1000 and 2 logs and now have:")
                print("- !" + str(money))                    
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")                    
                curl = (" ")
            else:
                print("That's not water!")
        if (bs == "8"):
            if cur == (" "):
                # TODO: write code...
                money = money - 2000
                population = population + 3
                log = log - 2
                power = power +30000
                print("You have built a small windmill")
                print("Your population has grown by 3, have spent !2000 and 2 logs and now have:")
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
                print("- " + str(power * Technology) + "w Power")
                curl = ("x")            
            else:
               print("You need to clear that land first!")
        if (bs == "9"):
            if cur == (" "):
                # TODO: write code...
                money = money - 10000
                population = population + 6
                log = log - 5
                power = power +150000
                print("You have built a large windmill")
                print("Your population has grown by 6, have spent !10000 and 5 logs and now have:")
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
                print("- " + str(power * Technology) + "w Power")
                curl = ("X")            
            else:
               print("You need to clear that land first!")
        if (bs == "10"):
            if cur == (" "):
                # TODO: write code...
                money = money - 10000
                population = population + 6
                log = log - 4
                resersh_staitions = resersh_staitions + 1
                print("You have built a Reaserch Staition")
                print("Your population has grown by 6, have spent !10000 and 4 logs and now have:")
                print("- !" + str(money))
                print("- " + str(population) + " people")
                print("- " + str(houses) + " houses")
                curl = ("%")            
            else:
               print("You need to clear that land first!")
            
    if not(bs == 0):        
        dir = input ("direction: ")
        len  = int(input ("length: "))
        if (dir == "left" or dir == "l"):
             X = X - len
        if (dir == "right" or dir == "r"):
             X = X + len
        if (dir == "down" or dir == "d"):
             Y = Y + len
        if (dir == "up" or dir == "u"):
             Y = Y - len
