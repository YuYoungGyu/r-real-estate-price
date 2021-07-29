import pandas as pd
import glob

def pos_to_dict(df):
    df = df.groupby(['week']).sum()
    weekly_keyword = df.iloc[:,3]

    weekly_dic_all = {}
    for idx in weekly_keyword.index:
        dic = {}
        for keyword in weekly_keyword[idx]:
            if keyword not in dic.keys():
                dic[keyword] = 1
            else:
                dic[keyword] += 1
        weekly_dic_all[idx] = dic

    weekly_df_all = pd.DataFrame(weekly_dic_all)
    weekly_df_all = weekly_df_all.fillna(0)
    return weekly_df_all