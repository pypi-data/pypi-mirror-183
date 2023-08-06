def data_detail(data, num_of_unique = 50):
    
    ''':data: input dataset name
        :num_of_unique: how many number of unique values in a column should be to consider it categorical :default = 50`
        
        [[[IMPLEMENTATION]]]
        >>> from data_detail.dd import datadetail
        >>> data_detail(data, num_of_unique)'''
    
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
    for i in data.columns:
        
        if data[i].nunique()<=num_of_unique:
            print(f'{i} => {data[i].nunique()} : Categorical')
            cat+=1
        else:
            print(f'{i} => {data[i].nunique()} : Continuous')
            num+=1
    print(f'Total Categorical : {cat}')
    print(f'Total Numerical : {num}')