import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Splitter")

        # Create a web view to display Flask app
        self.web_view = QWebEngineView()
        self.setGeometry(350,200,1280,720)
        self.setCentralWidget(self.web_view)

        # Start Flask server
        self.start_flask_server()

        # Load the Flask app
        self.load_flask_app()

    def start_flask_server(self):
        # Activate virtual environment and start Flask server
        venv_activate_cmd = r".\Envsplitter\Scripts\activate"
        flask_script_cmd = r"py .\pdfsplitter.py"
        cmd = f"{venv_activate_cmd} && {flask_script_cmd}"
        self.flask_process = subprocess.Popen(cmd, shell=True)

    def load_flask_app(self):
        # Load the Flask app in the web view
        self.web_view.load(QUrl("http://localhost:8080"))

    def closeEvent(self, event):
        # Terminate Flask server when the window is closed
        self.flask_process.terminate()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
