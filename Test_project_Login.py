import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QApplication, QMessageBox
from Professor_Login import ProfessorLogin

class TestProfessorLogin(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_check_login_success(self, mock_connect):
        # Create QApplication before creating the login window (necessary for PyQt widgets)
        app = QApplication([])  # Create the QApplication object

        # Mocking the database connection
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        
        # Simulate the cursor fetching a result
        mock_cursor.fetchone.return_value = ("Melvin", "Roxas")
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        # Create the login window instance
        login_window = ProfessorLogin()

        # Set mock user input
        login_window.Username.setText('Melvin Roxas')  # Simulate username input
        login_window.password.setText('00000001')  # Simulate password input
        
        # Trigger the login check
        login_window.check_login()

        # Check if the main menu is shown after a successful login
        # Assumption: The main_menu is instantiated in check_login method
        self.assertTrue(login_window.main_menu.isVisible())  # Assuming main_menu is set correctly in the method

    @patch('mysql.connector.connect')
    @patch.object(QMessageBox, 'warning')  # Mock the QMessageBox.warning method
    def test_check_login_failure(self, mock_warning, mock_connect):
        # Create QApplication before creating the login window (necessary for PyQt widgets)
        app = QApplication([])  # Create the QApplication object

        # Mocking the database connection
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        
        # Simulate no result found in the database
        mock_cursor.fetchone.return_value = None
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        # Create the login window instance
        login_window = ProfessorLogin()

        # Set mock user input
        login_window.Username.setText('incorrect user')  # Simulate incorrect username
        login_window.password.setText('wrongpassword')  # Simulate incorrect password

        # Trigger the login check
        login_window.check_login()

        # Check if the error message box was shown (indicating login failure)
        self.assertEqual(mock_connection.is_connected.called, True)
        mock_connect.assert_called_with(
            host='localhost',
            database='attendance_checker',
            user='root',
            password=''
        )

        # Assert the warning message box was triggered
        mock_warning.assert_called_once_with(
            login_window, "Login Failed", "Invalid username/email or password!"
        )

if __name__ == "__main__":
    unittest.main()
