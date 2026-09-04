blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1  # Начинаем с первого слоя (нужен 1 блок)

while blocks >= layer:  # Пока хватает блоков на текущий слой
    blocks -= layer     # Забираем блоки на этот слой
    height += 1         # Высота увеличилась на 1
    layer += 1          # Переходим к следующему слою (нужно на 1 блок больше)

print("The height of the pyramid:", height)