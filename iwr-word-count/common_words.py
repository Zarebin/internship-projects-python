import pandas as pd
import glob
from hazm import *


def get_label_list(label_list_path):
    # Load Labels List
    df = pd.read_excel(label_list_path, engine='openpyxl', sheet_name=0)
    labels_list = []
    for i in range(len(df['ClassName'])):
        labels_list.append(df['ClassName'][i])
    return labels_list


def clean_text(text):
    word_tokens = word_tokenize(text)
    word_tokens = [w for w in word_tokens if len(w) > 1]
    return word_tokens


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def get_common_words_count(sentence):
    tokens = clean_text(sentence)
    return len(intersection(tokens, label_list))


sentence_list = []
excel_files = glob.glob('data/*.xlsx')
label_list = get_label_list("labels_list_V2_100.xlsx")

for file_path in excel_files:
    data = pd.read_excel(file_path, engine='openpyxl', header=None, sheet_name=0)
    sentence_list = data.iloc[:, 0]
    data[1] = list(map(get_common_words_count, sentence_list))
    file_name = file_path.split('/')[-1]
    data.to_excel(f'convert/{file_name}', index=False, header=False)
