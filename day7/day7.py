input = [i for i in open("./day7/input.txt").read().split("\n") if i.strip()]
import collections


def calculate_hand_value(hand, use_part1):
    if use_part1:
        hand = hand.replace("J", "X")

    card_values = ["J23456789TXQKA".index(card) for card in hand]

    hand_types = []
    for rank in "J23456789TQKA":
        hand_with_rank = hand.replace("J", rank)
        card_counts = collections.Counter(hand_with_rank)
        sorted_counts = tuple(sorted(card_counts.values()))
        hand_type = [
            (1, 1, 1, 1, 1),
            (1, 1, 1, 2),
            (1, 2, 2),
            (1, 1, 3),
            (2, 3),
            (1, 4),
            (5,),
        ].index(sorted_counts)
        hand_types.append(hand_type)

    return (max(hand_types), card_values)


def calculate_score(hands_and_bets_sorted):
    total_score = 0
    for i, (_, bet) in enumerate(hands_and_bets_sorted):
        total_score += i * bet + bet
    return total_score


def part1(input):
    hands_and_bets = [
        (calculate_hand_value(hand, True), int(bet))
        for hand, bet in (line.split() for line in input)
    ]
    hands_and_bets_sorted = sorted(hands_and_bets, key=lambda x: x[0])

    total_score = calculate_score(hands_and_bets_sorted)

    return total_score


def part2(input):
    hands_and_bets = [
        (calculate_hand_value(hand, False), int(bet))
        for hand, bet in (line.split() for line in input)
    ]
    hands_and_bets_sorted = sorted(hands_and_bets, key=lambda x: x[0])

    total_score = calculate_score(hands_and_bets_sorted)

    return total_score


def main():
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
