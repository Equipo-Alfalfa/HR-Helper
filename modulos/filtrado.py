import pandas as pd
import read_data as data

def filtrar():
    dfaux = data.read_data()
    while True:
        todas = dfaux.columns
        columnas_especificas = ['Age','MonthlyIncome','YearsAtCompany','Days worked','Gender']
        columnas = dict.fromkeys(range(len(todas)))
        y = iter(todas)
        for i in columnas:
            columnas[i] = next(y)
        print(columnas)
        i = int(input('Que columna quieres filtrar?: '))
        
        if dfaux[columnas[i]].dtypes == 'int64' or dfaux[columnas[i]].dtypes == 'float64':
            min, max = dfaux[columnas[i]].min() ,dfaux[columnas[i]].max()
            print(f'Minimo: {min}, Maximo: {max}')
            mi = int(input('Minimo: ')) 
            ma = int(input('Maximo: ')) 
            
            def accion(minimo= min, maximo= max, columna= columnas[i]):
                x = set([i if i >= minimo and i <= maximo else None for i in dfaux[columna].values])
                for i in dfaux.index:
                    if dfaux[columna][i] in x:
                        continue
                    dfaux.drop([i], axis= 0, inplace= True)
            accion(mi, ma)
            
        else:
            x = set([i for i in dfaux[columnas[i]].values])
            o = dict.fromkeys(range(len(x)))
            y = iter(x)
            for k in o:
                o[k] = next(y)
            print(o)
            u = int(input('Que caracteristica quieres filtrar?: '))
            for j in dfaux.index:
                    if dfaux[columnas[i]][j] == o[u]:
                        continue
                    dfaux.drop([j], axis= 0, inplace= True)
        if int(input('Quieres filtrar otra caracteristica? Si(1) No(0): ')) != 1:
            nombres = dfaux['Name'].values
            nombres.sort()
            dic = {}
            for i in nombres:
                x = i.split()
                if x[0][0]+x[1][0] in dic:
                    dic[x[0][0]+x[1][0]].append(i)
                else:
                    dic[x[0][0]+x[1][0]] = [i]
            print(dic)
            return pd.DataFrame(dic)


