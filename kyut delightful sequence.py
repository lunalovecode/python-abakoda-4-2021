from itertools import count

def is_composite(value):
    for potential_div in range(1, int(value**0.5 + 5)):
        if value % potential_div == 0:
            b = potential_div
            a = value // potential_div
            if 1 <= a < value and 1 <= b < value:
                return True
    return False

def get_sequence(m, n):
    A = [m]
    for next_term in range(n - 1):
        for maybe_next in count(1):
            confirmed_next = True
            for previous_term in A:
                if not is_composite(previous_term + maybe_next):
                    confirmed_next = False
            if confirmed_next:
                A.append(maybe_next)
                break
    return A

line = input().split()
m = int(line[0])
n = int(line[1])
first_few = get_sequence(5, m)
if n <= 5:
    print(first_few[n - 1])
else:
    print(first_few[2])