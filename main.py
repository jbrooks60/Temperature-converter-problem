# Temperature converter problem

C = 30

#Subroutine to convert centigrade to fahrenheit
def CtoF(C):
  return (C * 1.8)+32

#Subroutine to convert centigrade to fahrenheit
F = CtoF(C)

def FtoC(F):
  return (F / 1.8) - 32

print(C,"degrees C is",F,"degrees F")