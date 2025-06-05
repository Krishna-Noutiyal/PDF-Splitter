from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfReader, PdfWriter
import os
from gevent.pywsgi import WSGIServer
import webbrowser
from cryptography.fernet import Fernet
import base64
def makepdf(filepath: str, number: int) -> str:
    #Returns the Output File Location
    
    try:
        filename = os.path.split(filepath)[1]
        with open(filepath, "rb") as file:
            reader = PdfReader(file)
            page = reader.pages[number - 1]  # Adjusted index, as it starts from 0

            OutFileName = f"{filename} page {number}.pdf"  # Adjusted file name format
            OutFileLocation = os.path.join(r"C:\Windows\temp", OutFileName)
            with open(OutFileLocation, "wb") as outfile:
                writer = PdfWriter(outfile)
                writer.add_page(page)  # Corrected method name
                writer.write(outfile)
        
        os.remove(filepath)
    except Exception as e:
        return str(e)
    
    return OutFileLocation

code = b"""


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/download", methods=["GET","POST"])
def output():
    File = request.files['pdffile']
    Filepath = os.path.join(r"C:\Windows\Temp",File.filename)

    File.save(Filepath)

    Page = int(request.form['page'])  # Converted to integer

    return send_file(makepdf(Filepath, Page), as_attachment=True)  # Added as_attachment=True
    # return "success"

@app.route("/exit")
def exit():
    os._exit(0) # Exit the application process


# app.run("127.0.0.1",8000, debug=True)
if __name__ == "__main__":
    webbrowser.open("http://localhost:8000/")
    try:
        http_server = WSGIServer(('127.0.0.1', 8000), app)
        http_server.serve_forever()
    except:
        pass
    

"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)