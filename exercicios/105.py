

def notas(*n, situacao=False):
    dic = {}
    soma = 0
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n) 
    for valor in n:
        soma += valor
    dic['media'] = soma/dic['total']
    if situacao == True:
        if dic['media'] == 10:
            dic['situacao'] = 'Excelente'
        elif 10 > dic['media'] >= 7:
            dic['situacao'] = 'Bom'
        elif 7 > dic['media'] >= 5:
            dic['situacao'] = 'Regular'
        else:
            dic['situacao'] = 'Ruim'
    return dic


x = notas(5.5, 7, 10, 6.5, 1,  situacao= True)
y = notas(5, 2, 8.5, 3.5, 4)
y2 = notas(5, 2, 8.5, 3.5, 4, situacao= True)

print(x)
print(y)
print(y2)