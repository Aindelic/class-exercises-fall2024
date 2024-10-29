def hello_world():
    return "Hello world!"


def rps(hand1, hand2):
    if hand1 == hand2:
        return "It's a tie!"
    elif hand1 == "rock":
        return "Rock wins!" if hand2 == "scissors" else "Paper wins!"
    elif hand1 == "paper":
        return "Paper wins!" if hand2 == "rock" else "Scissors win!"
    elif hand1 == "scissors":
        return "Scissors win!" if hand2 == "paper" else "Rock wins!"
    else:
        return "Invalid"
