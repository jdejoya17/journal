from flask import Flask

from controllers.users import user_routes 

app = Flask(__name__)
app.register_blueprint(user_routes) 

@app.route('/api/v1/welcome')
def welcome(): 
   return 'hello world'

if __name__ == '__main__':
   app.run()