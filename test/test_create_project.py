from model.project import Project


def test_create_project(app, db):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects = db.get_project_list()
    project = app.project.generate_project_data()
    app.project.fill_project_form(project)

    old_projects.append(Project(name=project.name))
    new_projects = db.get_project_list()

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
