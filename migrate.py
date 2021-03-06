from util import *


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


for project in gitlab_get(gitlab_user_projects_url).json():
    url = project["http_url_to_repo"]
    description = project["description"]
    path = project["path"]
    print(gitea_post(gitea_migrate_url, json=create_migration_body(url, description, path)).text)
