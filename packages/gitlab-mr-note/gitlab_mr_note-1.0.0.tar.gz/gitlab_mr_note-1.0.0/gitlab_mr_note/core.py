from gitlab import Gitlab


def post_comment(gl_config, content):
    gl = Gitlab(url=gl_config.server_url, private_token=gl_config.private_token)
    project = gl.projects.get(id=gl_config.project_id, lazy=True)
    mr = project.mergerequests.get(id=gl_config.mr_id, lazy=True)

    expected_comment = f"<!-- job: {gl_config.job_name} -->"
    body = expected_comment + content
    for note in mr.notes.list(get_all=True, iterator=True):
        if note.body.startswith(expected_comment):
            note.body = body
            note.save()
            break
    else:
        mr.notes.create({"body": body})
