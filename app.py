import os
from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
import connexion
from services.RedisProvider import RedisProvider

# Connexion can only receive 2 params
application = connexion.App(__name__, specification_dir='swagger/')

#Setup with Swagger and RestyResolver
application.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
def configure(binder: Binder) -> Binder:
    binder.bind(
        RedisProvider,
        RedisProvider([{"Name": "Test 1"}])
    )
#FlaskInjector Setup defined after configure
FlaskInjector(app=application.app, modules=[configure])

if __name__ == '__main__':
    
    #Redefine application as a connexion app. 
    application = connexion.App(__name__, specification_dir='swagger/')
    #Start the flask server on either a predefined port from the host machine or 2025
    application.run(port=int(os.environ.get('PORT', 2025)))
