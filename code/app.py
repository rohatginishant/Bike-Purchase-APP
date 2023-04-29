from flask import Flask,render_template,request,url_for,redirect
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.jinja2')

# @app.route('/post')
# def post():
        
    
@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        email =  request.form.get('email')
        bike_id = request.form.get('bike_id')
        color = request.form.get('color')
        
        api_endpoint = 'https://3upaasuxt3.execute-api.ap-northeast-1.amazonaws.com/test/userdetails'
        
        data = {'name':name, 'email':email, 'bike_id':bike_id,'color':color}
        
        response = requests.post(api_endpoint, json = data)
        print(response)
        
        return render_template('success.jinja2',data=data)
    return render_template('form.jinja2')
        
    
if __name__ == '__main__':
    app.run(debug=True)
    
    