arabic = 1
english = 2


def hebrew_translator(name):
    alef = "א"
    bet = "ב"
    gimel = "ג"
    dalet = "ד"
    hey = "ה"
    vav = "ו"
    zain = "ז"
    het = "ח"
    yod = "י"
    kaf = "כ"
    lamed = "ל"
    meem = "מ"
    meem_sofit = "ם"
    noon = "נ"
    noon_sofit = "ן"
    samech = "ס"
    ayin = "ע"
    pe = "פ"
    tsade = "צ"
    tsade_sofit = "ץ"
    qof = "ק"
    resh = "ר"
    shin = "ש"
    seen = "ש"
    tav = "ת"
    fe = "פ"
    fe_sofit = "ף"
    khaf = "כ"
    khaf_sofit = "ך"
    tet = "ט"

    # -----------------------------arabic----------------------------------

    alef1 = "ا"
    alef_maksoora1 = "ى"
    alef_maksoora_ma3_hamze = "ئ"
    waw_ma3_hamze = "ؤ"
    ba1 = "ب"
    ta1 = "ت"
    tha1 = "ث"
    gim1 = "ج"
    haa1 = "ح"
    kha = "خ"
    dal1 = "د"
    thal1 = "ذ"
    ra1 = "ر"
    zen1 = "ز"
    seen1 = "س"
    shin1 = "ش"
    sad1 = "ص"
    dad1 = "ض"
    taa1 = "ط"
    thaa1 = "ظ"
    een1 = "ع"
    gheen1 = "غ"
    fa1 = "ف"
    kaf1 = "ك"
    qaf1 = "ق"
    lam1 = "ل"
    meem1 = "م"
    noon1 = "ن"
    ha1 = "ه"
    waw1 = "و"
    ya1 = "ي"
    taa_marboota = "ة"
    # ------------------------------english--------------------------------
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"
    h = "h"
    i = "i"
    j = 'j'
    k = 'k'
    l = "l"
    m = 'm'
    n = "n"
    o = 'o'
    p = 'p'
    q = 'q'
    r = "r"
    s = 's'
    t = "t"
    u = "u"
    v = "v"
    w = 'w'
    x = "x"
    y = 'y'
    n = "n"
    z = "z"

    # ---------------------------------------------------------

    name_original = " "

    name = name.lower()

    for letter in range(0, len(name)):
        if (letter < len(name) - 1):

            if (name[letter] == alef1):
                name_original += alef
            if (name[letter] == ba1):
                name_original += bet
            if (name[letter] == ta1):
                name_original += tav
            if (name[letter] == thal1):
                name_original += tav
            if (name[letter] == ha1):
                name_original += hey
            if (name[letter] == gim1):
                name_original += gimel
            if (name[letter] == alef_maksoora_ma3_hamze):
                name_original += alef
            if (name[letter] == waw_ma3_hamze):
                name_original += vav + alef

            if (name[letter] == dal1):
                name_original += dalet
            if (name[letter] == thal1):
                name_original += dalet
            if (name[letter] == ra1):
                name_original += resh

            if (name[letter] == shin1):
                name_original += shin
            if (name[letter] == lam1):
                name_original += lamed
            if (name[letter] == haa1):
                name_original += het
            if (name[letter] == alef_maksoora1):
                name_original += alef


            if (name[letter] == tha1):
                name_original += tet
            if (name[letter] == zen1):
                name_original += zain
            if (name[letter] == seen1):
                name_original += samech
            if (name[letter] == sad1):
                name_original += samech
            if (name[letter] == dad1):
                name_original += dalet
            if (name[letter] == thaa1):
                name_original += tet

            if (name[letter] == taa1):
                name_original += tet
            if (name[letter] == een1):
                name_original += ayin
            if (name[letter] == gheen1):
                name_original += gimel



            if (name[letter] == waw1):
                name_original += vav
            if (name[letter] == ya1):
                name_original += yod

            if (name[letter] == taa_marboota):
                name_original += hey

            if (name[letter] == kaf1 and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                name_original += qof
            if (name[letter] == kaf1 and name[letter + 1] == " "):
                name_original += qof
            if (name[letter] == kaf1 and name[letter + 1] == ","):
                name_original += qof

            if (name[letter] == qaf1 and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                name_original += qof
            if (name[letter] == qaf1 and name[letter + 1] == " "):
                name_original += qof
            if (name[letter] == qaf1 and name[letter + 1] == ","):
                name_original += qof

            if (name[letter] == kha and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                name_original += khaf
            if (name[letter] == kha and name[letter + 1] == " "):
                name_original += khaf_sofit
            if (name[letter] == kha and name[letter + 1] == ","):
                name_original += khaf_sofit

            if (name[letter] == fa1 and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                name_original += fe
            if (name[letter] == fa1 and name[letter + 1] == " "):
                name_original += fe_sofit
            if (name[letter] == fa1 and name[letter + 1] == ","):
                name_original += fe_sofit

            if (name[letter] == meem1 and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                name_original += meem
            if (name[letter] == meem1 and name[letter + 1] == " "):
                name_original += meem_sofit
            if (name[letter] == meem1 and name[letter + 1] == ","):
                name_original += meem_sofit

            if (name[letter] == noon1 and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                name_original += noon
            if (name[letter] == noon1 and name[letter + 1] == " "):
                name_original += noon_sofit
            if (name[letter] == noon1 and name[letter + 1] == ","):
                name_original += noon_sofit

            else:
    # *****************************english alphabets***************************************************

                if (name[letter] == a):
                    name_original += alef
                if (name[letter] == b):
                    name_original += bet
                if (name[letter] == c):
                    name_original += qof
                if (name[letter] == d):
                    name_original += dalet
                if (name[letter] == e):
                    name_original += yod

                if (name[letter] == g):
                    name_original += gimel
                if (name[letter] == h):
                    name_original += het

                if (name[letter] == i):
                    name_original += yod
                if (name[letter] == j):
                    name_original += gimel

                if (name[letter] == l):
                    name_original += lamed
                if (name[letter] == o):
                    name_original += vav
                if (name[letter] == q):
                    name_original += qof
                if (name[letter] == r):
                    name_original += resh
                if (name[letter] == s):
                    name_original += samech

                if (name[letter] == t):
                    name_original += tav
                if (name[letter] == u):
                    name_original += vav
                if (name[letter] == v):
                    name_original += vav
                if (name[letter] == w):
                    name_original += vav
                if (name[letter] == x):
                    name_original += alef + qof + samech
                if (name[letter] == y):
                    name_original += yod + vav

                if (name[letter] == z):
                    name_original += zain

                if (name[letter] == p and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                    name_original += fe_sofit
                if (name[letter] == p and name[letter + 1] == " "):
                    name_original += fe_sofit
                if (name[letter] == p and name[letter + 1] == ","):
                    name_original += fe_sofit

                if (name[letter] == k and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                    name_original += qof
                if (name[letter] == k and name[letter + 1] == " "):
                    name_original += qof

                if (name[letter] == k and name[letter + 1] == ","):
                    name_original += qof

                if (name[letter] == f and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                    name_original += fe
                if (name[letter] == f and name[letter + 1] == " "):
                    name_original += fe_sofit
                if (name[letter] == f and name[letter + 1] == ","):
                    name_original += fe_sofit

                if (name[letter] == m and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                    name_original += meem
                if (name[letter] == m and name[letter + 1] == " "):
                    name_original += meem_sofit
                if (name[letter] == m and name[letter + 1] == ","):
                    name_original += meem_sofit

                if (name[letter] == n and name[letter + 1] != " " and name[letter + 1] != ","):  # lal sofeeeeet
                    name_original += noon
                if (name[letter] == n and name[letter + 1] == " "):
                    name_original += noon_sofit
                if (name[letter] == n and name[letter + 1] == ","):
                    name_original += noon_sofit
                 #------------------------------------hebrew alphabets---------------------------------------------
                if (name[letter] == alef):
                    name_original += alef
                if (name[letter] == bet):
                    name_original += bet
                if(name[letter] == resh):
                    name_original+= resh
                if (name[letter] == gimel):
                    name_original += gimel
                if (name[letter] == dalet):
                    name_original += dalet
                if (name[letter] == hey):
                    name_original += hey
                if (name[letter] == vav):
                    name_original += vav
                if (name[letter] == zain):
                    name_original += zain
                if (name[letter] == het):
                    name_original += het

                if (name[letter] == tet):
                    name_original += tet
                if (name[letter] == qof):
                    name_original += qof
                if (name[letter] == kaf):
                    name_original += kaf

                if (name[letter] == lamed):
                    name_original += lamed
                if (name[letter] == meem):
                    name_original += meem
                if (name[letter] == noon):
                    name_original += noon
                if (name[letter] == noon_sofit):
                    name_original += noon_sofit

                if (name[letter] == khaf_sofit):
                    name_original += khaf_sofit
                if (name[letter] == samech):
                    name_original += samech
                if (name[letter] == shin):
                    name_original += shin
                if (name[letter] == tsade_sofit):
                    name_original += tsade_sofit
                if (name[letter] == tsade):
                    name_original += tsade
                if (name[letter] == meem_sofit):
                    name_original += meem_sofit

                if (name[letter] == fe_sofit):
                    name_original += fe_sofit
                if (name[letter] == fe):
                    name_original += fe
                if (name[letter] == ayin):
                    name_original += ayin

                if (name[letter] == yod):
                    name_original += yod



                if (name[letter] == ","):
                   name_original += "\n"



            name_original += " "

            if (name[letter] == " "):  # spacing the words
                name_original += " "
# ---------------------------------------------the last letter------------------------------------------------
        if (letter == len(name) - 1):
            if (name[letter] == alef1):
                name_original += alef
            if (name[letter] == ba1):
                name_original += bet
            if (name[letter] == ta1):
                name_original += tav
            if (name[letter] == thal1):
                name_original += tav
            if (name[letter] == ha1):
                name_original += hey
            if (name[letter] == gim1):
                name_original += gimel



            if (name[letter] == dal1):
                name_original += dalet
            if (name[letter] == thal1):
                name_original += dalet
            if (name[letter] == ra1):
                name_original += resh

            if (name[letter] == shin1):
                name_original += shin
            if (name[letter] == lam1):
                name_original += lamed
            if (name[letter] == haa1):
                name_original += het
            if (name[letter] == alef_maksoora1):
                name_original += alef

            if (name[letter] == alef_maksoora_ma3_hamze):
                name_original += alef
            if (name[letter] == waw_ma3_hamze):
                name_original += vav + alef

            if (name[letter] == tha1):
                name_original += dalet
            if (name[letter] == zen1):
                name_original += zain
            if (name[letter] == seen1):
                name_original += samech
            if (name[letter] == sad1):
                name_original += samech
            if (name[letter] == dad1):
                name_original += dalet
            if (name[letter] == thaa1):
                name_original += tet

            if (name[letter] == taa1):
                name_original += tet
            if (name[letter] == een1):
                name_original += ayin
            if (name[letter] == gheen1):
                name_original += gimel

            if (name[letter] == qaf1):
                name_original += khaf_sofit

            if (name[letter] == waw1):
                name_original += vav
            if (name[letter] == ya1):
                name_original += yod

            if (name[letter] == taa_marboota):
                name_original += hey

            if (name[letter] == fa1):
                name_original += fe_sofit

            if (name[letter] == meem1):
                name_original += meem_sofit
            if(name[letter]== kaf1):
                name_original+=khaf_sofit

            if (name[letter] == noon1):
                name_original += noon_sofit
            if (name[letter] == a):
                name_original += alef
            if (name[letter] == b):
                name_original += bet
            if (name[letter] == c):
                name_original += qof
            if (name[letter] == d):
                name_original += dalet
            if (name[letter] == e):
                name_original += yod

            if (name[letter] == g):
                name_original += gimel
            if (name[letter] == h):
                name_original += het

            if (name[letter] == i):
                name_original += yod
            if (name[letter] == j):
                name_original += gimel

            if (name[letter] == l):
                name_original += lamed
            if (name[letter] == o):
                name_original += vav
            if (name[letter] == q):
                name_original += qof
            if (name[letter] == r):
                name_original += resh
            if (name[letter] == s):
                name_original += samech
            if (name[letter] == t):
                name_original += tav
            if (name[letter] == u):
                name_original += vav
            if (name[letter] == v):
                name_original += vav
            if (name[letter] == w):
                name_original += vav
            if (name[letter] == x):
                name_original += alef + qof + samech
            if (name[letter] == y):
                name_original += yod + vav

            if (name[letter] == z):
                name_original += zain

            if (name[letter] == p):
                name_original += fe_sofit

            if (name[letter] == k):
                name_original += khaf_sofit

            if (name[letter] == f):
                name_original += fe_sofit

            if (name[letter] == m):
                name_original += meem_sofit

            if (name[letter] == n):
                name_original += noon_sofit

    return name_original

# test the app here(write the names in the list)
list = ''' '''

print(hebrew_translator(list))
