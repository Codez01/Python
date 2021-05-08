import math


segment = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]  # thoom
HowManySplines = int(input("Choose 2 , 4 , 6 , 12 Splines.\n"))

xi = []
if HowManySplines == 2:
    xi = filter(lambda x: x % 6 == 0, segment)
    xi = list(xi)

if HowManySplines == 4:
    xi = filter(lambda x: x % 3 == 0, segment)
    xi = list(xi)

if HowManySplines == 6:
    xi = filter(lambda x: x % 2 == 0, segment)
    xi = list(xi)
if HowManySplines == 12:
    xi = segment
# ********************************************************************************************
yi = []
hi = []
ci = []
di = []
bi = []
ui = [0]
vi = [0]
splines = HowManySplines + 1
zi = [0] * splines


def yiFiller(list1: list):#yi filler
    for i in range(len(list1)):
        save = lambda x: (((math.sin(math.radians(x))) + (math.cos(math.radians(x)))) ** (1 / 3))
        yi.append(save(list1[i]))


def hiFiller(list1: list):#hi filler
    for i in range(HowManySplines, 0, -1):
        hi.append((list1[i]) - list1[i - 1])


def ciFiller(ylist: list, hlist: list, zlist):#ci filler
    for i in range(0, HowManySplines):
        save = lambda y, h, z: (y / h) - ((z * h) / 6)

        ci.append(save(ylist[i + 1], hlist[i], zlist[i + 1]))


def biFiller():# bi filler
    for i in range(0, HowManySplines):
        save = lambda h, y, z: (6 / h) * (y - z)
        bi.append(save(hi[i], yi[i + 1], yi[i]))

    ui.append(2 * (hi[0] + hi[1]))
    vi.append(bi[0] + bi[1])
    zi[0] = 0
    zi[HowManySplines - 1] = 0


def diroog():#function to fill U and V
    for i in range(2, HowManySplines):
        save = lambda h, y, z: 2 * (h + y) - ((y ** 2) / z)
        ui.append((save(hi[i], hi[i - 1], ui[i - 1])))
        save2 = lambda b, y, h, u, v: ((b - y) - (((h ** 2) / u) * v))
        vi.append(save2(bi[i], bi[i - 1], hi[i - 1], ui[i - 1], vi[i - 1]))


def ziFiller():# zi filler
    for i in range(HowManySplines - 1, 0, -1):
        save = lambda v, h, z, u: (v - (h * z)) / u

        zi[i] = save(vi[i], hi[i], zi[i + 1], ui[i])


def diFiller(ylist: list, hlist: list, zlist):#di filler
    for i in range(0, HowManySplines):
        save = lambda y, h, z: (y / h) - ((z * h) / 6)

        di.append(save(ylist[i], hlist[i], zlist[i]))


def splines():#prints the splines functions depending on how many splines you chose
    for i in range(0, HowManySplines):
        print("s{} = {}*(x-{})^3 + {}*(x - {}) + {}*({} - x )".format(i, zi[i + 1], xi[i], ci[i], xi[i], di[i],
                                                                       xi[i + 1]))



hiFiller(xi)
yiFiller(xi)
biFiller()
diroog()
ziFiller()
ciFiller(yi, hi, zi)
diFiller(yi, hi, zi)
splines()

