import json
import re
import requests
import pandas as pd

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


from datetime import datetime


def _calculate_age(birth_date, match_date):
    """Calculate a player's age at the time of a match."""
    if not birth_date:
        return None

    dob = datetime.strptime(birth_date, "%Y%m%d")
    match_day = datetime.strptime(match_date, "%Y%m%d")

    return (match_day - dob).days / 365.2425


def _get_opponent_age(age_value, match_date):
    """Handle opponent DOB or age from career match data."""
    if not age_value:
        return None

    try:
        if len(age_value) == 8 and age_value.isdigit():
            return _calculate_age(age_value, match_date)

        return float(age_value)
    except (ValueError, TypeError):
        return None


def _clean_match(match, player_dob):
    """Convert one career match into a cleaned record."""
    match_date = match[0]
    player_age = _calculate_age(player_dob, match_date)
    opponent_age = _get_opponent_age(match[16], match_date)

    if opponent_age is None:
        return None

    return {
        "date": match_date,
        "tournament": match[1],
        "surface": match[2],
        "result": "win" if match[4] == "W" else "loss",
        "opponent": match[11],
        "player_age": player_age,
        "opponent_age": opponent_age,
        "age_difference": opponent_age - player_age,
    }


def _build_match_dataframe(matches, player_dob):
    """Build a DataFrame from cleaned career match records."""
    cleaned = []

    for match in matches:
        record = _clean_match(match, player_dob)
        if record is not None:
            cleaned.append(record)

    if not cleaned:
        raise ValueError("No matches with valid age information were found.")

    return pd.DataFrame(cleaned)