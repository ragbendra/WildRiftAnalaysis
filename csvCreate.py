import csv

def save_match_data(match_id, player_name, champion, kills, deaths, assists, win_loss):
    # Append match data to a CSV file
    with open("wildrift_matches.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([match_id, player_name, champion, kills, deaths, assists, win_loss])

# Example usage
save_match_data(match_id, "Ragha", "Jinx", 10, 2, 8, "Win")
