input_number = int(input('Введите целое число от 3 до 20 включительно - '))

result = []
for i in range(1, 20):
    for j in range(i+1, input_number):
        if input_number % (i+j)==0:
            result.append(i)
            result.append(j)
print(*result)
