from database.models.usuario import Usuario
from database.database import db
from views.home import home_route
from views.usuario import usuario_route
from database.database import dblog
from database.models.blog import Blog


def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(usuario_route)



def configure_db():
    db.connect()
    db.create_tables([Usuario],safe=True)
    dblog.connect()
    dblog.create_tables([Blog],safe=True)
    


