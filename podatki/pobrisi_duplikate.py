from more_itertools import unique_everseen
with open('atrakcije_po_drzavah.csv','r') as f, open('pocisceno_atrakcije.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))