# we will create a hash map for some of the highest players this year in the world of ⚽
top_scorers = {
    "Cristiano Ronaldo": 25,
    "Lionel Messi": 10,
    "Antoine Griezmann": 17,
    "Kylian Mbappe": 24,
    "Erling Haaland": 24,
}
# We want to loop through the dictionary to find the player with the most goals and we want to print out who they are and
# how many goals they have.
max_goals = max(top_scorers.values())
for player, goals in top_scorers.items():
    if goals == max_goals:
        print(f"{player} has the most goals with {goals} this year.")
