import datetime
from typing import Any, List
import subprocess
import pathlib
from gitstats.repo_metrics import Repository
import configparser

root_dir = str(pathlib.Path.cwd().resolve())

print("ROOT_DIR: " + root_dir)

def get_stats() -> None:

    # Parse global config
    config = configparser.ConfigParser()

    config.read(root_dir + "/config.txt")

    date_string = config.get("global", "date", raw=True)

    starting_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")

    token = config.get("global", "token", raw=True)

    metrics = list(map(lambda metric: metric.strip(), config.get(
        "global", "metrics", raw=True).split(",")))

    expected_values = list(map(lambda metric: int(metric.strip()), config.get(
        "global", "expected_values", raw=True).split(",")))

    urls = list(map(lambda metric: metric.strip(), config.get(
        "repos", "urls", raw=True).split("\n")))

    repos: List[Repository] = []
    for url in urls:
        repo = Repository(starting_date, url, token, metrics, expected_values)
        repos.append(repo)

    get_charts(repos)
    get_alerts(repos)

    subprocess.run(["rm", "-fr", root_dir + "/repo"])


def get_charts(repos: List[Repository]) -> None:

    base_dir = root_dir + "/metrics/"
    subprocess.run(["rm", "-fr", base_dir])
    subprocess.run(["mkdir", base_dir])

    for repo in repos:
        repo_name = repo.name.replace("/", "#")

        csv = repo.get_csv_output()
        markdown = repo.get_markdown_output()
        with open(base_dir + repo_name + ".csv", 'w') as f:
            f.write(csv)
        with open(base_dir + repo_name + "_markdown.txt", 'w') as f:
            f.write(markdown)


def get_alerts(repos: List[Repository]) -> None:

    base_dir = root_dir + "/alerts/"
    subprocess.run(["rm", "-fr", base_dir])
    subprocess.run(["mkdir", base_dir])

    for repo in repos:
        result = ""
        for user in repo.users:
            user_alerts = ""
            for metric in user.metrics:
                if not metric.is_achieved():
                    user_alerts += f"User {user.name} has achieved only {metric.result}/{metric.expected_value} in metric {metric.metric_name()}\n"
            result += user_alerts
        if len(result) > 0:
            repo_name = repo.name.replace("/", "#")
            with open(base_dir + repo_name + "_alerts.txt", 'w') as f:
                f.write(result)