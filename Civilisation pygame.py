print("  ____                                         ___      _     _______         ____    ")
print(" |        ||   |     |     ||   |        ||   |        | |       |      ||   |    |   |\   |   ")
print(" |        ||    |   | _    ||   |        ||   |___    |   |      |      ||   |    |   | \  |   ")
print(" |        ||     | | |-|   ||   |        ||       |   |___|      |      ||   |    |   |  \ |   ")
print(" |____    ||      | ^|-|^^ ||   |_____   ||    ___|   |   |      |      ||   |____|   |   \| alfa v2.5 INCREMENTING debt")
print("                                                                                                        by text game studios")
print("                                         Loading...          ")
import time
import random
import pickle
xlbuts = []
ylbuts = []
xubuts = []
yubuts = []
idbuts = []
schools = 0
edu= 0.5
achev = "hi"
def rectdr(x55,y55,width3,hight3,text):
    x96 = x55 * (width*zoom) +  (width*zoom)
    y96 = y55  * (hight*zoom)
    #print("x for rect = " + str(x96))
    #print("Y for rect = " + str(y96))
    
    width2 = width3 * (width*zoom)
    hight2 = hight3 * (hight*zoom)
    #print("width for rect = " + str(width2))
    #print("hight for rect = " + str(hight2))
    
    font = pygame.font.SysFont(None, round(hight2*1.75))
    screentext = font.render(text, True, green)
    
    gameDisplay.fill(red, rect=[x96,y96,round(width2),round(hight2)])
    gameDisplay.blit(screentext, [x96, y96])
def rectdf(x55,y55,width3,hight3, but):
    x96 = x55 * (width*zoom) +  (width*zoom)
    y96 = y55  * (hight*zoom)
    #print("x for rect = " + str(x96))
    #print("Y for rect = " + str(y96))
    
    width2 = width3 * (width*zoom)
    hight2 = hight3 * (hight*zoom)
    #print("width for rect = " + str(width2))
    #print("hight for rect = " + str(hight2))
    xlbuts.append(x96)
    ylbuts.append(y96)
    xubuts.append(x96 + width2)
    yubuts.append(y96 + hight2)
    idbuts.append(but)
def happy():
    xl=[]
    yl=[]
    for y in range(0,len(world)):
        for x in range(0,len(world[y])):
            if(world[y][x])=="^":
                #print(world[y][x])
                xl.append(x)
                yl.append(y)
    dislist =[]
    #print(xl)
    #print(yl)
    curh = []
    for hs in range(0,len(xl)):
        dislist.append(sum(curh))
        curh = []
        for x in range(-3,4):
            for y in range(-3,4):
                try:
                    #print("hello")
                    #print(str([x+xl[hs]])+ "," + str([y+yl[hs]]))
                    if(world[y+yl[hs]][x+xl[hs]] == '^'):
                        x2 = abs(x)
                        y2 = abs(y)
                        if x2>y2:
                            dis=x2
                        else:
                            dis=y2
                        if dis == 0:
                            scr = 0
                        elif dis == 1:
                            scr = 3
                        elif dis == 2:
                            scr = 2
                        elif dis == 3:
                            scr = 1
                        curh.append(scr)
                        #print(dis)
                        #print(str(x) + "," + str(y))
                except:
                    pass
    A =[[],[],[]]
    #print(len(dislist))
    sdislist = sorted(dislist)
    cur = 0
    for x in range(0,round(len(dislist)/3)):
        A[0].append(sdislist[cur])
        cur += 1
    for x in range(0,(round(len(dislist)/3))):
        A[1].append(sdislist[cur])
        cur += 1
    for x in range(0,int((round(len(dislist)/3)))+((len(dislist)-(round(len(dislist)/3))*3))):
        #print(cur)
        A[2].append(sdislist[cur])
        cur += 1
    #print(A)
    cur = 0
    b = []
    for x in range(0,len(A[0])):
        cur += A[0][x]

    b.append(cur/(len(A[0])+0.01))
    cur = 0
    for x in range(0,len(A[1])):
        cur += A[1][x]
    b.append(cur/len(A[1]))
    cur = 0
    for x in range(0,len(A[2])):
        cur += A[2][x]
    b.append(cur/len(A[2]))
    cur = 0
    #print(b)
    b[0] -= 1
    b[1] -= 2.66
    b[2] -= 7
    happyy = sum(b)
    #Shopas
    for hs in range(0,len(xl)):
        dislist.append(sum(curh))
        curh = []
        for x in range(-3,4):
            for y in range(-3,4):
                try:
                    #print("hello")
                    #print(str([x+xl[hs]])+ "," + str([y+yl[hs]]))
                    if(world[y+yl[hs]][x+xl[hs]] == 's'):
                        x2 = abs(x)
                        y2 = abs(y)
                        if x2>y2:
                            dis=x2
                        else:
                            dis=y2
                        if dis == 0:
                            scr = 0
                        elif dis == 1:
                            scr = 3
                        elif dis == 2:
                            scr = 2
                        elif dis == 3:
                            scr = 1
                        curh.append(scr)
                        #print(dis)
                        #print(str(x) + "," + str(y))
                except:
                    pass
    A =[[],[],[]]
    #print(len(dislist))
    sdislist = sorted(dislist)
    cur = 0
    for x in range(0,round(len(dislist)/3)):
        A[0].append(sdislist[cur])
        cur += 1
    for x in range(0,(round(len(dislist)/3))):
        A[1].append(sdislist[cur])
        cur += 1
    for x in range(0,int((round(len(dislist)/3)))+((len(dislist)-(round(len(dislist)/3))*3))):
        #print(cur)
        A[2].append(sdislist[cur])
        cur += 1
    #print(A)
    cur = 0
    b = []
    for x in range(0,len(A[0])):
        cur += A[0][x]

    b.append(cur/(len(A[0])+0.01))
    cur = 0
    for x in range(0,len(A[1])):
        cur += A[1][x]
    b.append(cur/len(A[1]))
    cur = 0
    for x in range(0,len(A[2])):
        cur += A[2][x]
    b.append(cur/len(A[2]))
    cur = 0
    #print(b)
    b[0] -= 0.33
    b[1] -= 2.66/3
    b[2] -= 7/3
    happyy += sum(b)
    return happyy
