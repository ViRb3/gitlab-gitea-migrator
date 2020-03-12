# GitLab to Gitea Migrator
> Batch repository migrator from GitLab to Gitea using their APIs

## Usage
1. Create a `config.toml` using the provided [example](config.toml.example)
2. Run:
    ```python
    poetry install
    ```

### Migrate from GitLab to Gitea
```python
poetry run python migrate.py
```

### Delete migrated repos from GitLab
```python
poetry run python clean.py
```

### Change all local repo remote URLs
```bash
grep -Irl "url = https://gitlab.com/john/" | xargs sed -i 's@url = https://gitlab.com/john/@url = https://git.example.com/john/@g'
```