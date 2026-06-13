import requests
import json

USERNAME = "adithyanj-27"

url = f"https://api.github.com/users/{USERNAME}/repos"

repos = requests.get(url).json()

projects = []

for repo in repos:
    projects.append({
        "name": repo["name"],
        "url": repo["html_url"]
    })

with open("projects.json", "w") as f:
    json.dump(projects, f, indent=2)

print("projects.json updated")