zoom = int(input("zoom:"))

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
Xl = 8
Yl = 8
curl = ("^")
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
debtscor = 1
income = 0
tecworld = []
nbt = r"/m/"

# while x in range(0,(len(Xwat) - 1)):
#    print("hi")
time.sleep(1)
print(len(world))
print("WELCOME TO CITY.py!")
if input("Would you like to read the instructions!(y/n)? ") == "y":
    input(
        "Enter your zoom number, this determines how many pixels are used by each square, It will look best if it's a multiple of 20 but any number can be used. (press enter to move on)")
    input(
        "Now you can set your hight and width of your world, don't make it too big so that you can see it on your screen. Try restarting the game until you find a size that fits your screen. (press enter to move on) ")
    input("Now you have decided your hight and width you can choose the name of your world, make this easy to remember because you'll need it every time you load your world. Remember, if you use the same name as before it will override you previous save using that name.(press enter to move on)")
    input("Now the world will load up and you will see a menu on the right. (press enter to move on)")
    input(
        "You break trees to get logs which you use to build! You can also buy logs for £1500! (press enter to move on)")
    input(
        "Now you can select your building and stlye and start making your civilisation. remember to destor tees and build briges so you can place your buildings. (press enter to move on)")
    input(
        "And remember don't get in debt! (press enter to move on)")
    input("It is handles by an advanced algorithm to makw it as true to life as possible. (press enter to move on) ")
    input("Enjoy! (press enter to play)")
