"""RPS-001: one independent round from the player's perspective."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' for the supplied valid moves."""
    if player == computer:
        return "tie"
    winning_pairs = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    if (player, computer) in winning_pairs:
        return "win"
    return "lose"
