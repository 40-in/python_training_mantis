import pymysql
from model.project import Project


class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password, autocommit=True)

    def get_project_list(self):
        project_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name from mantis_project_table")
            for row in cursor:
                (id, name) = row
                project_list.append(Project(id=str(id), name=name))
        finally:
            cursor.close()
        return project_list

    # def get_contact_list(self):
    #     list = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute(
    #             "select id, firstname, lastname, address, email, email2, email3, home, mobile, work from addressbook where deprecated='0000-00-00 00:00:00'")
    #         for row in cursor:
    #             (id, firstname, lastname, address, email, email2, email3, home, mobile, work) = row
    #             list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email,
    #                                 email2=email2, email3=email3, home=home, mobile=mobile, work=work))
    #     finally:
    #         cursor.close()
    #     return list

    def destroy(self):
        self.connection.close()
