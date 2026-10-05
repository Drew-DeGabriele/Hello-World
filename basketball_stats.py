"""
basketball_stats.py
Sample Python script: calculates common basketball shooting stats
for a small set of players and prints a sorted summary table.
"""

players = [
    # name, points, field goals made, field goals attempted, 3PM, FTA
    {"name": "Player A", "pts": 412, "fgm": 150, "fga": 320, "tpm": 48, "fta": 90},
    {"name": "Player B", "pts": 355, "fgm": 140, "fga": 300, "tpm": 20, "fta": 70},
    {"name": "Player C", "pts": 298, "fgm": 105, "fga": 250, "tpm": 55, "fta": 50},
    {"name": "Player D", "pts": 240, "fgm": 98, "fga": 190, "tpm": 10, "fta": 60},
]


def fg_pct(p):
    """Field goal percentage."""
    return p["fgm"] / p["fga"] if p["fga"] else 0.0


def efg_pct(p):
    """Effective field goal percentage: (FGM + 0.5 * 3PM) / FGA."""
    return (p["fgm"] + 0.5 * p["tpm"]) / p["fga"] if p["fga"] else 0.0


def ts_pct(p):
    """True shooting percentage: PTS / (2 * (FGA + 0.44 * FTA))."""
    denom = 2 * (p["fga"] + 0.44 * p["fta"])
    return p["pts"] / denom if denom else 0.0


def main():
    ranked = sorted(players, key=ts_pct, reverse=True)
    print(f"{'Player':<10}{'PTS':>6}{'FG%':>8}{'eFG%':>8}{'TS%':>8}")
    print("-" * 40)
    for p in ranked:
        print(f"{p['name']:<10}{p['pts']:>6}"
              f"{fg_pct(p):>8.1%}{efg_pct(p):>8.1%}{ts_pct(p):>8.1%}")


if __name__ == "__main__":
    main()
