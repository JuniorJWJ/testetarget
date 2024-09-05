import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

valores = [dia['valor'] for dia in dados if dia['valor'] > 0]  # Ignora dias sem faturamento

menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
