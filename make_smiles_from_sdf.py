import csv

with open('pre_smiles.csv', mode='a') as g:
    with open('sdf_file.sdf') as f:
        list_all = list(f)
        for i in range(len(list_all)):
            if list_all[i] == '>  <SMILES_Canonical>\n':
                sml = list_all[i+1]
                sml_only = sml.rstrip('\n')
                g.write('\n' + sml_only)
            elif list_all[i] == '>  <pLC50>\n':
                LC50 = list_all[i+1]
                LC50_only = LC50.rstrip('\n')
                g.write(',' + LC50_only)
            pass

with open('smiles.csv', mode='a') as g:
    with open('pre_smiles.csv') as f:
        g.write('smiles' + ',' + 'value' + '\n')
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                g.write(row[0] + ',' + row[1] + '\n')
