# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file batch_delete_github_repo.py
# @description github_delete
# @author WcJun
# @date 2022/05/15
# --------------------------------------------
#
#
from time import sleep
import requests

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token ${GITHUB_DELETE_TOKEN}",
    "X-OAuth-Scopes": "repo"
}


def batch_delete_github():
    with open('./repo.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()

    url = "https://api.github.com/repos/{}/{}"
    urls = []
    for line in data:
        name, repo = line.strip().split("/")
        urls.append(url.format(name, repo))

    for repo in urls:
        requests.delete(url=repo, headers=headers)
        print("delete repo:" + repo)
        sleep(1)


if __name__ == '__main__':
    batch_delete_github()
