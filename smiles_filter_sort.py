import csv
import pandas as pd
import pubchempy as pcp

df1 = pd.read_csv('File1.csv')
df2 = pd.read_csv('File2.csv')

df3 = pd.merge(df2,df1,how = 'left')

df3.to_csv("File3.csv")

with open ("File4.csv", mode = 'a') as g:
    with open ("File3.csv") as f:
        reader = csv.reader(f)
        header = next(reader)
        g.write('SMILES' + ',' + 'num' + ',' + 'drug' + ',' + 'codes' + '\n')
        for row in reader:
            n = row[4].strip('CID')
            c = pcp.Compound.from_cid(n)
            l = c.synonyms
            x = 0
            g.write(row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4])
            if len(l) == 0:
                g.write('\n')
                continue
            elif len(l) > 4:
                for i in range(5):
                    s = l[int(i)]
                    g.write(',' + s)
                g.write('\n')
            else:
                for i in range(len(l)):
                    s = l[int(i)]
                    g.write(',' + s)
                g.write('\n')

df4 = pd.read_csv('File4.csv')
df5 = df4.sort_values('pyrethroid', ascending=False)
df5.index = np.arrange(1,len(df) + 1)

df5.to_csv('File4_sorted.csv')