# load
if input("Would you like to load a save(y/n)? ") == "y":
    # https://stackoverflow.com/questions/27745500/how-to-save-a-list-to-a-file-and-read-it-as-a-list-type
    name = input("filename:")
    with open('saves/' + name, "rb") as fp:  # Unpickling
        save = pickle.load(fp)
    if (len(save) < 17):
        print("Testing unknown file file, may fail!")
        ver = save[0]
        world = save[0]
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
            # injecting water
            A = random.randint(2, 6)
            x = 0
            for x in range(0, A):
                Xwat.append(random.randint(0, 18))
                Ywat.append(random.randint(0, 28))
            x = 0
            print(len(Xwat))
            for x in range(0, len(Xwat)):
                xfw = Xwat[x]
                yfw = Ywat[x]
                A = random.randint(10, 40)
                c = 0
                for c in range(0, A):
                    B = random.randint(0, 3)
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
                    # replace square
                    # remove curesser
                    if (world[yfw][xfw] == " " or world[yfw][xfw] == "|"):
                        worldadd = world[yfw]
                        varforw = worldadd[xfw]
                        worldaddd = []
                        worldadddd = []
                        c = 0
                        for c in range(0, 32):
                            if (c == xfw):
                                worldaddd.append("~")
                            else:
                                worldaddd.append(worldadd[c])
                        x = 0
                        for x in range(0, 22):
                            if (x == yfw):
                                worldadddd.append(worldaddd)
                            else:

                                worldadddd.append(world[x])
                    world = worldadddd

    else:

        print("checking version will be ported to current")
        if (save[16] == 2.1):
            print("old. all fine.")
            ver = save[0]
            world = save[0]
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
        elif (save[16] == 2.2):
            print("old. all fine.")
            ver = save[0]
            world = save[0]
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
        elif (save[16] == 2.3):
            print("old. all fine")
            ver = save[0]
            world = save[0]
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
        elif (save[16] == 2.4):
            print("old. all fine")
            ver = save[0]
            world = save[0]
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
        elif (save[16] == 2.5):
            print("Non compat!")
            ver = save[0]
            world = save[0]
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
            debtscor = save[24]
        elif (save[16] == 2.6):
            print("NEW!")
            ver = save[0]
            world = save[0]
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
            debtscor = save[24]
            tecworld = save[25]
        else:
            print("FILE UNSUPPORTED! NOW QUITING!")

else:
    # generaits world
    name = input("filename:")
    width = int(input("width:"))
    hight = int(input("hight:"))
    world = []
    # creating world
    for x in range(0, hight):
        tecworldadd = []
        for c in range(0, width):
            A = random.randint(0, 1)
            if (A == 1):
                worldadd.append(" ")
            else:
                B = random.randint(0, 50)
                if (B == 1):
                    worldadd.append("~")
                    Xwat.append(len(worldadd) - 1)
                    Ywat.append(len(world))
                else:
                    worldadd.append("|")
            tecworldadd.append("")

        world.append(worldadd)
        tecworld.append(tecworldadd)
        worldadd = []
    # spreading water
    x = 0
    print(len(Xwat))
    for x in range(0, len(Xwat)):
        xfw = Xwat[x]
        yfw = Ywat[x]
        A = random.randint(10, 40)
        c = 0
        for c in range(0, A):
            B = random.randint(0, 3)
            if (B == 0):
                if (xfw < width-1):
                    # TODO: write code...
                    xfw = xfw + 1
            if (B == 1):
                if (xfw > 1):
                    xfw = xfw - 1
            if (B == 2):
                if (yfw < hight-1):
                    yfw = yfw + 1
            if (B == 3):
                if (yfw > 1):
                    yfw = yfw - 1
            # replace square
            # remove curesser
            worldadd = world[yfw]
            varforw = worldadd[xfw]
            worldaddd = []
            worldadddd = []
            c = 0
            for c in range(0, width):
                if (c == xfw):
                    worldaddd.append("~")
                else:
                    worldaddd.append(worldadd[c])
            x = 0
            for x in range(0, hight):
                if (x == yfw):
                    worldadddd.append(worldaddd)
                else:

                    worldadddd.append(world[x])
            world = worldadddd
            world[4][4] = "^"
