import requests

from config import *


def gitlab_get(url):
    return requests.get(url, headers={"Private-Token": gitlab_api_token})


def gitlab_delete(url):
    return requests.delete(url, headers={"Private-Token": gitlab_api_token})


def gitea_get(url):
    return requests.get(url, headers={"Authorization": f"token {gitea_api_token}"})


def gitea_post(url, json):
    return requests.post(url, headers={"Authorization": f"token {gitea_api_token}"}, json=json)
