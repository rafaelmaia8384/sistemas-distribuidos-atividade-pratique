# Cálculo Paralelo do Produto Escalar em Python
## Disciplina: Sistemas Distribuídos - Curso Sistemas para Internet

### Introdução
Este repositório contém um aplicativo em Python que demonstra o uso de computação paralela para calcular o produto escalar de dois vetores grandes. O aplicativo utiliza a biblioteca multiprocessing do Python para realizar cálculos de forma paralela. Este projeto serve como um exemplo educacional para demonstrar como tarefas computacionalmente intensivas podem ser distribuídas entre múltiplos processadores para uma computação mais eficiente.

### Funcionalidades
- Utiliza a biblioteca nativa multiprocessing do Python para computação paralela.
- Divide os vetores em sub-vetores para serem processados paralelamente.
- Combina os resultados parciais para obter o resultado final.

### Requisitos
- Python 3.x

### Como executar
- Clone este repositório ou baixe os arquivos diretamente.
- Abra um terminal e navegue até o diretório onde os arquivos estão localizados.
- Execute o script Python com o comando python main.py.


### Resultados Esperados
O programa deve imprimir o produto escalar dos dois vetores, calculado de duas maneiras:
- Utilizando computação paralela.
- De forma sequencial (para fins de comparação).
Ambos os resultados devem ser idênticos, demonstrando que o cálculo foi feito corretamente em ambos os casos.

