def hanoi_solver(n):
    a = list(range(n, 0, -1))
    b = []
    c = []

    history = [f"{a} {b} {c}"]

    def solve(k, source, target, auxiliary):
        if k <= 0:
            return

        solve(k - 1, source, auxiliary, target)

        target.append(source.pop())
        history.append(f"{a} {b} {c}")

        solve(k - 1, auxiliary, target, source)

    solve(n, a, c, b)
    return "\n".join(history)