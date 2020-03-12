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


gitlab_projects = gitlab_get(gitlab_user_projects_url).json()
gitea_projects = gitea_get(gitea_repos_url).json()

pending_projects = [p for p in gitlab_projects if any(p2 for p2 in gitea_projects if p2["name"] == p["path"])]
for project in pending_projects:
    print(gitlab_delete(gitlab_projects_url + f'/{project["id"]}'))
