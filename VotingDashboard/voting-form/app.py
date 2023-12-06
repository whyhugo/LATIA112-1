from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/') 
def formPage():
    return render_template('form.html')

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        form_data = request.form
        new_data = {
            "gender": form_data['gender'],
            "age":form_data['age'],
            "area": form_data['area'],
            "food":form_data['food']
        }
        params = {}
        url = "http://localhost:3000/records";
        result = requests.post(url, params=params, json=new_data)
        print(result.status_code)
        print(result.content)
        return render_template('form.html', confirm = "上傳成功")
 
if __name__ == "__main__":
    app.run()