import greedy as g
import exhaustivo as e


print("Exhaustivo - Volumen")

e.EjecutaExhaustivo(True)

print("Greedy - Volumen")

g.EjecutaGreedy(True)

print("Exhaustivo - Peso")

e.EjecutaExhaustivo(False)

print("Greedy - Peso")

g.EjecutaGreedy(False)


