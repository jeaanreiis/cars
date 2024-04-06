import os


from app import create_app, db
from app.models import Cars, Buy
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Cars": Cars, "Buy": Buy}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()
