import random
import string
from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    def generate_project_data(self):
        Project.name = ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(random.randrange(20)))
        Project.status = random.choice(['development', 'release', 'stable', 'obsolete'])
        Project.inherit_global = random.choice([True, False])
        Project.view_state = random.choice(['public', 'private'])
        Project.description = ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(random.randrange(50)))
        return Project

    def fill_project_form(self, Project):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name('name').send_keys(Project.name)
        wd.find_element_by_name('status').click()
        Select(wd.find_element_by_name('status')).select_by_visible_text(Project.status)
        if Project.inherit_global == False:
            wd.find_element_by_name('inherit_global').click()
        wd.find_element_by_name('view_state').click()
        Select(wd.find_element_by_name('view_state')).select_by_visible_text(Project.view_state)
        wd.find_element_by_name('description').send_keys(Project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def open(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

