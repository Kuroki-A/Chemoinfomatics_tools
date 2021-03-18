from rdkit import Chem
import csv

with open ('compare_canonical.txt', mode='a') as g:
    with open('compare_smiles.csv') as f:
        reader = csv.reader(f) # readerオブジェクトを作成
        for row in reader:
            x = Chem.MolFromSmiles(row[0])
            if x == None:
                g.write('\n' + row[0])
                continue
            m = Chem.MolToSmiles(x)
            g.write('\n' + m)
