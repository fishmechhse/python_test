import pandas as pd
csv_files =['book_dataset_1_10.csv', 'book_dataset_11_20.csv', 'book_dataset_21_30.csv', 'book_dataset_31_40.csv']
df_csv_concat = pd.concat([pd.read_csv(file, delimiter=';') for file in csv_files], ignore_index=True)
df_csv_concat.to_csv('book_dataset.csv',sep=';')
