import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    scores = []
    for i in range(1, argc):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")

    if len(scores) == 0:
        print(
            "No scores provided. Usage: python3"
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        print("Score processed: [", end='')
        for i in range(0, len(scores)):
            if i < len(scores) - 1:
                print(f"{scores[i]}, ", end='')
            else:
                print(f"{scores[i]}]")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        aver = round(sum(scores) / len(scores), 1)
        print(f"Average score: {aver}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        ran = max(scores) - min(scores)
        print(f"Score range: {ran}")


if __name__ == "__main__":
    ft_score_analytics()
