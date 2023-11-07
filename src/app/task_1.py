def func_words(words):
    symbol = len(words) * 60
    return f'{symbol // 100} р. {symbol % 100} коп.'


input_words = input('Введите текст:')
answer = func_words(input_words)
print(answer)

