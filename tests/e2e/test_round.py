"""One real browser round and replay, fixing only the computer's moves."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_real_round_and_replay(page: Page, live_server, monkeypatch):
    """Rock loses to Paper, then Paper wins a fresh round against Rock."""
    computer_moves = iter(("paper", "rock"))
    monkeypatch.setattr(web.random, "choice", lambda _moves: next(computer_moves))
    page.goto(live_server)
    expect(page.get_by_role("status")).to_have_count(0)

    page.get_by_role("button", name="Rock", exact=True).click()
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "lose")
    expect(page.locator(".choice-value").nth(0)).to_have_text("Rock ✊")
    expect(page.locator(".choice-value").nth(1)).to_have_text("Paper ✋")

    page.get_by_role("button", name="Paper", exact=True).click()
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()
    expect(page.locator("[data-outcome]")).to_have_attribute("data-outcome", "win")
    expect(page.locator(".choice-value").nth(0)).to_have_text("Paper ✋")
    expect(page.locator(".choice-value").nth(1)).to_have_text("Rock ✊")
    expect(page.get_by_role("heading", name="Computer wins", exact=True)).to_have_count(
        0
    )
