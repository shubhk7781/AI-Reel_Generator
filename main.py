from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import uuid, os
import time
from generate_reel import generate_reel

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["POST", "GET"])
def create():
    my_uuid = uuid.uuid1()
    if request.method == "POST":
        rec_id = request.form.get("uuid")
        des = request.form.get("text")
        input_files = []
        # Ensure directory exists before processing files or description
        upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        for key, value in request.files.items():
            #upload the file
            file = request.files[key]
            if file:# and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_dir, filename))
            input_files.append(file.filename)
        
        #storing the description in the database (here local file)
        with open(os.path.join(upload_dir, "description.txt"), "w") as f:
            f.write(des)
        
        for inf in input_files:
            with open (os.path.join(upload_dir, "input.txt"), "a") as f:
                f.write(f"file '{inf}'\nduration 1\n")
        
        #generate the reel
        generate_reel()
 
    return render_template("create.html", my_uuid=my_uuid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    return render_template("gallery.html", reels=reels)

app.run(debug=True, port=9000)