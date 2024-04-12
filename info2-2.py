

vlanNum = int(input("Introduzca el número de Vlan: "))
if vlanNum >= 1 and vlanNum <= 1005:
    print ("Esta es una Vlan de rango normal")
elif vlanNum >= 1006 and vlanNum <= 4095:
    print ("Esta es una Vlan de rango extendido")
else:
    print ("Número de Vlan ingresado desconocido")
