from itertools import count

def get_next_term(n):
    for maybe_next in count(1):
        if maybe_next ** 2 >= n:
            break
    
    if maybe_next == 1:
        return None
    else:
        return maybe_next - 1

l = input().split()
m = int(l[0])
n = int(l[1])

# print(get_next_term(m))

def generate_terms(m):
    A = [m]
    next_term = get_next_term(A[-1])
    while next_term is not None:
        A.append(next_term)
        next_term = get_next_term(A[-1])
    return A

A = generate_terms(m)
if n <= len(A):
    print(A[n - 1])
else:
    print(-1)