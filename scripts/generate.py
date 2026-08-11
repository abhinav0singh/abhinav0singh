#!/usr/bin/env python3
"""
Regenerates assets/skyline.svg from live GitHub contribution data.
Run by .github/workflows/assets.yml. Stdlib only — no pip installs needed.

Env vars:
  GH_TOKEN     - a token with public read access (the default Actions
                 GITHUB_TOKEN works fine)
  GH_USERNAME  - defaults to abhinav0singh
"""
import json
import os
import sys
import urllib.request
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
from lib import build_isometric_skyline_svg

USERNAME = os.environ.get("GH_USERNAME", "abhinav0singh")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("No GH_TOKEN/GITHUB_TOKEN set — cannot call the GitHub API.", file=sys.stderr)
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": f"{USERNAME}-profile-readme",
}

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays { date contributionCount }
        }
      }
    }
  }
}
"""


def graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main():
    gql = graphql(QUERY, {"login": USERNAME})
    weeks = gql["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    daily = []
    for w in weeks:
        for d in w["contributionDays"]:
            daily.append((date.fromisoformat(d["date"]), d["contributionCount"]))
    daily.sort()

    svg = build_isometric_skyline_svg(daily)
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "skyline.svg")
    with open(out_path, "w") as f:
        f.write(svg)
    print(f"Updated skyline.svg — {sum(c for _, c in daily)} contributions across {len(daily)} days.")


if __name__ == "__main__":
    main()
