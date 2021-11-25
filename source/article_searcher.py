import pandas as pd
import glob

file_name = glob.glob('../article/headline_noun_keyword*')

keyword_df = []
for file in file_name:
    df = pd.read_pickle(file)
    keyword_df.append(df)

keyword_all = pd.concat(keyword_df, ignore_index = True)
keyword_df = keyword_all[keyword_all['week'] <= 807]

result_list = pd.Series([True for i in range(len(keyword_df))], index = [i for i in range(len(keyword_df))], name = 'result')
keyword_df = pd.concat([keyword_df, result_list], axis=1)

all_week = list(set(keyword_df['week']))
all_company = list(set(keyword_df['co']))

def return_pos_result(keyword):
    global keyword_df
    result_list = []
    for pos in keyword_df.loc[:,'pos']:
        pos = list(pos)
        if set(pos) >= set(keyword):
            result_list.append(True)
        else:
            result_list.append(False)
    keyword_df.loc[:,'result'] = result_list

def search_article(keyword, co, week):
    global keyword_df
    if co == 0:
        co = all_company
    if week == -1:
        week = all_week
        
    co_str= ' '
    if type(co) == list:
        co_str = f'(co in {co}) and '
    else:
        co_str = f'(co in "{co}") and '
    week_str = f'(week in {week}) and '
    return_pos_result(keyword)
    str_keyword = f'{co_str} {week_str} (result == True)'
    df = keyword_df.query(str_keyword)
    return df