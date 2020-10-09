import random
import string
from selenium.webdriver.support.ui import Select
from model import project


class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    def generate_project_data(self):
        project.name = ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(random.randrange(20)))
        project.status = random.choice(['development', 'release', 'stable', 'obsolete'])
        project.inherit_global = random.choice([True, False])
        project.view_state = random.choice(['public', 'private'])
        project.description = ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(random.randrange(50)))
        return project

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name('name').send_keys(project.name)
        wd.find_element_by_name('status').click()
        Select(wd.find_element_by_name('status')).select_by_visible_text(project.status)
        if project.inherit_global == False:
            wd.find_element_by_name('inherit_global').click()
        wd.find_element_by_name('view_state').click()
        Select(wd.find_element_by_name('view_state')).select_by_visible_text(project.view_state)
        wd.find_element_by_name('description').send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def create(self, project):
        self.open_projects_page()
        self.generate_project_data()
        self.fill_project_form(project)

# def get_project_list(self):
#         wd = self.app.wd
#         self.open_contacts_page()
#         self.contact_cache = []
#         for element in wd.find_elements_by_name("entry"):
#             cells = element.find_elements_by_tag_name("td")
#             firstname = cells[2].text
#             lastname = cells[1].text
#             address = cells[3].text
#             id = element.find_element_by_name("selected[]").get_attribute("value")
#             all_phones = cells[5].text
#             all_emails = cells[4].text
#             self.contact.append(
#                 Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones,
#                         address=address, all_emails_from_home_page=all_emails))
#     return self.contact
