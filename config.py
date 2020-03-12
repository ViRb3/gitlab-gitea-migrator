import toml

config = toml.load("config.toml")

gitea_api_token = config["gitea"]["api_token"]
gitlab_api_token = config["gitlab"]["api_token"]

gitlab_username = config["gitlab"]["username"]
gitlab_password = config["gitlab"]["password"]

gitea_migrate_url = config["gitea"]["base_url"] + "/api/v1/repos/migrate"
gitea_repos_url = config["gitea"]["base_url"] + "/api/v1/user/repos"
gitlab_projects_url = config["gitlab"]["base_url"] + f"/api/v4/projects"
gitlab_user_projects_url = config["gitlab"]["base_url"] + f"/api/v4/users/{gitlab_username}/projects"
