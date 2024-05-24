import pandas as pd
import ast

## This file turns hashtag data into case insensitive (ex. #hi and #HI)

files = ['~/Coding/buntain/hashtag_data/TMRC14_APAC_1.csv', '~/Coding/buntain/hashtag_data/TMRC14_APAC_2.csv', 
         '~/Coding/buntain/hashtag_data/TMRC15_APAC_3.csv', '~/Coding/buntain/hashtag_data/twitterrei_china_052020.csv',
         '~/Coding/buntain/hashtag_data/twitterrei_china_082019_1.csv', '~/Coding/buntain/hashtag_data/twitterrei_china_082019_2.csv',
         '~/Coding/buntain/hashtag_data/twitterrei_china_082019_3.csv', '~/Coding/buntain/hashtag_data/twitterrei_thailand_092020.csv']

for file in files:
    print(file)
    df = pd.read_csv(file)
    case_insensitive_dict = dict()
    current_dict = df.set_index('hashtag')['count'].to_dict()
    current_dict = {key: int(value) for key, value in current_dict.items()}
    # current_dict = {key: ast.literal_eval(value) for key, value in current_dict.items()}
    for key in current_dict.keys():
        lowercase_key = key.lower()
        if lowercase_key in case_insensitive_dict:
            case_insensitive_dict[lowercase_key] += current_dict[key]
        else:
            case_insensitive_dict[lowercase_key] = current_dict[key]
    case_insensitive_dict = dict(sorted(case_insensitive_dict.items(), key=lambda item: item[1], reverse=True))
    new_df = pd.DataFrame(case_insensitive_dict.items(), columns = ["hashtag", "count"])
    new_df.to_csv(file, index=False)
