
def summ_poli():
    with open('poly.txt') as f:
        lines = f.readlines()
        poli_1 = lines[4]
        poli_3 = poli_1[:19] 
    with open('poly2.txt') as f:
        lines = f.readlines()
        poli_2 = lines[0]
    summ_poli = f'{poli_3}+{poli_2}'
    print(summ_poli)

summ_poli()