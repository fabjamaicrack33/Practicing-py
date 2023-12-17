from exchange import rate

base_currency = 'USD'
target_currency = 'COP'

exchange_rate = rate(base_currency, target_currency)
print(f"La tasa de cambio de {base_currency} a {target_currency} es: {exchange_rate}")


