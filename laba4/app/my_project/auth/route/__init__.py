from flask import Flask

from .error_handler import err_handler_bp



def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .orders.affiliation_route import affiliation_bp
    from .orders.attempt_route import attempt_bp
    from .orders.attempt_answer_route import attempt_answer_bp
    from .orders.author_route import author_bp
    from laba4.app.my_project.auth.route.orders.course_route import course_bp
    from laba4.app.my_project.auth.route.orders.lecture_route import lecture_bp
    from laba4.app.my_project.auth.route.orders.module_route import module_bp
    from laba4.app.my_project.auth.route.orders.progress_route import progress_bp
    from laba4.app.my_project.auth.route.orders.test_route import test_bp
    from .orders.student_route import student_bp
    from laba4.app.my_project.auth.route.orders.test_question_route import test_question_bp
    app.register_blueprint(affiliation_bp)
    app.register_blueprint(attempt_bp)
    app.register_blueprint(attempt_answer_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(lecture_bp)
    app.register_blueprint(module_bp)
    app.register_blueprint(progress_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(test_question_bp)