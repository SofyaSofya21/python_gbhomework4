n = int(input('Введите кол-во шариков (до 1000): '))
list_row = [int(input('Введите коды цветов шариков (от 0 до 9): ')) for i in range(n)]
count = 0
while len(list_row) >= 3:
    i = 0
    while i < len(list_row) - 2:
        if list_row[i] == list_row[i+1] == list_row[i+2]:
            temp_val = list_row[i]
            while temp_val == list_row[i]:
                temp_val = list_row.pop(i)
                count +=1
                if i == len(list_row):
                    break
            i = 0
        else:
            i += 1    
    break
print('Кол-во шариков к удалению: ' + str(count))