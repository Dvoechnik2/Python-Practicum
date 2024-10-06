req = [
    ('John', 32, 2),
    ('Alice', 32, 1),
    ('Bob', 50, 3),
    ('Eve', 1, 1),
    ('Clara', 1, 2)
]


def main(requests):
    requests = sorted(requests, key=lambda x: (x[1], x[2]))
    time = 0
    final_req = []
    for i in range(len(requests)):
        if time + requests[i][1] < 50:
            time += requests[i][1]
            final_req.append(requests[i])
        else:
            break
    r = final_req[-1]
    if r[1] > 30:
        r = final_req[-1]
        final_req[-1] = (r[0], r[1] // 2, r[2])
        final_req.append((r[0], r[1] // 2, r[2]))
    final_req = sorted(final_req, key=lambda x: (x[2], x[1]))
    print(final_req)


if __name__ == '__main__':
    main(req)