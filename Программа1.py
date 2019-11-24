import time
z = input("Что тебе надо? S = расстояние, T = время, U = скорость?")
if z=="U":
          S=int(input("расстояние"))
          T=int(input("время"))
          U=S/T
          print(U)
if z=="S":
          T=int(input("время"))
          U=int(input("скорость"))
          S=U*T
          print(S)
if z=="T":
          U=int(input("скорость"))
          S=int(input("расстояние"))
          T=S/U
          print(T)
    
