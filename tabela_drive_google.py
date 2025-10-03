import csv

with open(r"C:\Users\lenovo\OneDrive\Documents\AULA_Python.csv", encoding="utf-8") as joaquim_arquivo:
    j_reader=csv.reader(joaquim_arquivo, delimiter=",")
    
    line=0
    for row in j_reader:
        if line == 0:
            print(f"As colunas estão representadas em: {",".join(row)}")
            line +=1
        else:
            print(f"{row[0]} tem {row[1]} de idade,Vive em {row[2]} e trabalha como {row[3]}.Tem um salario de KZ${row[4]}, usa o carro de marca {row[5]}.Tem casa? {row[6]}, tem filho {row[7]}.")
            line +=1

print(f"A lista contém: {line} linhas.")