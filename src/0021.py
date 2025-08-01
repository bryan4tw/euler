# Names Scores

# import src/0021.txt as an array of strings
with open("input/0021.txt", "r") as f:
    names = f.read().strip().split(",")

names = [name.strip('"') for name in names]
names = sorted(names)


def score_name(name):
    score = 0
    for char in name:
        score += ord(char) - ord("A") + 1
    return score


def total_score(names):
    total_score = 0
    for i in range(len(names)):
        total_score += score_name(names[i]) * (i + 1)
    return total_score


print(f"Total score of names: {total_score(names)}")
