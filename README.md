# nivel_1
Desafio Nível 1 — PDV com Descontos (Python)

O código PDV (ou ponto de venda) consiste na lógica de vendas baseada em decisões que seguem regras de negócios, portanto ele automatiza o cálculo de descontos progressivos baseados na idade do cliente e no valor da compra, registrando o histórico das transações realizadas e exibindo um resumo detalhado ao encerrar o atendimento.

#Como ele faz:
- • Criação de listas: Criação das listas vazias para armazenar os dados de compras, descontos e valores finais
- • Ciclo de atendimento: O sistema executa um loop contínuo que apresenta o menu de opções e aguarda a escolha do consumidor.
- • Entrada e validação simples: Se a opção escolhida for `1`, o programa solicita o valor da compra e a idade do cliente, validando se os dados introduzidos são positivos, caso não, ele retorna ao loop de escolha
- • Regra 1: Desconto pela idade: Se a idade for superior ou igual a 65 anos, aplica-se automaticamente um desconto de **20%** sobre o valor original
- • Regra 2: Desconto pelo valor da compra: Verifica se o valor resultante (já com o desconto de idade aplicado) ou o valor sem desconto é superior a R$ 100,00. Caso seja, aplica-se um desconto adicional de **10%**.
- • Registro: Os valores calculados para desconto, valores finais (com ou sem desconto), lista de compras (armazenando os valores de cada compra inicialmente) são guardados nas respetivas listas utilizando o método `.append()`.
- • Resumo do dia: Quando o utilizador introduz `0`, o ciclo termina (`break`) e o programa calcula e apresenta o resumo completo com a quantidade de compras, total bruto, total de descontos e o valor final acumulado

#Como rodar:
(python pdv.py)

#Tabela de exemplos

| #  | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|----|------------|-------|----------------|----------------|----------------------|
| 1  | 50.00      | 30    | 0%             | 0%             | R$ 50.00             |
| 2  | 100.00     | 30    | 0%             | 0%             | R$ 100.00            |
| 3  | 80.00      | 65    | 20%            | 0%             | R$ 64.00             |
| 4  | 100.00     | 70    | 20%            | 0%             | R$ 80.00             |
| 5  | 125.00     | 70    | 20%            | 0%             | R$ 100.00            |
| 6  | 200.00     | 30    | 0%             | 10%            | R$ 180.00            |
| 7  | 101.00     | 30    | 0%             | 10%            | R$ 90.90             |
| 8  | 200.00     | 65    | 20%            | 10%            | R$ 144.00            |
| 9  | 1000.00    | 80    | 20%            | 10%            | R$ 720.00            |
| 10 | 200.00     | 64    | 0%             | 10%            | R$ 180.00            |