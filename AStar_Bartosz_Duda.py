import math

  # y   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19   # x
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0],  # 3
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],  # 5
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],  # 6
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],  # 7
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 5, 5, 5, 5, 5],  # 11
       [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],  # 12
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0],  # 13
       [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0],  # 14
       [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0],  # 15
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 0],  # 16
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0],  # 17
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 18
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 19

#Koordynaty początkowe:
stx = 0 #stx = x index || sty = y index
sty = 0
#Koordynaty końcowe:
finx = 19
finy = 19


def A_star(map, stx, sty, finx, finy):
    current = [stx, sty] #Obecny punkt
    finish = [finx, finy] #Koniec

    best_route = []
    best_route.append(current) #Dodanie pierwszego do trasy ostateczniej

    while current != finish:
        available_dirs = []
    #Deklarowanie kierunków które będą sprawdzane (np. n=północ)
        n = map[current[0] - 1][current[1]]                # Północ
        if n == 0:
            n = [current[0] - 1, current[1]]
            if not n in best_route:
                available_dirs.append(n)
        try:
            s = map[current[0] + 1][current[1]]            #Południe
            if s == 0:
                s = [current[0] + 1, current[1]]
                if not s in best_route:
                    available_dirs.append(s)
        except:
            pass
        w = map[current[0]][current[1] - 1]                #Zachód
        if w == 0:
            w = [current[0], current[1] - 1]
            if not w in best_route:
                available_dirs.append(w)

        e = map[current[0]][current[1] + 1]                #Wschód
        if e == 0:
            e = [current[0], current[1] + 1]
            if not e in best_route:
                available_dirs.append(e)

        heuristics = []

        for i in range(len(available_dirs) - 1, -1, -1):
            value = math.sqrt(((available_dirs[i][0] - finx) ** 2) + ((available_dirs[i][1] - finy) ** 2)) #Wzór na heurystykę
            heuristics.append(value)
        heuristics.reverse()

        lowHeuInd = heuristics.index(min(heuristics))  #Najmniejsza wartosc z obliczonych heurystyk
        nextBestStep = available_dirs[lowHeuInd]

        current = [nextBestStep[0], nextBestStep[1]]

        best_route.append(current)

        heuristics.clear()
        available_dirs.clear()

        if current == finish:
            print("Cyfra 5 - oznacza PRZESZKODE")
            print("Cyfra 0 - oznacza PUSTE POLE")
            print("Punkt (0,0) - oznacza START")
            print("Punkt (19,19) - oznacza KONIEC")
            print("Najlepsza droga:")
            print(best_route)




A_star(map, stx, sty, finx, finy)