hero_name = "Alex"
def play_round():
    points = 10
    print(f"{hero_name} earned {points} points inside the function.")
    play_round()
    print(f"Outside: We can still see {hero_name}.")
