import pandas as pd
import random


data_path = '/Users/soumya/Documents/Mannheim-Data-Science/Sem_4/MasterThesis/Data/'
demo = 'religion1' # 'race'  # 'religion2' # 'gender' #  # 'race'  # 'race' #'gender' # 'religion'
demo_1 = 'jews' # 'black_pos'  # 'muslims' # 'female' # 'black'  # 'jews' # 'black' #'female' # 'jews'

demo1_df_processed = pd.read_csv(data_path + demo + '/' + 'reddit_comments_' + demo + '_' + demo_1 + '_processed' + '.csv')

print(demo1_df_processed.shape)

targets = []
attributes = []


if demo == 'race':
    targets = []
    attributes = []
elif demo == 'gender':
    targets = []
    attributes = []
elif demo == 'religion1':
    targets = ['jew ', 'Jews', 'Jewish', 'Torah', 'Judaism', 'Semitic', 'Ashkenazi']
    with open(data_path + demo + '/' + demo + '_' + demo_1 + '.txt') as f:
        attributes = [line.split('\n')[0] for line in f]
    print(len(attributes))
elif demo == 'religion2':
    targets = []
    attributes = []
elif demo == 'orientation':
    targets = []
    attributes = []

data_list = []

for idx, row in demo1_df_processed.iterrows():
    row_dict = {}
    phrase_joined = ''
    sent = row['comments_processed']
    try:
        sent_list = sent.split(" ")
        targets_in_sent = [t.lower() for t in targets if t.lower() in sent_list]
        print(targets_in_sent)
        # if len(targets_in_sent) == 0:
        #     print(sent)
        for target in targets_in_sent:
            # print(target)
            # target = random.choice(targets_in_sent)
            target_index1, target_index2 = None, None
            target_index1 = sent_list.index(target.strip())
            # print(target_index1)
            print(sent_list.count(target))
            if sent_list.count(target) > 1:
                sent_list_2 = sent_list[target_index1 + 1:]
                target_index2 = sent_list_2.index(target.strip())
            print(target_index1, target_index2)
            # print('***')

            for target_index in [target_index1, target_index2]:

                if target_index is not None:
                    left_window, right_window = target_index-7, target_index+7+1

                    if left_window < 0:
                        left_window = 0
                    phrase_list = sent_list[left_window:right_window]
                    phrase_joined = ' '.join(phrase_list)

                    if any(attr.lower() in phrase_joined for attr in attributes):
                        row_dict['id'] = row['id']
                        row_dict['attribute_in_window'] = True
                        row_dict['comment'] = row['comments_processed']
                        row_dict['phrase'] = phrase_joined
                        data_list.append(row_dict)
                        break

        if not row_dict:
            row_dict['id'] = row['id']
            row_dict['attribute_in_window'] = False
            row_dict['comment'] = row['comments_processed']
            row_dict['phrase'] = phrase_joined
            data_list.append(row_dict)
            # print('false')

    except Exception as ex:
        pass


print(data_list)
data_df = pd.DataFrame(data_list)
print(data_df.shape)
data_df.to_csv(data_path + demo + '/' + 'reddit_comments_' + demo + '_' + demo_1 + '_processed_phrase' + '.csv', index=False)

