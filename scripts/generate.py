#!/usr/bin/env python3
"""
Regenerates assets/skyline.svg and assets/stats.svg from live GitHub data.
Run by .github/workflows/assets.yml. Stdlib only — no pip installs needed.

Env vars:
  GH_TOKEN       - a token with public read access (the default Actions
                   GITHUB_TOKEN works fine)
  GH_USERNAME    - defaults to abhinav0singh
"""
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from lib import build_skyline_svg, build_stats_svg, CYAN, MINT, BLUE_TEAL, GREEN_TEAL

USERNAME = os.environ.get("GH_USERNAME", "abhinav0singh")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
if not TOKEN:
    print("No GH_TOKEN/GITHUB_TOKEN set — cannot call the GitHub API.", file=sys.stderr)
    sys.exit(1)

HEADERS_REST = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "User-Agent": f"{USERNAME}-profile-readme",
}
HEADERS_GQL = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": f"{USERNAME}-profile-readme",
}


def rest(path):
    req = urllib.request.Request(f"https://api.github.com{path}", headers=HEADERS_REST)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers=HEADERS_GQL)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


CONTRIB_QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { contributionCount }
        }
      }
    }
  }
}
"""


def main():
    user = rest(f"/users/{USERNAME}")
    followers = user.get("followers", 0)
    following = user.get("following", 0)
    public_repos = user.get("public_repos", 0)

    gql = graphql(CONTRIB_QUERY, {"login": USERNAME})
    cal = gql["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    total = cal["totalContributions"]
    weekly = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in cal["weeks"]]

    skyline_svg = build_skyline_svg(weekly, total)
    stats_svg = build_stats_svg([
        (str(public_repos), "Repositories", CYAN),
        (str(total), "Contributions / yr", MINT),
        (str(followers), "Followers", BLUE_TEAL),
        (str(following), "Following", GREEN_TEAL),
    ])

    out_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    with open(os.path.join(out_dir, "skyline.svg"), "w") as f:
        f.write(skyline_svg)
    with open(os.path.join(out_dir, "stats.svg"), "w") as f:
        f.write(stats_svg)
    print(f"Updated skyline.svg and stats.svg — {total} contributions, {public_repos} repos.")


if __name__ == "__main__":
    main()
