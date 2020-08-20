from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<page_name>')
def page_name(page_name):
    return render_template(page_name)

def write(data):
    with open ('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def writeCSV(data):
    with open ('database2.csv', mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:    
            data = request.form.to_dict()
            writeCSV(data)
            return redirect ('/thanks.html')
        except:
            return "OOPS SOMETHING WENT WRONG TRY AGAIN OR DO IT AFTER SOME TIME!!"   
    else:
        return "something went wrong!"