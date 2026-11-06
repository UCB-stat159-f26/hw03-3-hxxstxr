import matplotlib.pyplot as plt


def plot_age_difference(matches):
    """Plot age differences across a player's career matches."""
    fig, ax = plt.subplots(figsize = (10, 6))

    for result, color in [("win", "blue"), ("loss", "red")]:
        data = matches[matches["result"] == result]
        ax.scatter(
            data["player_age"],
            data["age_difference"],
            color = color,
            alpha = 0.5,
            s = 15,
            label = result.capitalize(),
        )

    ax.axhline(0, color = "gray", linestyle = "--")
    ax.set_xlabel("Player Age")
    ax.set_ylabel("Opponent Age - Player Age")
    ax.set_title("Career Matches by Age Difference")
    ax.legend()

    return fig