import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from Teacher_Login import TeacherLogin  # Ensure TeacherLogin class is implemented and correctly imported


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(500, 500)
        
        # Center the window on the screen
        self.setGeometry(650, 270, 500, 500)
       


        # Set up the background
        self.set_background("C:/Applications/VCS codes/Attendance_Checker ACP/Icons/Login Icons/Login_Background.jpg")

        # Create buttons
        self.create_buttons()
        

    def create_buttons(self):
        # Student Button
        self.student_button = QtWidgets.QPushButton("Student", self)
        self.student_button.setGeometry(100, 250, 300, 50)
        self.student_button.setFont(QtGui.QFont("Montserrat", 13))
        self.student_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: 2px solid white;
                border-radius: 25px;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.student_button.clicked.connect(self.student_login)  # Connect button to method

        # Instructor Button
        self.instructor_button = QtWidgets.QPushButton("Instructors", self)
        self.instructor_button.setGeometry(100, 320, 300, 50)
        self.instructor_button.setFont(QtGui.QFont("Montserrat", 13))
        self.instructor_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: 2px solid white;
                border-radius: 25px;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.instructor_button.clicked.connect(self.Teacher_Login)  # Connect to Teacher Login
        
        # Close Button (Top right corner)
        closeButton = QtWidgets.QPushButton(self)
        closeButton.setGeometry(460, 10, 35, 35)  # Adjusted to fit within the fixed window size
        closeButton.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 17px;  /* Half of the width/height for a circle */
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 150);
            }
        """)
        close_Button_icon = QtGui.QIcon("C:/Applications/VCS codes/Attendance_Checker ACP/Icons/Login Icons/Close_Icon.png")
        closeButton.setIcon(close_Button_icon)
        closeButton.setIconSize(QtCore.QSize(35, 35))
        closeButton.clicked.connect(self.close)

        # Minimize Button (Top right corner, next to close button)
        minimizeButton = QtWidgets.QPushButton(self)
        minimizeButton.setGeometry(420, 10, 35, 35)  # Adjusted to fit within the fixed window size
        minimizeButton.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 17px;  /* Half of the width/height for a circle */
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 150);
            }
        """)
        minimize_Button_icon = QtGui.QIcon("C:/Applications/VCS codes/Attendance_Checker ACP/Icons/Login Icons/Minimze_Icon.png")
        minimizeButton.setIcon(minimize_Button_icon)
        minimizeButton.setIconSize(QtCore.QSize(35, 35))
        minimizeButton.clicked.connect(self.showMinimized)

        
    def student_login(self):
        """Placeholder for student login action."""
        QtWidgets.QMessageBox.information(self, "Student Login", "Student login functionality goes here.")

    def Teacher_Login(self):
        """Show the teacher login window."""
        self.teacher_login_window = TeacherLogin()
        self.teacher_login_window.show()
        self.hide()

    def set_background(self, image_path):
        """Set the window background image."""
        self.background_label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(image_path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setScaledContents(True)
        self.background_label.lower()  # Ensure the background is behind all widgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
