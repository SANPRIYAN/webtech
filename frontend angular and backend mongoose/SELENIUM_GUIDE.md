# Automated Selenium Testing Guide
### Full-Stack App: AngularJS + Express + Mongoose + Selenium WebDriver

This guide explains how to run the automated Selenium test suite (`selenium_test.py`) alongside your full-stack application and how to adapt it to **any question** asked during your lab exam.

---

## 📋 What the Selenium Test Suite Does

The test script automatically launches a browser and executes 4 test cases:
1. **TEST-01 (Interface Test)**: Confirms presence and visibility of Page Title, Form Inputs, Submit Button, Search Bar, and Data Table.
2. **TEST-02 (Functional - Create)**: Automatically enters test data, clicks **Add Student**, and asserts that the new record appears in the table.
3. **TEST-03 (Functional - Search)**: Types a keyword in the search bar and verifies that the AngularJS filter updates the table rows in real-time.
4. **TEST-04 (Functional - Delete)**: Locates the test record, clicks **Delete**, and confirms removal.
5. **📸 Automated Screenshots**: Automatically saves proof screenshots to `./screenshots/` (`01_interface_test.png`, `02_create_record.png`, etc.) for your lab record/report.

---

## ⚙️ Step 1: Install Python Requirements

Open Command Prompt or PowerShell:

```bash
pip install selenium webdriver-manager
```

> `webdriver-manager` automatically downloads and configures the exact driver matching your installed Google Chrome version.

---

## 🚀 Step 2: Run the Full Stack App and Selenium (3 Terminals)

### Terminal 1: Verify & Start MongoDB
```cmd
net start MongoDB
```

### Terminal 2: Start the Full-Stack Backend
Navigate to the `backend` folder and start the server:

```cmd
cd backend
node server.js
```

You should see:
```text
MongoDB Connected
Server running at http://localhost:5000
```
> **Note**: `server.js` serves both the Express REST API (`/api/records`) and the AngularJS frontend at `http://localhost:5000`.

### Terminal 3: Run Selenium Automated Tests
In the `frontend angular and backend mongoose` folder:

```cmd
python selenium_test.py
```

The browser will open, perform the actions automatically, print test results, and close.

---

## 🔄 How to Change Based on Any Question

If your exam question changes from **Student Management** to **Books**, **Employees**, or **Products**, make these 2 quick changes:

### Change 1: In `frontend/index.html` (Form Inputs & Table)
Update the input IDs and placeholders to match your new fields:

```html
<!-- Example for Book Inventory: -->
<input type="text" id="inputName" ng-model="formData.title" placeholder="Book Title" required>
<input type="text" id="inputDept" ng-model="formData.author" placeholder="Author" required>
<input type="number" id="inputAge" ng-model="formData.price" placeholder="Price" required>
```

### Change 2: At the Top of `selenium_test.py` (Configuration Section)
Open `selenium_test.py` and modify the top configuration dictionary:

```python
# ==============================================================================
# ⚙️ CONFIGURATION - EDIT THIS SECTION BASED ON YOUR LAB QUESTION
# ==============================================================================
APP_URL = "http://localhost:5000"

TEST_RECORD = {
    "field1_id": "inputName",      # ID of first input
    "field1_val": "Web Tech",      # Test value to type (e.g. Title)
    
    "field2_id": "inputDept",      # ID of second input
    "field2_val": "Godbole",       # Test value to type (e.g. Author)
    
    "field3_id": "inputAge",       # ID of third input
    "field3_val": "650"            # Test value to type (e.g. Price)
}

SEARCH_KEYWORD = "Web Tech"        # Keyword to test search filter
HEADLESS_MODE = False              # Set to True for background, False to watch live
# ==============================================================================
```

---

## 📋 Question Substitution Cheat Sheet

| Question Domain | `field1_id` & Sample Value | `field2_id` & Sample Value | `field3_id` & Sample Value | `SEARCH_KEYWORD` |
| :--- | :--- | :--- | :--- | :--- |
| **Students (Current)** | `"inputName"`: `"Sanjaypriyan"` | `"inputDept"`: `"IT"` | `"inputAge"`: `"20"` | `"Sanjaypriyan"` |
| **Book Inventory** | `"inputName"`: `"Web Technologies"` | `"inputDept"`: `"Godbole"` | `"inputAge"`: `"650"` | `"Web Technologies"` |
| **Employee Payroll** | `"inputName"`: `"John Doe"` | `"inputDept"`: `"Developer"` | `"inputAge"`: `"75000"` | `"John Doe"` |
| **Product Store** | `"inputName"`: `"Wireless Mouse"` | `"inputDept"`: `"Electronics"` | `"inputAge"`: `"499"` | `"Wireless Mouse"` |
| **Hospital Patients**| `"inputName"`: `"Ravi Kumar"` | `"inputDept"`: `"Cardiology"` | `"inputAge"`: `"45"` | `"Ravi Kumar"` |

---

## 🖥️ Expected Console Output

When you run `python selenium_test.py`:

```text
======================================================================
  STARTING SELENIUM TEST SUITE FOR FULL-STACK APPLICATION
======================================================================

[RUNNING] TEST 01: Interface Elements Verification
  📸 Screenshot saved: ...\screenshots\01_interface_test.png
  ✅ [PASS] TEST 01 Passed: All interface elements verified.

[RUNNING] TEST 02: Create Record (Functional Positive)
  📸 Screenshot saved: ...\screenshots\02_create_record.png
  ✅ [PASS] TEST 02 Passed: Successfully added record 'Sanjaypriyan'.

[RUNNING] TEST 03: Search / Filter Verification
  📸 Screenshot saved: ...\screenshots\03_search_filter.png
  ✅ [PASS] TEST 03 Passed: Search filter verified for 'Sanjaypriyan'.

[RUNNING] TEST 04: Delete Record Verification
  📸 Screenshot saved: ...\screenshots\04_delete_record.png
  ✅ [PASS] TEST 04 Passed: Successfully deleted record 'Sanjaypriyan'.

======================================================================
  ALL TESTS COMPLETED - CLOSING BROWSER
======================================================================
----------------------------------------------------------------------
Ran 4 tests in 8.420s

OK
```

---

## 🛠️ Common Errors & Quick Solutions

| Error | Cause | Quick Fix |
| :--- | :--- | :--- |
| `ERR_CONNECTION_REFUSED` on port 5000 | Backend not running | Start backend with `node server.js` before running Selenium. |
| `NoSuchElementException` | Element ID mismatch | Check if the ID in `index.html` matches `field1_id` in `selenium_test.py`. |
| `SessionNotCreatedException` | Browser / Driver version mismatch | Run `pip install --upgrade webdriver-manager`. |
| Chrome not installed in lab | College uses Microsoft Edge | In `selenium_test.py`, replace `webdriver.Chrome()` with `webdriver.Edge()`. |
| Records not saving | MongoDB service stopped | Run `net start MongoDB` as Administrator. |
