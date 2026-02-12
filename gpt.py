n = int(input())  # Read the number of participants
scores = list(map(int, input().split()))  # Read scores

winner_up = max(scores)  # Get the highest score
runner_up = float('')  # Initialize runner-up as a very low number

for element in scores:
    if runner_up < element < winner_up:  # If element is between max and runner-up
        runner_up = element

print(runner_up)  # Print the runner-up score
