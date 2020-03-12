import requests
import toml

config = toml.load("config.toml")

gitea_api_token = config["gitea"]["api_token"]
gitlab_api_token = config["gitlab"]["api_token"]

gitea_migrate_url = config["gitea"]["base_url"] + "/api/v1/repos/migrate"
gitlab_projects_url = config["gitlab"]["base_url"] + "/api/v4/users/virb3/projects"

gitlab_username = config["gitlab"]["username"]
gitlab_password = config["gitlab"]["password"]


def gitlab_request(url):
    return requests.get(url, headers={"Private-Token": gitlab_api_token})


def gitea_request(url, json):
    return requests.post(url, headers={"Authorization": f"token {gitea_api_token}"}, json=json)


def create_migration_body(project_url, project_description, project_path):
    return {
        "auth_username": gitlab_username,
        "auth_password": gitlab_password,
        "clone_addr": project_url,
        "description": project_description,
        "issues": True,
        "labels": True,
        "milestones": True,
        "mirror": False,
        "private": True,
        "pull_requests": True,
        "releases": True,
        "repo_name": project_path,
        "uid": 1,
        "wiki": True
    }


for project in gitlab_request(gitlab_projects_url).json():
    url = project["http_url_to_repo"]
    description = project["description"]
    path = project["path"]
    print(gitea_request(gitea_migrate_url, json=create_migration_body(url, description, path)).text)
