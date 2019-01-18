import numpy as np

#One-hot enconding

pessoas = ['ana', 'paulo', 'julia']

def normalize(nome):

    array = np.zeros(len(pessoas))

    for i, pessoa in enumerate(pessoas):
        if pessoa == nome:
            array[i] = 1.0

    return array

for pessoa in pessoas:
    print (pessoa, ' => ', normalize (pessoa))

