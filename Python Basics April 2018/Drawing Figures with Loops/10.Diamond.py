num = int(input())
    
for i in range(1, (num + 3) // 2):
    if (num + 1) // 2 >= i:
        if i == 1:
            if num % 2 == 0:
                print(f"{'-' * ((num - 2) // 2)}**{'-' * ((num - 2) // 2)}")
            else:
                print(f"{'-' * ((num - 1) // 2)}*{'-' * ((num - 1) // 2)}")
        else:
            if num % 2 == 0:
                print(f"{'-' * ((num - (i - 1) * 2 - 2) // 2)}*{'-' * ((i - 1) * 2)}*{'-' * ((num - (i - 1) * 2 - 2) // 2)}")
            else:
                print(f"{'-' * ((num - (i - 1) * 2 - 1) // 2)}*{'-' * ((i - 1) * 2 - 1)}*{'-' * ((num - (i - 1) * 2 - 1) // 2)}")

for i in range((num - 1) // 2, 0, -1):
    if (num + 1) // 2 >= i:
        if i == 1:
            if num % 2 == 0:
                print(f"{'-' * ((num - 2) // 2)}**{'-' * ((num - 2) // 2)}")
            else:
                print(f"{'-' * ((num - 1) // 2)}*{'-' * ((num - 1) // 2)}")
        else:
            if num % 2 == 0:
                print(f"{'-' * ((num - (i - 1) * 2 - 2) // 2)}*{'-' * ((i - 1) * 2)}*{'-' * ((num - (i - 1) * 2 - 2) // 2)}")
            else:
                print(f"{'-' * ((num - (i - 1) * 2 - 1) // 2)}*{'-' * ((i - 1) * 2 - 1)}*{'-' * ((num - (i - 1) * 2 - 1) // 2)}")