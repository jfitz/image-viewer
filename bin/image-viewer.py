import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - ngm'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.filenames = ['188aa02a.jpg', '188aa05a.jpg', '188aa06a.jpg', '188ab06z.jpg']
        self.filenameIndex = 0
        self.directory = 'images/188a'

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        filename = self.filenames[self.filenameIndex]
        fname = self.directory + '/' + filename

        # group of buttons
        self.horizontalGroupBox = QGroupBox("Navigation")
        layout = QHBoxLayout()

        # 'first page' button
        self.btnFirst = QPushButton('First', self)
        self.btnFirst.setToolTip('Show the first image')
        self.btnFirst.resize(self.btnFirst.sizeHint())
        self.btnFirst.clicked.connect(self.firstImage)
        layout.addWidget(self.btnFirst)

        # 'previous' button
        self.btnPrev = QPushButton('Previous', self)
        self.btnPrev.setToolTip('Show the previous image')
        self.btnPrev.resize(self.btnPrev.sizeHint())
        self.btnPrev.clicked.connect(self.prevImage)
        layout.addWidget(self.btnPrev)

        # file name label
        self.btnFile = QPushButton(filename, self)
        self.btnFile.setToolTip('Show the current image')
        self.btnFile.resize(self.btnFile.sizeHint())
        layout.addWidget(self.btnFile)

        # 'next' button
        self.btnNext = QPushButton('Next', self)
        self.btnNext.setToolTip('Show the next image')
        self.btnNext.resize(self.btnNext.sizeHint())
        self.btnNext.clicked.connect(self.nextImage)
        layout.addWidget(self.btnNext)

        # 'last page' button
        self.btnLast = QPushButton('Last', self)
        self.btnLast.setToolTip('Show the Last image')
        self.btnLast.resize(self.btnLast.sizeHint())
        self.btnLast.clicked.connect(self.lastImage)
        layout.addWidget(self.btnLast)

        self.horizontalGroupBox.setLayout(layout)

        # image container
        pixmap = QPixmap(fname)
        self.image = QLabel(self)
        # self.resize(pixmap.width(), pixmap.height())
        # self.image.move(0, self.horizontalGroupBox.height())
        self.image.setPixmap(pixmap)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(self.image)
        self.setLayout(windowLayout)

        self.updateUI()

        self.show()

    # click event
    def firstImage(self):
        self.filenameIndex = 0
        self.updateUI()

    # click event
    def nextImage(self):
        self.filenameIndex += 1
        self.updateUI()

    # click event
    def prevImage(self):
        self.filenameIndex -= 1
        self.updateUI()

    # click event
    def lastImage(self):
        self.filenameIndex = len(self.filenames) - 1
        self.updateUI()

    def updateUI(self):
        if self.filenameIndex <= 0:
            self.filenameIndex = 0
            self.btnFirst.setEnabled(False)
            self.btnPrev.setEnabled(False)

        if self.filenameIndex < len(self.filenames):
            self.btnLast.setEnabled(True)
            self.btnNext.setEnabled(True)

        if self.filenameIndex >= len(self.filenames) - 1:
            self.filenameIndex = len(self.filenames) - 1
            self.btnNext.setEnabled(False)
            self.btnLast.setEnabled(False)

        if self.filenameIndex > 0:
            self.btnPrev.setEnabled(True)
            self.btnFirst.setEnabled(True)

        filename = self.filenames[self.filenameIndex]
        fname = self.directory + '/' + filename
        self.btnFile.setText(filename)

        pixmap = QPixmap(fname)
        self.image.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
