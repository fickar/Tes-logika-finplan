def print_pattern(N):
    if N % 2 == 0:
        print("Harus bilangan ganjil")
        return

    pattern = [["X"] * N for _ in range(N)]

    for i in range(1, N-1):
        for j in range(1, N-1):
            if i == j or i == N - 1 - j:
                pattern[i][j] = "O"

    for row in pattern:
        print("".join(row))

N = 7
print_pattern(N)

N = 6
print_pattern(N)
