import sqlalchemy

from laba4.app.my_project.auth.dao.general_dao import GeneralDAO
from laba4.app.my_project.auth.domain.orders.authors import Author


class AuthorDAO(GeneralDAO):
    _domain_type = Author

    def insert_author(self, name, title, email):
        self._session.execute(sqlalchemy.text("CALL InsertIntoAuthors(:p1, :p2, :p3)"),
                              {"p1": name, "p2": title, "p3": email})
        self._session.commit()

    def insert_multiple_authors(self, name):
        self._session.execute(sqlalchemy.text("CALL InsertIntoMultipleAuthors(:p1)"),
                              {"p1": name})
        self._session.commit()


