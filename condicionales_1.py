# input
cant_minutos=int(input("dijite la cant_minutos: "))

# processing
if cant_minutos<=3:
    print("el valor de la llamada es : 300 pesos")
    

else:
    valor_llamada=300+50*(cant_minutos-3)

#output
print ("el valor de la llamada es: "+str(valor_llamada))

