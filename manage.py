# -*-coding:utf-8 -*-
import os
from flask_migrate import Migrate
from blockchainscm import create_app, db
from blockchainscm.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestResult(verbosity=2).run(tests)

