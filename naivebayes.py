#Exercício 02 - Naive Bayes De Laboratório de Inteligência Artificial
# Autor: Guilherme Costa

#Recebimento de entradas

entrada = input().rstrip()
n, m = entrada.split(" ") #n - numero de registros m - número de testes
n = int(n)
m = int(m)

dataset = list()

for i in range(1,n):
    entrada = input().rstrip()
    registro = entrada.split(",")
    dataset.append(registro)

inst_teste = (input().rstrip().split(","))

num_atributos = len(dataset[0]) - 1
classe_no = [i for i in dataset if i[-1] == "no-recurrence-events"]
classe_yes = [i for i in dataset if i[-1] == "recurrence-events"]

## Iteração Que Calcula a probabilidade da instância teste dado que a classe é no-recurrencec-events

prob_no = len(classe_no)/n
for i in range(num_atributos):
    numOcorrenciasAttr = len(list(filter(lambda x: x[i] == inst_teste[i], classe_no))) #Filtra as linhas onde a lista classe1 possui o valor da instância
    # o valor do tamanho da lista acima será o número de ocorrências do valor da instância dado que classe = 1
    probAttr = numOcorrenciasAttr/len(classe_no)
    prob_no*= probAttr


## Iteração Que Calcula a probabilidade da instância teste dado que a classe é recurrence-events
prob_yes = len(classe_yes)/n
for i in range(num_atributos):
    numOcorrenciasAttr = len(list(filter(lambda x: x[i] == inst_teste[i], classe_yes))) #Filtra as linhas onde a lista classe1 possui o valor da instância
    # o valor do tamanho da lista acima será o número de ocorrências do valor da instância dado que classe = 1
    probAttr = numOcorrenciasAttr/len(classe_yes)
    prob_yes*= probAttr


if prob_yes >= prob_no:
    print("recurrence-events")
else:
    print("no-recurrence-events")
    
#input()