#pygame initilisation
import pygame
from math import floor
pygame.init()
green = (0,255,0)
yellow = (255,255,0)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((width * zoom * 2, hight * zoom))
rectdf(0.025,0.07,0.2,0.05,("bs",1))
rectdf(0.275,0.07,0.2,0.05,("bs",2))
rectdf(0.525,0.07,0.2,0.05,("bs",3))
rectdf(0.775,0.07,0.2,0.05,("bs",4))
rectdf(0.025,0.14,0.2,0.05,("bs",5))
rectdf(0.275,0.14,0.2,0.05,("bs",7))
rectdf(0.525,0.14,0.2,0.05,("bs",8))
rectdf(0.775,0.14,0.2,0.05,("bs",9))
rectdf(0.025,0.21,0.2,0.05,("bs",10))
rectdr(0.275,0.21,0.2,0.05,("bs",14))
rectdf(0.025,0.35,0.45,0.05,("trt",r"/R/"))
rectdf(0.025,0.42,0.4,0.05,("trt",r"/M/"))
rectdf(0.5,0.35,0.4,0.05,("trt",r"/I/"))
rectdf(0.5,0.42,0.4,0.05,("trt",r"/S/"))
nbs = 0
pygame.display.set_caption('City.py.2.5.3')
##    bs = input("0:exit menu 1:place house(£5000 and 1 log) 2:place shop(£5000) 3:place road(£1000) 4:plant tree(£50) 5:remove + 2 log per tree(£2000) 7:Brige(£1000 and 2 logs) 8:windmill small(£2000 and 2 logs) 9:windmill large(£10000 and 5 logs) 10:Build reserch staition(£10000 and 4 logs) 11:skip movement 12:save | Enter your choice:")
pygame.display.update()
# makes it lopp infinitaly
running = 1
pygl = time.time()
while 1 == 1:
    XQ = []
    YQ = []
    bsQ = []
    while pygl + 2 > time.time():
        for y2 in range(0, hight):
            for x2 in range(0, width):
                x = x2 * zoom
                y = y2 * zoom
                filly = (0,255,0)
                if ((world[y2][x2]) == "~"):
                    filly = (0,0,255)
                if ((world[y2][x2]) == "|"):
                    filly = (125,75,0)
                if ((world[y2][x2]) == "^"):
                    filly = (225,0,0)
                #if x2 in XQ:
                #    if (YQ[XQ.index(x2)] == y2) : 
                #        filly = (0,0,0)
                gameDisplay.fill(filly, rect=[x,y,zoom,zoom])
                if not tecworld[y2][x2] == "":
                    #print("not")
                    image = pygame.image.load(tecworld[y2][x2])
                    image = pygame.transform.scale(image,(zoom,zoom))
                    gameDisplay.blit(image,(x,y))
        rectdr(0.01,0.01,0.6,0.05,"£" + str(round(money)))
        rectdr(0.65,0.01,0.35,0.05,"£" + str(round(income)) + "/D")
        #nbs buttons
        rectdr(0.025,0.07,0.2,0.05,"HOME")
        rectdr(0.275,0.07,0.2,0.05,"SHOP")
        rectdr(0.525,0.07,0.2,0.05,"ROAD")
        rectdr(0.775,0.07,0.2,0.05,"TREE")
        rectdr(0.025,0.14,0.2,0.05,"DELE")
        rectdr(0.275,0.14,0.2,0.05,"BRIG")
        rectdr(0.525,0.14,0.2,0.05,"SWIN")
        rectdr(0.775,0.14,0.2,0.05,"LWIN")
        rectdr(0.025,0.21,0.2,0.05,"RECH")
        rectdr(0.275,0.21,0.2,0.05,"SCHL")
        rectdr(0.025,0.35,0.4,0.05,"Rustic")
        
        rectdr(0.025,0.42,0.4,0.05,"Modern")
        rectdr(0.5,0.35,0.4,0.05,"Industrial")
        rectdr(0.5,0.42,0.4,0.05,"Stately")
        rectdr(0.025,0.925,0.4625,0.05,("Tech:" + str(Technology)))
        rectdr(0.025,0.85,0.4625,0.05,("Log:" + str(log)))
        rectdr(0.5,0.85,0.4625,0.05,("debt:" + str(debtscor)))
        rectdr(0.025,0.775,0.4625,0.05,("Power:" + str(power)))
        rectdr(0.5,0.775,0.4625,0.05,("Need:" + str(powerneed)))
        rectdr(0.025,0.7,0.95,0.025,("Achev:" + str(achev)))
        rectdr(0.025,0.625,0.4625,0.05,("EDU:" + str(edu)))
        rectdr(0.5125,0.625,0.4625,0.05,("EDU:" + str(0.005 * schools) + "/d"))
        rectdr(0.5125,0.925,0.4625,0.05,("Tech:" + str((0.005 * resersh_staitions)) + "/d"))
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(event.button == 1):
                    if(event.pos[0] > (width * zoom)):
                        for wxe in range(0 , len(xlbuts)):
                            if(event.pos[0] > xlbuts[wxe]):
                                if(event.pos[0] < xubuts[wxe]):
                                    if(event.pos[1] > ylbuts[wxe]):
                                        if(event.pos[1] < yubuts[wxe]):
                                            print(idbuts[wxe])
                                            if(idbuts[wxe][0] == "bs"):
                                                nbs = idbuts[wxe][1]
                                                print(nbs) 
                                            if(idbuts[wxe][0] == "trt"):
                                                nbt = idbuts[wxe][1]
                                                
                    if(event.pos[0] < (width * zoom)):
                        nxq = floor(event.pos[0] / zoom)
                        nyq = floor(event.pos[1] / zoom)
                        XQ.append(nxq)
                        YQ.append(nyq)
                        bsQ.append(nbs)
                        if not world[int(event.pos[1] / zoom)][int(event.pos[0] / zoom)] == " ":
                            gameDisplay.fill((255,0,0), rect=[nxq*zoom,nyq*zoom,zoom,zoom])
                        else:
                            tecworld[int(event.pos[1] / zoom)][int(event.pos[0] / zoom)] = ("tex" + nbt + str(nbs) + ".png")
                        
        pygame.display.update()
        inputbs = 0
        #print(XQ)
        #print(YQ)
        #print(bsQ)
    pygl = time.time()
    #print(xlbuts)
    #print(ylbuts)
    #print(xubuts)
    #print(yubuts)
    #print(idbuts)
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("You have £" + str(money) + " and " + str(log) + " logs and you technoligy score is " + str(Technology))

    # acheivments!
    # house counter
    if (houses == 6) and (CITY_SIZE == 0):
        achev  = ("HOUSE SIZE: LODGE - You have built 5 houses, have £500!")
        money = money + int(500)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 11) and (CITY_SIZE == 1):
        achev  = ("HOUSE SIZE: VILLAGE - You have built 10 houses, have £1,000!")
        money = money + int(1000)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 51) and (CITY_SIZE == 2):
        achev  = ("HOUSE SIZE: TOWN - You have built 50 houses, have £2,500!")
        money = money + int(5000)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 101) and (CITY_SIZE == 3):
        achev  = ("HOUSE SIZE: CITY - You have built 100 houses, have £10,000!")
        money = money + int(10000)
        CITY_SIZE = CITY_SIZE + 1
    if (houses == 301) and (CITY_SIZE == 4):
        achev  = ("HOUSE SIZE: CITY - You have built 300 houses, have £30,000!")
        money = money + int(30000)
        CITY_SIZE = CITY_SIZE + 1
    # shop counter
    if (shops == 1) and (SHOP_SIZE == 0):
        achev = "SHOPS SIZE: CORNER SHOP - You have built 1 shop, have £500!"
        money = money + int(500)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 3) and (SHOP_SIZE == 1):
        achev = "SHOP SIZE: MINI-MARKET - You have built 3 shops, have £1,000!"
        money = money + int(1000)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 10) and (SHOP_SIZE == 2):
        achev = "SHOP SIZE: SUPER-MARKET - You have built 11 shops, have £2,500!"
        money = money + int(5000)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 21) and (SHOP_SIZE == 3):
        achev = "SHOP SIZE: CITY MARKET - You have built 21 shops, have £10,000!"
        money = money + int(10000)
        SHOP_SIZE = SHOP_SIZE + 1
    if (shops == 61) and (SHOP_SIZE == 4):
        achev = "SHOP SIZE: INTERNATIONAL MARKET - You have built 61 shops, have £30,000!"
        money = money + int(30000)
        SHOP_SIZE = SHOP_SIZE + 1
    # power counter
    if (power == 3000) and (POWER_SIZE == 0):
        achev  = ("POWER SUPPLY: WHISTLING - You have 3 KW, have £500!")
        money = money + int(500)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 3) and (POWER_SIZE == 1):
        achev  = ("POWER SUPPLY: BREZZE - You have 6 KW, have £1,000!")
        money = money + int(1000)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 10) and (POWER_SIZE == 2):
        achev  = ("POWER SUPPLY: SOLAR WIND - You have 12 KW, have £2,500!")
        money = money + int(5000)
        POWER_SIZE = POWER_SIZE + 1
    if (power == 20) and (POWER_SIZE == 3):
        achev  = ("POWER SUPPLY: CENTRAL STATION - You have 20 KW , have £10,000!")
        money = money + int(10000)
        POWER_SIZE = POWER_SIZE + 1
    if (shops == 60) and (POWER_SIZE == 4):
        achev  = ("POWER SUPPLY: INTERNATIONAL STATION - You have 50 KW , have £30,000!")
        money = money + int(30000)
        POWER_SIZE = POWER_SIZE + 1
    # tree counter
    # income
    if log < 0:
        money -= abs(log)*1500
        log = 0
    income = 50 * houses
    income = income + (population * 10)
    powerneed = 200 * houses
    powerneed = powerneed + population * 100
    powerneed = powerneed + resersh_staitions * 2000
    powerneed = powerneed + (powerneed * (Technology / 2))
    edu += 0.005 * schools
    Technology = Technology + (0.005 * resersh_staitions * edu)
    income = income + (120 * shops)
    powerneed = powerneed + shops * 600
    income = income + (40 * roads)
    powerneed = powerneed + 10 * roads
    income = income + (30 * trees)
    income -= 100 * schools
    if houses > 2:
        income = income/abs(happy()*7+(0.01))
    if not (powerneed < (power * Technology)):
        print("more power")
        income = income / 10
    
    
    
    
    
    print("Your income is £" + str(income))
    money = money + income
    print("power:" + str(power * Technology))
    print("power nedded:" + str(powerneed))

    if (money < 0):
        debtscor = debtscor + (debtscor / 7)
        print("YOU IN debt Interst:" + str(money / 6000 * debtscor) + "% and you debtscor is " + str(
            debtscor) + "If you dont get into positives before debt score is higher than 3.728...")
        money = money - (money / 100 * (money / 1000 * debtscor))
        if (debtscor >= 3.728330206437307):
            
            print("GAME END YOU GOT TO FAR INTO debt")
            gameDisplay.fill(red)
            rectdr(0,0,0.25,0.25,"debt")
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            quit()
    else:
        debtscor = 1
    """# remove curesser
    worldadd = world[Yl]
    cur = worldadd[Xl]
    worldaddd = []
    worldadddd = []
    c = 0
    print("cur:" + str(cur))
    for c in range(0, width):
        if (c == Xl):
            worldaddd.append(curl)
        else:
            worldaddd.append(worldadd[c])
    x = 0
    for x in range(0, hight):
        if (x == Yl):
            worldadddd.append(worldaddd)
        else:

            worldadddd.append(world[x])
    world = worldadddd


    # save where cureser is to remove
    Xl = X
    Yl = Y
    #set cun cur to curl
    curl =  world[Y][X]
    # prints out the world"""
    """px = 0
    py = 0
    for py in range(0, hight):
        for px in range(0, width):
            if (world[py][px] == " "):
                print("ʬ", end='')
            else:
                print(world[py][px], end='')
        print("")
    print(X)
    print(Y)"""
    if (1 == 1):
        if (1 == 1):
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
            save.append(2.6)
            save.append(log)
            save.append(power)
            save.append(POWER_SIZE)
            save.append(Technology)
            save.append(resersh_staitions)
            save.append(hight)
            save.append(width)
            save.append(debtscor)
            save.append(tecworld)
            with open('saves/' + name, "wb") as fp:  # Pickling
                pickle.dump(save, fp)
            print("saved as '" + name + "' succsefly with a lenghth of " + str(len(save)))
    # givves opptions
