import random
score, rounds, historial = 0, 0, []

def roll(n):
    return sum(random.dandint(1,6) for _ in range(n))

def shop(s):
    if input("store (extra dice, y/n): ").lower() == "s" and s >= 5:
        return s - 5, 1
    return s, 0

while True:
    extra = 0
    if input("Visit Store? (y/n): ").lower() == "s":
        score, extra = shop(score)
    j, c = roll(2 + extra), roll(2)
    print("Player:", j, "| Computer:", c)
    res = "Tie" if j == c else ("Win" if j > c else "Loss")
    score += 10 if j > c else (-5 if j < c else 2)
    rounds += 1 
    historial.append((rounds, j, c, res))
    if input("Continue? (y/n): "). lower() != "s":
        break

print("n\Rounds:", rounds, "| Final Score:", score)
for r, j, c, res in historial:
    print(f"Rounds {r}: {j} vs {c} -> {res}")