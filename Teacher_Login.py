import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

class TeacherLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.set_background("C:/Applications/VCS codes/Attendance_Checker ACP/Icons/Login Icons/Login_Background.jpg")
        
        self.setGeometry(350, 150, 1200, 800)
        
        
        # Create a frame for the login form
        self.loginFrame = QtWidgets.QFrame(self)
        self.loginFrame.setGeometry(400, 100, 400, 600)
        self.loginFrame.setStyleSheet("""
            background: rgba(128,128,128,100);
            border-radius: 20px;
            border: 2px solid white;
        """)

        # Apply shadow effect to the login frame
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)          # Set the blur radius of the shadow
        shadow.setXOffset(0)              # Set horizontal offset of the shadow
        shadow.setYOffset(5)              # Set vertical offset of the shadow
        shadow.setColor(QtGui.QColor(0, 0, 0, 255))  # Set shadow color (black with some transparency)

        self.loginFrame.setGraphicsEffect(shadow)

        # Close Button (Top right corner)
        closeButton = QtWidgets.QPushButton(self)
        closeButton.setGeometry(1153, 10, 35, 35)
        closeButton.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 17px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 150);
            }
        """)
        close_Button_icon = QtGui.QIcon("C:/Applications/VCS codes/Attendance_Checker ACP/Icons/Login Icons/Close_Icon.png")
        closeButton.setIcon(close_Button_icon)
        closeButton.setIconSize(QtCore.QSize(35, 35))
        closeButton.clicked.connect(self.close)

        # Minimize Button (Top right corner)
        minimizeButton = QtWidgets.QPushButton(self)
        minimizeButton.setGeometry(1112, 10, 35, 35)
        minimizeButton.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 17px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 150);
            }
        """)
        minimize_Button_icon = QtGui.QIcon("C:/Applications/VCS codes/Attendance_Checker ACP/Icons/Login Icons/Minimze_Icon.png")
        minimizeButton.setIcon(minimize_Button_icon)
        minimizeButton.setIconSize(QtCore.QSize(35, 35))
        minimizeButton.clicked.connect(self.showMinimized)

        # Username input field
        self.Username = QtWidgets.QLineEdit(self.loginFrame)
        self.Username.setPlaceholderText("Username or Email")
        self.Username.setGeometry(60, 360, 290, 40)
        self.Username.setFont(QtGui.QFont("Montserrat", 13))
        self.Username.setStyleSheet("""
            QLineEdit {
                padding-left: 10px;
                background: transparent;
                color: rgba(255, 255, 255);
                border: none;
                border-bottom: 2px solid white;
                border-radius: 0px;
            }
        """)

        # Login Button
        self.Login_Button = QtWidgets.QPushButton("Login", self.loginFrame)
        self.Login_Button.setGeometry(70, 410, 130, 30)
        self.Login_Button.setFont(QtGui.QFont("Montserrat", 13))
        self.Login_Button.setStyleSheet("""
            QPushButton {
                font-size: 13px;
                color: white;
                border-radius: 10px;
                border: 1px solid gray;
                background-color: rgba(128, 128, 128, 100);
            }
            QPushButton::hover {
                background-color: rgba(155, 155, 155, 50);
            }
        """)

    def set_background(self, image_path):
        self.background_label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(image_path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 1400, 900)
        self.background_label.setScaledContents(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    Instructors = TeacherLogin()
    Instructors.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
