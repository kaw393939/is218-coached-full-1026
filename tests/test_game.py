"""Literal RPS-001 outcomes and one request through the real rules."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_all_nine_matchups(player, computer, expected):
    """The real rule returns the spec's literal answer for each valid pair."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_real_rules_show_player_loss(monkeypatch):
    """A valid Rock submission against Paper reaches and displays real rules."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    monkeypatch.setitem(web.app.config, "TESTING", True)
    response = web.app.test_client().post("/", data={"move": "rock"})
    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Computer wins" in page
    assert 'data-outcome="lose"' in page
    assert "You chose" in page and "Computer chose" in page
    assert "Rock" in page and "Paper" in page
    assert "game rules not built yet" not in page
