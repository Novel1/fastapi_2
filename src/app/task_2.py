def func_number(number):
    answer_number = ''
    if len(number) > 5:
        answer_number += number[:-5]
        answer_number += number[-5:][::-1]
    else:
        answer_number = number
    return answer_number


input_number = input('Введите число:')
answer = func_number(input_number)
print(answer)