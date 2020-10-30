import pandas as pd
from sklearn.model_selection import train_test_split


def build_dataset_manual_annot(df, dest_path):
    f = open(dest_path, 'w')
    data = ''

    for idx, row in df.iterrows():
        comment = row['comments_processed']
        data += '<bos> ' + comment + '\n'

    f.write(data)


data_path = '/Users/soumya/Documents/Mannheim-Data-Science/Sem_4/MasterThesis/Data/'
demo = 'religion1' # 'religion2' # 'orientation' # 'race' # 'gender' #  # 'race'  # 'race' #'gender' # 'religion'
demo_1 = 'jews' # 'muslims' # 'lgbtq'
demo_2 = 'christians' # 'straight' # 'christians'
desti_path = data_path + 'bias_annotated/' + demo + '/'


df_train_1 = pd.read_csv(data_path + demo + '/' + 'reddit_comments_' + demo + '_' + demo_1 + '_processed_phrase_biased_trainset' + '.csv')
df_train_2 = pd.read_csv(data_path + demo + '/' + 'reddit_comments_' + demo + '_' + demo_2 + '_processed_phrase_biased_trainset' + '.csv')

df_train_1 = df_train_1[['comments_processed']]
df_train_2 = df_train_2[['comments_processed']]

df_train = pd.concat([df_train_1, df_train_2])
build_dataset_manual_annot(df_train, desti_path + demo + '_bias_manual_swapped_targets_train.txt')

print(df_train.shape)

df_test_1 = pd.read_csv(data_path + demo + '/' + 'reddit_comments_' + demo + '_' + demo_1 + '_processed_phrase_biased_testset' + '.csv')
df_test_2 = pd.read_csv(data_path + demo + '/' + 'reddit_comments_' + demo + '_' + demo_2 + '_processed_phrase_biased_testset' + '.csv')

df_test_1 = df_test_1[['comments_processed']]
df_test_2 = df_test_2[['comments_processed']]

df_test = pd.concat([df_test_1, df_test_2])

print(df_test.shape)

build_dataset_manual_annot(df_test, desti_path + demo + '_bias_manual_swapped_targets_test.txt')