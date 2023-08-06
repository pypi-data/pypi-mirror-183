import os


class GitlabConfig:
    env_mapping = {
        "CI_SERVER_URL": "server_url",
        "CI_MERGE_REQUEST_IID": "mr_id",
        "CI_PROJECT_ID": "project_id",
        "CI_JOB_NAME": "job_name",
        "GITLAB_PRIVATE_TOKEN": "private_token"
    }

    converters = {
        "mr_id": int,
        "project_id": int
    }

    def __init__(self, **kwargs):
        self.get_from_environ()

        for attr_name, attr_value in kwargs.items():
            if attr_value is None:
                continue

            if attr_name in self.env_mapping.values():
                setattr(self, attr_name, attr_value)

    def get_from_environ(self):
        for env_name, attr_name in self.env_mapping.items():
            attr_value = os.environ.get(env_name)
            if attr_value and attr_name in self.converters:
                attr_value = self.converters[attr_name](attr_value)
            setattr(self, attr_name, attr_value)
