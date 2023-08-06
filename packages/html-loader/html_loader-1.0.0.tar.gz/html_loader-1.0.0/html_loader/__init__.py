import os.path
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *
from PyQt5 import QtGui
from threading import Thread

# jsfunction = pyqtSlot

# class CallHandler(QObject):
#     def __init__(self, parent=None):
#         super().__init__(parent)
    
#     @jsfunction()
#     def text(self):
#         print("test")

class LoaderHTML:
    def __init__(self, name: str="Document", icon: str | None=None, width: int=700, heigth: int=700):
        self.app = QApplication([])
        self.app.setApplicationName(name)

        if icon:
            self.app.setWindowIcon(QtGui.QIcon(icon))

        self.window_ = QMainWindow()
        self.window_.setGeometry(0, 0, width, heigth)
        self.window_.browser = QWebEngineView()

        self.window_.setCentralWidget(self.window_.browser)
        self.window_.show()

    def Thread(self, fun):
        Thread(target=fun).start()

    def load_html(self, code: str):
        self.window_.browser.setHtml(code)
    
    def load_from_url(self, url: str):
        self.window_.browser.setUrl(QUrl(url))

    def load_file(self, name: str):
        self.path = "file:///%s" % (os.path.join(os.getcwd(), name).replace('\\','/'))
        self.window_.browser.setUrl(QUrl(self.path))

    def load_file_absolute_path(self, path: str):
        self.path = "file:///%s" % (path.replace('\\', '/'))
        self.window_.browser.setUrl(QUrl(self.path))

    # def web_channel(self,handler=CallHandler):
    #     channel = QWebChannel()
    #     channel.registerObject('handler', handler())

    #     self.window_.browser.page().setWebChannel(channel)

    def run(self):
        self.app.exec_()
