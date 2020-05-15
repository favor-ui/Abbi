import os

basedir = os.path.abspath(os.path.dirname(__file__))


# creating a configuration class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abi-you-can'\

    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://dbabi:dbabialways@cluster0-k3ewb.mongodb.net/abi?retryWrites=true&w=majority'


    
