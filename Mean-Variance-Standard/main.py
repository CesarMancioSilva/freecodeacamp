import numpy as np
def Calculate(listInput):
    if len(listInput) != 9:
        raise ValueError("List must contain nine numbers.")
    array = np.array(listInput)
    matriz = array.reshape(3,3)
    print(matriz)

    info={}
    info['mean'] = [np.mean(matriz,axis=0).tolist(),np.mean(matriz,axis=1).tolist(),float(np.mean(listInput))]
    info['variance']= [np.var(matriz,axis=0).tolist(),np.var(matriz,axis=1).tolist(),float(np.var(listInput))]
    info['standard deviation']= [np.std(matriz,axis=0).tolist(),np.std(matriz,axis=1).tolist(),float(np.std(listInput))]
    info['max']= [np.max(matriz,axis=0).tolist(),np.max(matriz,axis=1).tolist(),int(np.max(listInput))]
    info['min']= [np.min(matriz,axis=0).tolist(),np.min(matriz,axis=1).tolist(),int(np.min(listInput))]
    info['sum']= [np.sum(matriz,axis=0).tolist(),np.sum(matriz,axis=1).tolist(),int(np.sum(listInput))]
    

    print(info)

Calculate([ 0 ,1 ,2 ,3 ,4 ,5 ,6, 7 ,8])
# Calculate(list(map(int,input().split())))

#this is just a test