#    bs = input("0:exit menu 1:place house(£5000 and 1 log) 2:place shop(£5000) 3:place road(£1000) 4:plant tree(£50) 5:remove + 2 log per tree(£2000) 7:Brige(£1000 and 2 logs) 8:windmill small(£2000 and 2 logs) 9:windmill large(£10000 and 5 logs) 10:Build reserch staition(£10000 and 4 logs) 11:skip movement 12:save | Enter your choice:")
    for nud in range(0,len(XQ)):
        Xl = XQ[nud]
        Yl = YQ[nud]
        bs = str(bsQ[nud])
        cur = world[Yl][Xl]
        curl = world[Yl][Xl]
        if not (bs == "11"):
            if (bs == "1"):
                if cur == (" "):
                    # TODO: write code...
                    money = money - 5000
                    population = population + 4
                    houses = houses + 1
                    log = log - 1
                    print("You have built a house")
                    print("Your population has grown by 4, have spent £5000 and 1 log and now have:")
                    print("- £" + str(money))
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
                    print("Your population has grown by 20%, have spent £5000 and now have:")
                    print("- £" + str(money))
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
                    print("Your population has grown by 15%, have spent £1000 and now have:")
                    print("- £" + str(money))
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
                    print("Your population has grown by 2%, have spent £50 and now have:")
                    print("- £" + str(money))
                    print("- " + str(population) + " people")
                    print("- " + str(houses) + " houses")
                    curl = ("t")
                else:
                    print("You need to clear that land first!")
            if (bs == "5"):
                if (cur == "~"):
                    print("You can't clear water like that!!")
                else:
                    print("You have destroyed a place")
                    print("You now have:")
                    if cur == "^":
                        houses = houses - 1
                        population = population - 4
                    if cur == "s":
                        shops = shops - 1
                        population = population / 6 * 5
                    if cur == "r":
                        roads = roads - 1
                        population / 115 * 100
                    if cur == "t":
                        trees = trees - 1
                        log = log + 2
                        population = population / 102 * 100
                    if cur == "|":
                        log = log + 2
                    if cur == "x":
                        power = power - 3000
                        population = population - 3
                    if cur == "X":
                        power = power - 15000
                        population = population - 6
                        money = money - 2000
                    if cur == "%":
                        population = population - 6
                        resersh_staitions = resersh_staitions - 1
                        money = money - 2000
                    print("- £" + str(money))
                    print("- " + str(population) + " people")
                    print("- " + str(houses) + " houses")
                    
                    curl = (" ")
