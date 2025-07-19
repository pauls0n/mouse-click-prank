import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QButtonGroup
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from sound_effects import sound_effects
from pynput import mouse

class MouseClickPrank(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Mouse Click Prank")
		self.setWindowIcon(QIcon("logo.ico"))
		self.setGeometry(800, 250, 500, 300)
		self.vbox = QVBoxLayout()
		self.player = QMediaPlayer()

		self.title = QLabel("Mouse Click Prank", self)
		self.description = QLabel("This widget makes the computer play a sound effect of your choosing every time you click your mouse", self)
		self.help = QLabel("Choose the sound effect:", self)

		self.vbox.addWidget(self.title)
		self.vbox.addWidget(self.description)
		self.vbox.addWidget(self.help)
		self.radio_group = QButtonGroup()

		for text in sound_effects.keys():
			self.radio_button = QRadioButton(text, self)
			self.vbox.addWidget(self.radio_button)
			self.radio_button.setCursor(QCursor(Qt.PointingHandCursor))
			self.radio_button.setToolTip("Click to preview")
			self.radio_group.addButton(self.radio_button)

		self.listener = mouse.Listener(on_click=self.playSound)
		self.listener.start()
		self.radio_group.buttonToggled.connect(lambda: self.playSound(pressed=True))
		self.initUI()

	def playSound(self, x=0, y=0, button=0, pressed=False):
		if self.radio_group.checkedId() != -1 and pressed:
			file_name = sound_effects[self.radio_group.checkedButton().text()]
			path = f"sounds/{file_name}"
			url = QUrl.fromLocalFile(path)
			content = QMediaContent(url)
			self.player.stop()
			self.player.setMedia(content)
			self.player.play()
			print(file_name)

	def initUI(self):
		self.setLayout(self.vbox)

		self.vbox.setSpacing(25)
		self.vbox.setContentsMargins(20, 30, 20, 50)

		self.title.setObjectName("title")
		self.description.setObjectName("description")
		self.help.setObjectName("help")

		self.title.setAlignment(Qt.AlignHCenter)
		self.description.setAlignment(Qt.AlignHCenter)
		self.description.setWordWrap(True)

		self.setStyleSheet("""
										 
									QWidget {
										font-family: "Segoe UI Variable Text";
										font-size: 20px;
									}
										 
									QLabel#title {
										font-size: 30px;
										font-weight: bold;
									}
										 
									QLabel#description {
										font-size: 20px;
									}
										 
									QRadioButton {
										margin-left: 30px;	 
									}			
									
									
									""")
	
def main():
	app = QApplication(sys.argv)
	widget = MouseClickPrank()
	widget.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()