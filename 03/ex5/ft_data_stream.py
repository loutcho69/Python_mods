import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["bob", "charlie", "alice", "dylan"]
    actions = ["move", "climb", "use", "grab", "release", "swim", "sleep"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    lst: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while lst:
        pick = random.choice(lst)
        lst.remove(pick)
        yield pick


def display() -> None:
    g = gen_event()
    for i in range(1000):
        event = next(g)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events = []
    for i in range(10):
        event = next(g)
        events.append(event)
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


def main() -> None:
    print("=== Game Data Stream Processor ===")
    display()


if __name__ == "__main__":
    main()
