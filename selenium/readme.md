```powershell
cd "D:\web lab\selenium-login"
npm init -y
npm install express mongoose dotenv
python -m pip install selenium
node server.js
python test_login.py



prompt for other application. enter your applicaiton name

Create a very simple Web Lab application for **[APPLICATION NAME]** using AngularJS, Node.js, Express.js, MongoDB Atlas, and Selenium with Python.

Requirements:

1. Create all required project files automatically. Do not ask me to create files manually.
2. Use a very simple single-page HTML frontend with minimal CSS.
3. Include the main form and basic functionality relevant to the application.
   - Hospital Management: patient name, age, department, and submit button.
   - School Management: student name, roll number, class, and submit button.
   - Library Management: book name, student name, and submit button.
   Adapt the form to the application name I provide.
4. Use AngularJS for the frontend, Node.js and Express.js for the backend, and MongoDB Atlas for storing submitted data.
5. Read the MongoDB Atlas URI from an existing `.env` file using `dotenv`. Never overwrite or expose my existing credentials.
6. Create a simple backend API to save form data to MongoDB Atlas and display a success message after submission.
7. Generate a simple Selenium Python test named `test_login.py` that opens Chrome, fills the form, clicks Submit, and verifies the success message.
8. Keep the code short, beginner-friendly, and easy to explain in a viva. Avoid unnecessary CSS, extra files, complex functions, and comments.
9. Automatically install required Node.js and Python packages if needed.
10. Configure the project so I only need to run these commands:
    - `node server.js`
    - `python test_login.py`
11. Keep the frontend at `http://localhost:5000`.
12. Use the same filenames and project structure each time. Make the Selenium test match the generated HTML element IDs and expected message.
13. If a required package is already installed, do not reinstall it unnecessarily.
14. Ensure the code is consistent across all files and can run without manual corrections.
15. Do not modify unrelated files or overwrite my existing `.env` file.

First, ask me for the application name if I have not provided one. Then generate the complete working project files and give me only the essential commands to run it.
```
