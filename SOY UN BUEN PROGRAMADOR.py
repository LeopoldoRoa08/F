World1=["ab","c"]
Wordl2=["a","bc"]
def Unir(World1,Wordl2):
    cadena1="".join(World1)
    cadena2="".join(Wordl2)
    if cadena1==cadena2:
        return True
    else:
        return False
print(Unir(World1,Wordl2))

hours = [0,1,2,3,4]
target=2
contador=0

def evaluacion(hours,target,contador):
    contador=0
    for i in range(len(hours)):
        if i>=target:
            contador=+1
            print("El empleado",str(i+1),"trabajo",str(i+1),"horas y cumplio con el objetivo")
        else:
            print("El empleado",str(i+1),"trabajo",str(i+1),"horas y no cumplio con el objetivo")
    print("Hay",str(contador),"empleados que cumplieron el objetivo")
    return i 
print(evaluacion(hours,target,contador))



