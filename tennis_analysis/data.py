import json
import re
import requests

def _normalize_player_name(player_name):
    """Convert a player's name to Tennis Abstract format."""
    if not isinstance(player_name, str) or not player_name.strip():
        raise ValueError("Please enter a valid player name.")

    return "".join(player_name.split()).lower()


def _download_career_js(player_slug):
    """Download a player's career match data from Tennis Abstract."""
    url = (
        "https://www.tennisabstract.com/jsmatches/"
        f"{player_slug}Career.js"
    )

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ValueError(
            f"Could not retrieve career data for '{player_slug}'."
        ) from error

    if "var morematchmx" not in response.text:
        raise ValueError(
            f"No valid career match data found for '{player_slug}'."
        )

    return response.text

def _parse_career_js(js_text):
    """Extract match records from Tennis Abstract JavaScript."""
    match = re.search(
        r"var\s+morematchmx\s*=\s*(\[[\s\S]*?\]);",
        js_text,
    )

    if match is None:
        raise ValueError("Could not find career match records.")

    return json.loads(match.group(1))