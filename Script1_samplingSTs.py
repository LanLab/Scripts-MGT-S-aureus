import pandas as pd
import random

def main():

    STs_in_df = open('/Users/liamcheneyy/Desktop/untitled folder/ST_sizes.csv').read().splitlines()

    df = pd.read_csv('/Users/liamcheneyy/Desktop/hasMLST.csv')

    save_list = []
    save_list.append(df.columns)
    for line in STs_in_df[1:]:
        col = line.split(',')
        ST = col[0]
        size = int(col[1])

        sub_df = df[df['MGT1'] == ST]
        if size > sub_df.shape[0]:
            print(ST, size, sub_df.shape[0])
            # save_list.append([ST, sub_df['ID'].tolist()])
            pass
        else:
            # print(ST, size, sub_df.shape)
            sample = sub_df.sample(n = size)
            save_list.append(sample.values[0])

    outDF = pd.DataFrame(save_list)
    outDF.to_csv('/Users/liamcheneyy/Desktop/genomes_STs.csv', header=False, index=False)

if __name__ == '__main__':
    main()
