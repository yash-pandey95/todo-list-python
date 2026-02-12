n = int(input())
scores = list(map(int,input().split()))
winner_up = max(scores)
runner_up = scores[0]
for element in scores:
    if element > runner_up and runner_up<winner_up:
        runner_up = element
print(runner_up)        