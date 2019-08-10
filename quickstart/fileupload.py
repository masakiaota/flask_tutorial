from flask import request, Flask
app= Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    return 'file upload'

# fileuploadできないが

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