#            if input("do you want to exit(y/n):") == "y":
#                exit()
            if (bs == "7"):
                if cur == ("~"):
                    money = money - 1000
                    log = log - 2
                    population = population + (population / 100 * 2)
                    print("You have built a bridge")
                    print("Your population has grown by 2%,you have spent £1000 and 2 logs and now have:")
                    print("- £" + str(money))
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
                    power = power + 30000
                    print("You have built a small windmill")
                    print("Your population has grown by 3, have spent £2000 and 2 logs and now have:")
                    print("- £" + str(money))
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
                    power = power + 150000
                    print("You have built a large windmill")
                    print("Your population has grown by 6, have spent £10000 and 5 logs and now have:")
                    print("- £" + str(money))
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
                    print("Your population has grown by 6, have spent £10000 and 4 logs and now have:")
                    print("- £" + str(money))
                    print("- " + str(population) + " people")
                    print("- " + str(houses) + " houses")
                    curl = ("%")
                else:
                    print("You need to clear that land first!")
            if (bs == "14"):
                if cur == (" "):
                    # TODO: write code...
                    money = money - 100000
                    population = population + 6
                    log = log - 4
                    schools += 1
                    print("You have built a School")
                    print("Your population has grown by 6, have spent £10000 and 4 logs and now have:")
                    print("- £" + str(money))
                    print("- " + str(population) + " people")
                    print("- " + str(houses) + " houses")
                    curl = ("Y")
                else:
                    print("You need to clear that land first!")
            
        if not (bs == 0):
            """dir = input("direction: ")
            len = int(input("length: "))
            if (dir == "left" or dir == "l"):
            X = X - len
            if (dir == "right" or dir == "r"):
                X = X + len
            if (dir == "down" or dir == "d"):
                Y = Y + len
            if (dir == "up" or dir == "u"):
                Y = Y - len"""
        # remove curesser
        worldadd = world[Yl]
        cur = worldadd[Xl]
        worldaddd = []
        worldadddd = []
        c = 0
        print("cur:" + str(cur))
        for c in range(0, width):
            if (c == Xl):
                worldaddd.append(curl)
            else:
                worldaddd.append(worldadd[c])
        x = 0
        for x in range(0, hight):
            if (x == Yl):
                worldadddd.append(worldaddd)
            else:
                worldadddd.append(world[x])
        world = worldadddd
        
        
        # save where cureser is to remove
        Xl = X
        Yl = Y
        #set cun cur to curl
        curl =  world[Y][X]
        
#comment
