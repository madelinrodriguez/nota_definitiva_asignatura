print("---------------------------------------")
print("------VALOR DE LA NOTA DEFINITIVA------")
print("---------------------------------------")

#input

nc = int(input("Digite el valor de la nota cognitivo:"))
np = int(input("Digite el valor de la nota procedimental:"))
na = int(input("Digite el valor de la nota actitudinal:"))
au = int(input("Digite el valor de la nota autoevaluacion:"))
bi = int(input("Digite el valor de la nota bimestral:"))

# processing

nd = (0.3*nc) + (0.3*np) + (0.1*na) + ( 0.1*au) + (0.2*bi)

# output

print("----------------------------")
print("--------RESULTADOS----------")
print("----------------------------")

print("Resultados nota definitiva:" + str (nd))