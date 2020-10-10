from model.project import Project
from random import randrange


def test_delete_project(app, db):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects = db.get_project_list()
    index = randrange(len(old_projects))
    name = old_projects[index].name
    app.project.open(name)
    app.project.delete()

    old_projects[index:index+1] = []
    new_projects = db.get_project_list()

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)