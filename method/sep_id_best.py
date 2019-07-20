if __name__ == "__main__":
    import pandas as pd
    import pathlib
    src = 'D:\Study\COPD\COPD_DATA\daycarelog_VitalSigns.csv'
    outputdir = pathlib.Path('D:\Study\COPD\COPD_DATA\olds_best')
    df = pd.read_csv(src,
                names=['index','id','cat_name','sub_name','opt_name','opt_type','opt_memo','date'],
                usecols=[1,3,6,7])
    table = pd.pivot_table(df,index=['id','date'],columns='sub_name',values = 'opt_memo')
    table.reset_index(inplace = True)
    for _id,data in table.groupby('id'):
        data.iloc[:,1:].to_csv(outputdir / f'{_id}.csv',index = False)