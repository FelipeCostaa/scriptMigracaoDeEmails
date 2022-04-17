import csv
from matplotlib.pyplot import close

from pyparsing import delimitedList

with open("lista_email.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")
    for i, linha in enumerate(arquivo_csv):
        if i > 0:
            arquivoSaida = open(linha[0]+".bat", "w")
            arquivoSaida.write("imapsync.exe --host1 mail.wh1.net.br  --user1 " + linha[0] + " --password1  \"" + linha[1] + "\"  ^\n")
            arquivoSaida.write("               --host2 imap.gruposym.com.br --user2 " + linha[0] + " --password2  \"" + linha[2] + "\" ^\n")
            arquivoSaida.write("\t\t\t   \n\n\n")
            arquivoSaida.write("@PAUSE")
            arquivoSaida = close()

