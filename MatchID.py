import datetime
import uuid

def generate_match_id(player_name):
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Generate a unique identifier for the match
    unique_id = str(uuid.uuid4())[:8]  # Shorten UUID to 8 characters for simplicity
    # Combine player name, timestamp, and unique ID
    match_id = f"{player_name}_{timestamp}_{unique_id}"
    return match_id

# Example usage
player_name = "MrFool神"
match_id = generate_match_id(player_name)
print("Generated Match ID:", match_id)
