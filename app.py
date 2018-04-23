import os
from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
import connexion
from services.RedisProvider import RedisProvider



def configure(binder: Binder) -> Binder:
    binder.bind(
        RedisProvider,
        RedisProvider([{"Name": "Test 1"}])
    )



if __name__ == '__main__':
    # Connexion can only receive 2 params
    application = connexion.App(__name__, specification_dir='swagger/')
    

    application = connexion.App(__name__, specification_dir='swagger/')

    #app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    application.add_api('my_super_app.yaml', resolver=RestyResolver('api'))

    FlaskInjector(app=application.app, modules=[configure])
    application.run(port=int(os.environ.get('PORT', 2025)))
