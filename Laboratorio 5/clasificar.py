from cgi import test
import re
import random
import math

def separarAtributos():   
    poblacion = []
    with open('car.data') as archivo:
        for linea in archivo:
            Arr1 = []
            aux = 0
            for i in re.finditer(',', linea):
                Arr1.append(linea[aux:i.start()])
                ##print(i.start())
                aux = i.start()+1
            poblacion.append(Arr1)
    return poblacion
                 
                 
def separarListas(poblacion, entrenamiento):
    numeros = random.sample(range(0,len(poblacion)),len(poblacion))
    delNumeros =[]
    entrenamientoArr = []
    testArr=[]
    cantEntrenamiento = math.floor(len(poblacion)*(entrenamiento/100))
    i = 0

    for i in range(0, len(poblacion)):
        if(poblacion[numeros[i]][6] == 'vgood' and len(entrenamientoArr) < math.floor(cantEntrenamiento/2)):
            entrenamientoArr.append(poblacion[numeros[i]])
            delNumeros.append(i)

    for i in range(0, len(poblacion)):
        if(poblacion[numeros[i]][6] == 'good' and len(entrenamientoArr) < math.floor(cantEntrenamiento)):
            entrenamientoArr.append(poblacion[numeros[i]])
            delNumeros.append(i)
    
    for i in range(0, len(poblacion)):
        if(i not in delNumeros):
            testArr.append(poblacion[numeros[i]])
    
    return(entrenamientoArr,testArr)

def entrenamiento(entrenamientoArr, prueba):
    vgood = 0
    good = 0
    variables =[0,0,0,0,0,0]
    arreglo = [0,0,0,0,0,0,0,0,0,0,0,0]
    

    for i in entrenamientoArr:
        if(i[6] == "vgood"):
            vgood += 1
        if(i[6] == "good"):
            good += 1
        if(i[0] == prueba[0]):
            variables[0] += 1
        if(i[1] == prueba[1]):
            variables[1] += 1
        if(i[2] == prueba[2]):
            variables[2] += 1
        if(i[3] == prueba[3]):
            variables[3] += 1
        if(i[4] == prueba[4]):
            variables[4] += 1
        if(i[5] == prueba[5]):
            variables[5] += 1
        if(i[0] == prueba[0] and i[6] == "vgood"):
            arreglo[0] += 1
        if(i[1] == prueba[1] and i[6] == "vgood"):
            arreglo[1] += 1
        if(i[2] == prueba[2] and i[6] == "vgood"):
            arreglo[2] += 1
        if(i[3] == prueba[3] and i[6] == "vgood"):
            arreglo[3] += 1
        if(i[4] == prueba[4] and i[6] == "vgood"):
            arreglo[4] += 1
        if(i[5] == prueba[5] and i[6] == "vgood"):
            arreglo[5] += 1
        if(i[0] == prueba[0] and i[6] == "good"):
            arreglo[6] += 1
        if(i[1] == prueba[1] and i[6] == "good"):
            arreglo[7] += 1
        if(i[2] == prueba[2] and i[6] == "good"):
            arreglo[8] += 1
        if(i[3] == prueba[3] and i[6] == "good"):
            arreglo[9] += 1
        if(i[4] == prueba[4] and i[6] == "good"):
            arreglo[10] += 1
        if(i[5] == prueba[5] and i[6] == "good"):
            arreglo[11] += 1

    # print(arreglo)
    #print(variables)  
    vgoodMult = (vgood/len(entrenamientoArr))*(arreglo[0]/variables[0])*(arreglo[1]/variables[1])*(arreglo[2]/variables[2])*(arreglo[3]/variables[3])*(arreglo[4]/variables[4])*(arreglo[5]/variables[5])
    goodMult = (good/len(entrenamientoArr))*(arreglo[6]/variables[0])*(arreglo[7]/variables[1])*(arreglo[8]/variables[2])*(arreglo[9]/variables[3])*(arreglo[10]/variables[4])*(arreglo[11]/variables[5])
    
    if(vgoodMult > goodMult):
        return "vgood"
    else:
        return "good"


def main():
    poblacion = separarAtributos()
    entrenamientoArr, testArr = separarListas(poblacion,80)

    print(testArr[0])
    print(entrenamiento(entrenamientoArr, testArr[0]))
    
    correctas = 0
    for i in testArr:
        aux = entrenamiento(entrenamientoArr, i)
        if (aux == i[6]):
            correctas += 1

    print("El  porcentaje de error es de ->", (100 - correctas/len(testArr)*100))
        

main() 