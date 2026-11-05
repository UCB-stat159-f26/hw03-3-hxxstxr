def _normalize_player_name(player_name):
    """Convert a player's name to Tennis Abstract format."""
    if not isinstance(player_name, str) or not player_name.strip():
        raise ValueError("Please enter a valid player name.")

    return "".join(player_name.split()).lower()