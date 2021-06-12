from flask import *
import pdfSplitter

app=Flask(__name__)


@app.route("/")
def upload():
    return render_template('file_upload.html')

@app.route("/success",methods=["POST"])
def success():
    global start,end,file
    start=int(request.form['start'])
    end=int(request.form['end'])
    f=request.files['file']
    file=f.filename
    f.save(file)
    return render_template('success.html',start=start,end=end,name=file)



@app.route("/convert")
def cropper():
    pdfSplitter.cropper(start,end,file)

    return render_template('download.html')



@app.route("/download")
def download():
    filename=file.split(".")[0]+"_cropped_.pdf"

    return send_file(filename,as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
