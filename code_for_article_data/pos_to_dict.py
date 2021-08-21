import pandas as pd
import glob

def weekly_pos_to_dict(df):
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

def monthly_pos_to_dict(df):
    week_col = df['week']

    month_col = []
    for w in week_col:
        month_col.append(w//4)
    df['month'] = month_col
    keyword_month = df
    monthly_pos = keyword_month.groupby('month')['pos'].sum()

    monthly_word_dict = {}

    for m in range(len(monthly_pos)):
        word_dict = {}
        for word in monthly_pos[m]:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        monthly_word_dict[m] = word_dict
    monthly_word_df = pd.DataFrame(monthly_word_dict)
    monthly_word_df = monthly_word_df.fillna(0)
    return monthly_word_df