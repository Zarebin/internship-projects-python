import pandas as pd
import glob
from hazm import word_tokenize


# Read the first column of an Excel file
# Return the list of values in a column
def read_excel(path, col_index=0, header=None):
    df = pd.read_excel(path, engine='openpyxl', header=header, sheet_name=0)
    return df.iloc[:, col_index].astype(str).values.tolist()


# Tokenize a sentence and return a list of words with len > 1
def clean_text(text):
    word_tokens = word_tokenize(text)
    return [w for w in word_tokens if len(w) > 1]


# Intersection of two Lists
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Tokenize the sentence and return the length of common words with label_list
def get_common_words_count(sentence):
    global label_list
    tokens = clean_text(sentence)
    return len(intersection(tokens, label_list))


if __name__ == "__main__":

    label_path = "labels_list_V2_100.xlsx"
    in_path = "input/"
    out_path = "output/"
    excel_list = []
    excel_files = glob.glob(f'{in_path}/*.xlsx')
    label_list = read_excel(label_path, col_index=1, header=0)

    for excel_path in excel_files:
        sentence_list = read_excel(excel_path)
        com_word_count_list = list(map(get_common_words_count, sentence_list))
        dataframe = pd.DataFrame({
                '0': sentence_list,
                '1': com_word_count_list
        })
        excel_list.append(dataframe)

    excel_merged = pd.concat(excel_list, ignore_index=True)
    excel_merged.to_excel(f'{out_path}/merge.xlsx', index=False, header=False)
