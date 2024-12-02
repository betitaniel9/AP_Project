import sys
import mysql.connector
import random  # Import the random module
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from datetime import datetime

class ProfessorMainMenu(QtWidgets.QMainWindow):
    def __init__(self, professor_name):
        super().__init__()
        self.professor_name = professor_name  # Store the professor's name
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 1920, 1080)
        self.set_background("C:\\Applications\\VCS codes\\Attendance_Checker ACP\\Icons\\Login Icons\\MAIN_MENU_BG.png")
        self.add_top_bar(professor_name)
        self.create_buttons()
        self.table_widget = None
        self.attendance_table = None  # Initialize attendance table

    def set_background(self, image_path):
        self.background_label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(image_path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setScaledContents(True)

    def add_top_bar(self, professor_name):
        self.top_bar = QtWidgets.QFrame(self)
        self.top_bar.setGeometry(0, 0, self.width(), 80)
        self.top_bar.setStyleSheet("background-color: rgba(0, 0, 0, 80);")
    
        self.professor_label = QtWidgets.QLabel(f"Welcome, {professor_name}", self.top_bar)
        self.professor_label.setGeometry(20, 10, 400, 60)
        self.professor_label.setFont(QtGui.QFont("Montserrat", 20))
        self.professor_label.setStyleSheet("color: white;")
    
        # ComboBox for Block Selection
        self.block_combobox = QtWidgets.QComboBox(self.top_bar)
        self.block_combobox.setGeometry(450, 15, 200, 40)
        self.block_combobox.setFont(QtGui.QFont("Montserrat", 12))
        self.block_combobox.setStyleSheet("""
            QComboBox {
                background-color: rgba(255, 255, 255, 150);
                color: black;
                border: 1px solid white;
                border-radius: 10px;
                padding-left: 10px;
            }
        """)
        self.block_combobox.addItems(["All Blocks", "2101", "2102", "2103", "2104", "2105", "2106"])
        self.block_combobox.currentIndexChanged.connect(self.filter_by_block)
    
        # Logout Button
        self.logout_button = QtWidgets.QPushButton("Logout", self.top_bar)
        self.logout_button.setGeometry(self.width() - 100, 15, 80, 30)
        self.logout_button.setFont(QtGui.QFont("Montserrat", 12))
        self.logout_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 150);
                color: white;
                border: 1px solid white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: rgba(255, 0, 0, 200);
            }
        """)
        self.logout_button.clicked.connect(self.logout)
    
    def filter_by_block(self):
        """Filter both the attendance and students tables based on the selected block."""
        selected_block = self.block_combobox.currentText()
        
        # Filter attendance table
        if self.attendance_table is not None:
            for row_idx in range(self.attendance_table.rowCount()):
                block_item = self.attendance_table.item(row_idx, 3)  # Get the Block column
                if block_item:
                    block_text = block_item.text()
                    self.attendance_table.setRowHidden(
                        row_idx, 
                        selected_block != "All Blocks" and block_text != selected_block
                    )

        # Filter students table
        if self.table_widget is not None:
            for row_idx in range(self.table_widget.rowCount()):
                block_item = self.table_widget.item(row_idx, 4)  # Get the Block column
                if block_item:
                    block_text = block_item.text()
                    self.table_widget.setRowHidden(
                        row_idx, 
                        selected_block != "All Blocks" and block_text != selected_block
                    )

    def create_buttons(self):
        button_style = """
            QPushButton {
                background-color: rgba(255, 255, 255, 50);
                border: 2px solid white;
                border-radius: 20px;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255, 0, 0, 100);
            }
        """

        # View Attendance Button
        self.attendance_button = QtWidgets.QPushButton("View Attendance", self)
        self.attendance_button.setGeometry(15, 100, 500, 200)
        self.attendance_button.setFont(QtGui.QFont("Montserrat", 25))
        self.attendance_button.setStyleSheet(button_style)
        self.attendance_button.clicked.connect(self.view_attendance)

        # Random Select Button
        self.random_select_button = QtWidgets.QPushButton("Random Select Student", self)
        self.random_select_button.setGeometry(15, 320, 500, 200)
        self.random_select_button.setFont(QtGui.QFont("Montserrat", 25))
        self.random_select_button.setStyleSheet(button_style)
        self.random_select_button.clicked.connect(self.random_select_student)

        # Manage Students Button
        self.manage_students_button = QtWidgets.QPushButton("Manage Students", self)
        self.manage_students_button.setGeometry(15, 540, 500, 200)
        self.manage_students_button.setFont(QtGui.QFont("Montserrat", 25))
        self.manage_students_button.setStyleSheet(button_style)
        self.manage_students_button.clicked.connect(self.manage_students)



        # Exit Button
        self.exit_button = QtWidgets.QPushButton("Exit", self)
        self.exit_button.setGeometry(15, 760, 500, 200)
        self.exit_button.setFont(QtGui.QFont("Montserrat", 25))
        self.exit_button.setStyleSheet(button_style)
        self.exit_button.clicked.connect(self.close)

    def view_attendance(self):
        """Fetch and display attendance records."""
        if self.table_widget is not None:
            self.table_widget.hide()  # Hide the manage students table if it exists
    
        if self.attendance_table is None:
            self.attendance_table = QtWidgets.QTableWidget(self)
            self.attendance_table.setGeometry(560, 100, 1360, 900)  # Positioning the table
            self.attendance_table.setColumnCount(5)
            self.attendance_table.setHorizontalHeaderLabels(["Student Name", "Date", "Attendance", "Block", "Professor Name"])
    
            header_font = QtGui.QFont("Montserrat", 20, QtGui.QFont.Bold)
            self.attendance_table.horizontalHeader().setFont(header_font)
            self.attendance_table.horizontalHeader().setStyleSheet("background-color: lightgray;")
    
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="attendance_checker"
            )
            cursor = connection.cursor()
            query = """
                SELECT CONCAT(s.first_name, ' ', s.last_name) AS student_name, 
                    a.date, 
                    a.attendance, 
                    a.block, 
                    a.professor_name 
                FROM attendance a
                JOIN student_list s ON a.student_id = s.srcode
            """
            cursor.execute(query)
            records = cursor.fetchall()
    
            self.attendance_table.setRowCount(len(records))
            for row_idx, row_data in enumerate(records):
                for col_idx, value in enumerate(row_data):
                    self.attendance_table.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(value)))
    
        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

        # Table customization
        self.attendance_table.setColumnWidth(0, 260)  # Student Name
        self.attendance_table.setColumnWidth(1, 260)  # Date
        self.attendance_table.setColumnWidth(2, 260)  # Attendance
        self.attendance_table.setColumnWidth(3, 260)  # Block
        self.attendance_table.setColumnWidth(4, 260)  # Professor Name
        self.attendance_table.verticalHeader().setDefaultSectionSize(40)  # Set row height

    # Enable sorting
        self.attendance_table.setSortingEnabled(True)
    
        self.attendance_table.show()  # Show the attendance table # Show the attendance table
    
    def random_select_student(self):
        """Randomly select a student from the attendance table."""
        if self.attendance_table is not None:
            row_count = self.attendance_table.rowCount()
            if row_count > 0:
                random_row = random.randint(0, row_count - 1)
                # Highlight the randomly selected row
                for row in range(row_count):
                    if row == random_row:
                        self.attendance_table.selectRow(row)
                    else:
                        self.attendance_table.setRowHidden(row, False)  # Ensure other rows are visible
            else:
                QtWidgets.QMessageBox.information(self, "No Students", "No students available to select.")
        else:
            QtWidgets.QMessageBox.warning(self, "No Attendance Data", "Please view attendance first.")

    def manage_students(self):
        if self.attendance_table is not None:
            self.attendance_table.hide()  # Hide the attendance table if it exists

        if self.table_widget is None:
            self.table_widget = QtWidgets.QTableWidget(self)
            self.table_widget.setGeometry(560, 100, 1360, 900)  # Positioning the table
            self.table_widget.setColumnCount(8)  # Updated column count after removing Status
            self.table_widget.setHorizontalHeaderLabels(["SRCODE", "First Name", "Last Name", "Course", "Block", "Attendance", "Mark", "Professor Name"])

            header_font = QtGui.QFont("Montserrat", 14, QtGui.QFont.Bold)
            self.table_widget.horizontalHeader().setFont(header_font)
            self.table_widget.horizontalHeader().setStyleSheet("background-color: lightgray;")

            # Fetch data from the MySQL database
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="attendance_checker"
                )
                cursor = connection.cursor()
                query = "SELECT srcode, first_name, last_name, course, block, attendance FROM student_list"
                cursor.execute(query)
                rows = cursor.fetchall()

                # Populate the table
                self.table_widget.setRowCount(len(rows))
                for row_idx, row_data in enumerate(rows):
                    for col_idx, value in enumerate(row_data):
                        self.table_widget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(value)))  # Keeping original order

                    # Set color based on attendance status
                    status = row_data[5]  # Assuming the attendance status is the 6th column
                    if status == "Present":
                        self.table_widget.item(row_idx, 5).setBackground(QtGui.QColor(0, 255, 0))  # Green for Present
                    elif status == "Absent":
                        self.table_widget.item(row_idx, 5).setBackground(QtGui.QColor(255, 0, 0))  # Red for Absent
                    elif status == "Late":
                        self.table_widget.item(row_idx, 5).setBackground(QtGui.QColor(255, 255, 0))  # Yellow for Late

                    # Create Mark button
                    mark_button = QtWidgets.QPushButton("Mark", self.table_widget)
                    mark_button.clicked.connect(lambda checked, idx=row_idx: self.mark_attendance(idx))
                    self.table_widget.setCellWidget(row_idx, 6, mark_button)  # Add button to the last column

                    # Set professor name in the last column
                    self.table_widget.setItem(row_idx, 7, QtWidgets.QTableWidgetItem(self.professor_name))  # Add professor name

            except mysql.connector.Error as e:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            finally:
                if 'connection' in locals() and connection.is_connected():
                    connection.close()

        # Table customization
        self.table_widget.setColumnWidth(0, 170)  # SRCODE
        self.table_widget.setColumnWidth(1, 170)  # First Name
        self.table_widget.setColumnWidth(2, 170)  # Last Name
        self.table_widget.setColumnWidth(3, 170)  # Course
        self.table_widget.setColumnWidth(4, 170)  # Block
        self.table_widget.setColumnWidth(5, 170)  # Attendance
        self.table_widget.setColumnWidth(6, 100)  # Mark button
        self.table_widget.setColumnWidth(7, 190)  # Professor Name
        self.table_widget.verticalHeader().setDefaultSectionSize(60)  # Set row height

        # Enable sorting
        self.table_widget.setSortingEnabled(True)

        # Show the table
        self.table_widget.show()
    def mark_attendance(self, row_idx):
        """Prompt user to select attendance status."""
        status, ok = QtWidgets.QInputDialog.getItem(self, "Mark Attendance", "Select Status:", ["Present", "Late", "Absent"], 0, False)
        if ok and status:
            # Update the attendance status in the table
            self.table_widget.item(row_idx, 5).setText(status)  # Update the status in the table
            if status == "Present":
                self.table_widget.item(row_idx, 5).setBackground(QtGui.QColor(0, 255, 0))  # Green for Present
            elif status == "Absent":
                self.table_widget.item(row_idx, 5).setBackground(QtGui.QColor(255, 0, 0))  # Red for Absent
            elif status == "Late":
                self.table_widget.item(row_idx, 5).setBackground(QtGui.QColor(255, 255, 0))  # Yellow for Late

            # Get the current date
            current_date = datetime.now().strftime("%Y-%m-%d")

            # Update the database with the new status
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="attendance_checker"
                )
                cursor = connection.cursor()
                srcode = self.table_widget.item(row_idx, 0).text()  # Get SRCODE from the first column
                block = self.table_widget.item(row_idx, 4).text()  # Get Block from the fifth column
                insert_query = "INSERT INTO attendance (student_id, date, attendance, block, professor_name) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (srcode, current_date, status, block, self.professor_name))
                connection.commit()
            except mysql.connector.Error as e:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            finally:
                if 'connection' in locals() and connection.is_connected():
                    connection.close()

    def generate_reports(self):
        """Placeholder for generating reports."""
        QtWidgets.QMessageBox.information(self, "Generate Reports", "Generate Reports feature coming soon!")

    def logout(self):
        """Logout and return to the login window."""
        QtWidgets.QMessageBox.information(self, "Logout", "You have been logged out.")
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    professor_name = "John Doe"  # Replace with any name you'd like to display
    main_menu = ProfessorMainMenu(professor_name)
    main_menu.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()