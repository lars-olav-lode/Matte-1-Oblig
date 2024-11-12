import numpy as np
import matplotlib.pyplot as plt
import math as math

e = math.e         # Setter e lik eulerskonstant
R = 100 * 10 ** 3          # Verdien til resistansen i Ohm.
C = 100 * 10 ** (-6) # Kondensatorens verdi i farad
def realfunk(t):   # Funksjonen til den teoretiske kretsen
    return -10 * e ** -((1 / (R * C))*t) + 10     # Skriver inn funksjonen for spenningen av tiden
liste = []
for i in range(1,31, 2):
    liste.append(i)
for i in range(31,71, 4):
    liste.append(i)

liste2 = [0.154 , 1.313,  2.78,  3.59, 4.45, 5.40, 6.17,6.89, 7.23, 7.75, 7.99, 8.23, 8.47, 8.64, 8.81, 8.96, 9.15, 9.30, 9.41, 9.51, 9.57, 9.63, 9.67,9.71, 9.73 ]

plt.plot(liste, liste2, "r",label = "Måling")



t_verdier = np.linspace(0,70,10000)   # Velger at t-verdiene skal være mellom 0 og 80 sekund med 10000 skritt.
v_verdier = realfunk(t_verdier)      # Finner spenningen som funksjon av tiden

plt.plot(t_verdier, v_verdier, "--", label = "Teoretisk")       # Lager funksjonen
plt.xlabel("Tiden")                        # Setter navn på aksene og tittel
plt.ylabel("V/Spenning")
plt.title("Spenningen i en RC-krets")       


plt.grid()                                 # Viser grid
plt.legend()
plt.show()                                 # Viser alt
