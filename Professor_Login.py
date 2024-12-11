import sys
import mysql.connector
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

#Calls or inherits the Main Menu Class
from Professor_Main_Frame import ProfessorMainMenu

class ProfessorLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.set_background("C:\VSC files(codes)\Attendance_Checker ACP\Icons\Login Icons\Teacher_Login_Pic.png")
        self.setGeometry(350, 150, 1200, 800)

        # Create a frame for the login form
        self.loginFrame = QtWidgets.QFrame(self)
        self.loginFrame.setGeometry(400, 100, 400, 600)
        self.loginFrame.setStyleSheet("""
            background: rgba(128,128,128,100);
            border-radius: 20px;
            border: 2px solid red;
        """)

        self.logo = QtWidgets.QLabel(self.loginFrame)
        self.logo.setGeometry(105, 50, 200, 200)  # Adjust the size and position as needed

        logo_pixmap = QtGui.QPixmap("C:\VSC files(codes)\Attendance_Checker ACP\Icons\Login Icons\BSU_Logo.png")
        self.logo.setPixmap(logo_pixmap)
        self.logo.setScaledContents(True)

        # Ensure no border or styling is applied to the logo label
        self.logo.setStyleSheet("""
            QLabel {
                border: none;
                background: transparent;
            }
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
        close_Button_icon = QtGui.QIcon("C:\VSC files(codes)\Attendance_Checker ACP\Icons\Login Icons\Close_Icon.png")
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
        minimize_Button_icon = QtGui.QIcon("C:\VSC files(codes)\Attendance_Checker ACP\Icons\Login Icons\Minimze_Icon.png")
        minimizeButton.setIcon(minimize_Button_icon)
        minimizeButton.setIconSize(QtCore.QSize(35, 35))
        minimizeButton.clicked.connect(self.showMinimized)

        # Name input field
        self.Username = QtWidgets.QLineEdit(self.loginFrame)
        self.Username.setPlaceholderText("Name or Email")
        self.Username.setGeometry(60, 330, 290, 40)
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

        # Password input field
        self.password = QtWidgets.QLineEdit(self.loginFrame)
        self.password.setPlaceholderText ("Password")
        self.password.setGeometry(60, 380, 290, 40)
        self.password.setFont(QtGui.QFont("Montserrat", 13))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet("""
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
        self.Login_Button.setGeometry(130, 440, 130, 40)
        self.Login_Button.setFont(QtGui.QFont("Montserrat", 13))
        self.Login_Button.setStyleSheet("""
            QPushButton {
                font-size: 13px;
                color: white;
                border-radius: 10px;
                border: 1px solid White;
                background-color: rgba(128, 128, 128, 150);
            }
            QPushButton::hover {
                background-color: rgba(255, 0, 0, 50);
                border-radius: 10px;
                border: 1px solid White;
            }
        """)

        self.Login_Button.clicked.connect(self.check_login)

        # Add text at the bottom of the loginFrame
        self.bottomText = QtWidgets.QLabel("(this is for Project Purposes only)", self.loginFrame)
        self.bottomText.setGeometry(60, 520, 290, 40)  # Adjust position as needed
        self.bottomText.setFont(QtGui.QFont("Montserrat", 10))  # Adjust font size
        self.bottomText.setAlignment(QtCore.Qt.AlignCenter)  # Center the text
        self.bottomText.setStyleSheet("""
            QLabel {
                color: white;
                border: none;
                background: transparent;
            }
        """)

    def set_background(self, image_path):
        self.background_label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(image_path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 1400, 900)
        self.background_label.setScaledContents(True)

    def check_login(self):
        username = self.Username.text().strip()  # Remove leading/trailing spaces
        input_password = self.password.text().strip()  # Remove leading/trailing spaces

    # Validation checks
        if not username or not input_password:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Username and password cannot be empty!")
            return

        if not self.is_valid_username(username):
            QtWidgets.QMessageBox.warning(self, "Input Error", "Username must contain only letters and spaces!")
            return

    # Debug: Print input values
        print(f"Username: {username}, Password: {input_password}")

        try:
        # Connect to the MySQL database
            connection = mysql.connector.connect(
                host='localhost',
                database='attendance_checker',
                user='root',  # Replace with your MySQL username
                password=''  # Replace with your MySQL password
            )

            if connection.is_connected():
                cursor = connection.cursor()

            # If the username contains a space (full name), split it into first and last name
                if ' ' in username:
                    first_name, last_name = username.split(' ', 1)  # Split only into first and last name
                    query = """
                    SELECT first_name, last_name FROM professor_list 
                    WHERE 
                        LOWER(first_name) = %s AND LOWER(last_name) = %s 
                        AND password = %s
                    """
                    cursor.execute(query, (first_name, last_name, input_password))
                else:
                    # Otherwise, assume the username is either email or a single name
                    query = """
                    SELECT first_name, last_name FROM professor_list 
                    WHERE 
                        (LOWER(first_name) = %s AND LOWER(last_name) = %s) 
                        OR LOWER(email) = %s 
                    AND password = %s
                    """
                    cursor.execute(query, (username, username, username, input_password))

                result = cursor.fetchone()

                if result:
                    first_name, last_name = result  # Fetch first_name and last_name
                    name = f"{first_name} {last_name}"  # Combine first and last name
                    self.main_menu = ProfessorMainMenu(name)  # Pass the professor's name to the main menu
                    self.main_menu.show()  # Show the main menu
                    self.close()  # Close the login window
                else:
                # If no match was found
                    QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username/email or password!")

        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred while connecting to the database: {str(e)}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def is_valid_username(self, username):
        return all(c.isalpha() or c.isspace() for c in username)


    

    

def main():
    app = QtWidgets.QApplication(sys.argv)
    Instructors = ProfessorLogin()
    Instructors.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()