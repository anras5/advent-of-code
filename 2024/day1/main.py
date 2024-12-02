# task 1
l = sum(
    [
        abs(a - b)
        for a, b in zip(
            sorted(
                int(tuple(filter(lambda x: x, word.split(" ")))[0])
                for word in open("input.txt").read().split("\n")
            ),
            sorted(
                int(tuple(filter(lambda x: x, word.split(" ")))[1])
                for word in open("input.txt").read().split("\n")
            ),
        )
    ]
)
print(l)

# task 2
l2 = sum(
    [
        abs(
            a
            * len(
                list(
                    filter(
                        lambda x: x == a,
                        [
                            int(tuple(filter(lambda x: x, word.split(" ")))[1])
                            for word in open("input.txt").read().split("\n")
                        ],
                    )
                )
            )
        )
        for a in [
            int(tuple(filter(lambda x: x, word.split(" ")))[0])
            for word in open("input.txt").read().split("\n")
        ]
    ]
)
print(l2)
