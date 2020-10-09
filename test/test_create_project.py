from model import project


def test_create_project(app):
    app.session.login("administrator", "root")
    app.project.create(project)
