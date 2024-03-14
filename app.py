from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/portfolio/<project_number>")
def project(project_number):
    return render_template(f"portfolio/{project_number}.html")


@app.route('/halytskyi_cv')
def download_cv():
    return send_file('static/my_files/Halytskyi_cv.pdf', mimetype='application/pdf')


@app.route('/German_B2')
def german():
    return send_file('static/my_files/Certificate_B2.pdf', mimetype='application/pdf')


@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with open('form_data.txt', 'a', encoding='utf-8') as file:
            file.write(f'Name: {name}, Email: {email}, Message: {message}\n')
        file.close()

        return render_template("index.html")



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(debug=True)