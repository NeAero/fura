USD_TO_RUB = 78,59
def convert_jpy_to_rub(amount):
    return amount * JPY_TO_RUB
Usd = float(input('Сумма в иенах:'))
rub= convert_jpy_to_rub(jpy)
print(f'{jpy:.2f}JPY={rub:.2f}RUB'.replace(',',' '))