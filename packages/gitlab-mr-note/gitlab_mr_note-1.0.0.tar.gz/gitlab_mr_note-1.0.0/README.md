# Post or Update Comments on Gitlab MR

The idea behind this project is to post content on the Gitlab MR which
dynamically updates as new commits are made. In order to do that, we add a
comment at the start of our content to identify the job the content is from.

## Usage

- General Access Token from `Settings > Access Tokens` with `api` permissions.
- Go to `Settings > CI/CD > Variables > Add Variables`
- Set the key to `GITLAB_PRIVATE_TOKEN` and value to key generated in first step.
- Set `Mask` flag and uncheck `Protect` flag.
- Create a test like follows

```yaml
test:
  stage: test
  script:
    - pip install gitlab-mr-note
    - echo hello world | gitlab-mr-note
  only:
    - merge_requests
```

`gitlab-mr-note` infers the details from environment variables set in the CI.
For manual usage, pass the following args.

```
Usage: gitlab-mr-note [OPTIONS]

Options:
  -s, --server-url TEXT     Server URL of gitlab instance
  -m, --mr-id TEXT          ID of the MR to comment on
  -p, --project-id TEXT     ID of the Project
  -j, --job-name TEXT       Job Name
  -t, --private-token TEXT  Private Token
  --help                    Show this message and exit.
```
