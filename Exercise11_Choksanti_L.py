# พีระมิดกำหนดความสูงจาก input
high = int(input("Enter the height of the pyramid: "))

for i in range(high):
    print(" " * (high - i - 1) + "*" * (2 * i + 1))
    
