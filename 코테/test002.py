def solution(arrayA, arrayB):
    arrayA.sort()
    setA = []
    setA.append(arrayA[0])
    for i in range(1,len(arryA)):
        if(setA[len(setA)-1] < arrayA[i]):
            setA.append(arrayA[i])
    arrayB.sort()
    setB = []
    setB.append(arrayB[0])
    for i in range(1,len(arrayB)):
        if(setB[len(setB) - 1] < arrayB[i]):
            setB.append(arrayB[i])
    _sum = setA.copy()
    
    for num in setB:
        if((num in _sum) == False):
            _sum.append(num)
        
    _erase = setA.copy()
    for num in setB:
        if(num in _erase):
            del _erase[_erase.index(num)]
    _inter = []
    for num in setA:
        if(num in setB):
            _inter.append(num)
        return [len(setA),len(setB),len(_sum),len(_erase),len(_inter)]


