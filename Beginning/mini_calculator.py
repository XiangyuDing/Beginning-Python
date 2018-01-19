import sys # sys.exit() quits the program

line = input()
split = line.split()

if len(split) != 3:
    print("Wrong format!")
    sys.exit()

left = int(split[0])
op = split[1]
right = int(split[2])

val = 0

if op == '+':
    val = left + right
elif op == '-':
    val = left - right
elif op == '*':
    val = left * right
elif op == '/':
    if right == 0:
        print("Division by zero. Halting")
        sys.exit()
    val = left / right
else:
    print("Unknown operator:{operator}".format(operator=op))
    sys.exit()

print("{line_expr} = {value:.2f}".format(line_expr=line, value=val))