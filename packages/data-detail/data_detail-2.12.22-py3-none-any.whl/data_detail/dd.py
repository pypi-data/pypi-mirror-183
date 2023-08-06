def data_detail(data, num_of_unique:int = 50, graph:bool = False, all_numerical_dtype = False):
    
    ''':data: input dataset name
        :num_of_unique: how many number of unique values in a column should be to consider it categorical :default = 50`
        
        [[[IMPLEMENTATION]]]
        >>> from data_detail.dd import datadetail
        >>> data_detail(data, num_of_unique)'''
    import pandas  
    data = pandas.DataFrame(data)
    print('SHAPE')
    print(data.shape)
    print('='*50)
    print('DATA INFO')
    print(data.info())
    print()
    print('='*50)
    print("DUPLICATE")
    print(f'Data has {data.duplicated().sum()} duplicate values')
    print('='*50)
    print()
    print('NULL VALUES')
    print(data.isnull().sum())
    print('='*50)
    print()
    print('Categorical/Numerical')
    cat = 0
    num = 0
    cont = []
    for i in data.columns:
        
        if data[i].nunique()<=num_of_unique:
            print(f'{i} => {data[i].nunique()} : Categorical')
            cat+=1
        else:
            print(f'{i} => {data[i].nunique()} : Continuous')
            cont.append(i)
            num+=1
    
    print(f'Total Categorical : {cat}')
    print(f'Total Numerical : {num}')
    print('='*50)
    
    if all_numerical_dtype == True:
        try:
            for i in cont:
                if data[i].skew()>=0.5:
                    print(f'Right Skewed : {data[i].skew()} : apply log_transform')
                elif data[i].skew()<=-0.5:
                    print(f'{i} => Left Skewed : {data[i].skew()} : apply exponential transform')
                elif data[i].skew()<0.5 or data[i].skew()>-0.5:
                    print(f'{i} => {data[i].skew()} : No need to transform')
        except TypeError:
            print('Please remove date column before processing!!!')