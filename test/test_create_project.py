from model.project import Project


def test_create_project(app, db):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects = app.soap.mc_projects_get_user_accessible("administrator", "root")
    project = app.project.generate_project_data()
    app.project.fill_project_form(project)

    old_projects.append(Project(name=project.name))
    new_projects = app.soap.mc_projects_get_user_accessible("administrator", "root")

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
