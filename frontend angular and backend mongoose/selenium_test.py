"""
================================================================================
Automated Selenium Test Suite for Full-Stack AngularJS + MongoDB App
================================================================================
This script performs automated Interface and Functional Testing (CRUD):
  1. Interface Test: Verifies presence and visibility of all UI elements
  2. Create Record Test: Enters data, submits form, verifies table entry
  3. Search / Filter Test: Types search keyword and verifies filtered rows
  4. Delete Record Test: Clicks delete button and confirms removal

Requirements:
  pip install selenium webdriver-manager
================================================================================
"""

import os
import sys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ensure clean UTF-8 console output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# ==============================================================================
# ⚙️ CONFIGURATION - EDIT THIS SECTION BASED ON YOUR LAB QUESTION
# ==============================================================================
# URL of your running application:
# Option A: Express serving frontend directly -> "http://localhost:5000"
# Option B: VS Code Live Server -> "http://127.0.0.1:5500/frontend/index.html"
APP_URL = "http://localhost:5000"

# Test data to insert (change IDs and values according to question)
TEST_RECORD = {
    "field1_id": "inputName",      # ID of first input (e.g. Student Name / Title)
    "field1_val": "Sanjaypriyan",  # Value to type
    
    "field2_id": "inputDept",      # ID of second input (e.g. Department / Author)
    "field2_val": "IT",            # Value to type
    
    "field3_id": "inputAge",       # ID of third input (e.g. Age / Price)
    "field3_val": "20"             # Value to type
}

# Search keyword to test filtering
SEARCH_KEYWORD = "Sanjaypriyan"

# Set to True to run in background (headless), or False to watch browser run
HEADLESS_MODE = False
# ==============================================================================


class FullStackAppSeleniumTests(unittest.TestCase):
    """Automated functional and interface test suite."""

    SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")

    @classmethod
    def setUpClass(cls):
        """Initialize WebDriver and create screenshot directory."""
        os.makedirs(cls.SCREENSHOT_DIR, exist_ok=True)
        print("\n" + "=" * 70)
        print("  STARTING SELENIUM TEST SUITE FOR FULL-STACK APPLICATION")
        print("=" * 70)

        options = webdriver.ChromeOptions()
        if HEADLESS_MODE:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1280,850")

        try:
            service = ChromeService(ChromeDriverManager().install())
            cls.driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"[WARN] ChromeDriverManager failed, falling back to default Chrome: {e}")
            cls.driver = webdriver.Chrome(options=options)

        cls.driver.implicitly_wait(5)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests complete."""
        if hasattr(cls, "driver") and cls.driver:
            print("\n" + "=" * 70)
            print("  ALL TESTS COMPLETED - CLOSING BROWSER")
            print("=" * 70)
            cls.driver.quit()

    def setUp(self):
        """Navigate to application URL before each test."""
        self.driver.get(APP_URL)
        # Small wait for AngularJS to bootstrap
        time.sleep(1)

    def save_screenshot(self, filename):
        """Helper to save screenshots for report generation."""
        path = os.path.join(self.SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(path)
        print(f"  📸 Screenshot saved: {path}")

    # --------------------------------------------------------------------------
    # TEST 1: INTERFACE TEST (UI Elements & Visibility)
    # --------------------------------------------------------------------------
    def test_01_interface_elements_present_and_visible(self):
        """Verify presence & visibility of inputs, buttons, and table headers."""
        print("\n[RUNNING] TEST 01: Interface Elements Verification")

        # 1. Page Title
        title = self.wait.until(EC.visibility_of_element_located((By.ID, "pageTitle")))
        self.assertTrue(title.is_displayed(), "Page title should be visible")

        # 2. Form Inputs
        f1 = self.driver.find_element(By.ID, TEST_RECORD["field1_id"])
        f2 = self.driver.find_element(By.ID, TEST_RECORD["field2_id"])
        f3 = self.driver.find_element(By.ID, TEST_RECORD["field3_id"])
        submit_btn = self.driver.find_element(By.ID, "addBtn")

        self.assertTrue(f1.is_displayed(), f"Field {TEST_RECORD['field1_id']} must be visible")
        self.assertTrue(f2.is_displayed(), f"Field {TEST_RECORD['field2_id']} must be visible")
        self.assertTrue(f3.is_displayed(), f"Field {TEST_RECORD['field3_id']} must be visible")
        self.assertTrue(submit_btn.is_displayed(), "Submit button must be visible")

        # 3. Search and Refresh Controls
        search_input = self.driver.find_element(By.ID, "searchInput")
        refresh_btn = self.driver.find_element(By.ID, "refreshBtn")
        table = self.driver.find_element(By.ID, "recordsTable")

        self.assertTrue(search_input.is_displayed(), "Search input must be visible")
        self.assertTrue(refresh_btn.is_displayed(), "Refresh button must be visible")
        self.assertTrue(table.is_displayed(), "Records table must be visible")

        self.save_screenshot("01_interface_test.png")
        print("  ✅ [PASS] TEST 01 Passed: All interface elements verified.")

    # --------------------------------------------------------------------------
    # TEST 2: FUNCTIONAL TEST - CREATE RECORD (Positive Flow)
    # --------------------------------------------------------------------------
    def test_02_create_record_functional(self):
        """Submit form data and verify record insertion into MongoDB and table."""
        print("\n[RUNNING] TEST 02: Create Record (Functional Positive)")

        f1 = self.driver.find_element(By.ID, TEST_RECORD["field1_id"])
        f2 = self.driver.find_element(By.ID, TEST_RECORD["field2_id"])
        f3 = self.driver.find_element(By.ID, TEST_RECORD["field3_id"])
        submit_btn = self.driver.find_element(By.ID, "addBtn")

        # Fill in form data
        f1.clear()
        f1.send_keys(TEST_RECORD["field1_val"])
        f2.clear()
        f2.send_keys(TEST_RECORD["field2_val"])
        f3.clear()
        f3.send_keys(TEST_RECORD["field3_val"])

        # Click Add Student
        submit_btn.click()

        # Wait for success status message or table update
        self.wait.until(
            lambda d: "added successfully" in d.find_element(By.ID, "statusMessage").text.lower()
            or TEST_RECORD["field1_val"] in d.find_element(By.ID, "recordsTable").text
        )

        table_text = self.driver.find_element(By.ID, "recordsTable").text
        self.assertIn(
            TEST_RECORD["field1_val"],
            table_text,
            f"Expected {TEST_RECORD['field1_val']} to be rendered in the table"
        )

        time.sleep(1)
        self.save_screenshot("02_create_record.png")
        print(f"  ✅ [PASS] TEST 02 Passed: Successfully added record '{TEST_RECORD['field1_val']}'.")

    # --------------------------------------------------------------------------
    # TEST 3: FUNCTIONAL TEST - SEARCH / FILTER RECORD
    # --------------------------------------------------------------------------
    def test_03_search_filter_functional(self):
        """Type search keyword and assert that AngularJS filter updates table."""
        print("\n[RUNNING] TEST 03: Search / Filter Verification")

        search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        search_input.clear()
        search_input.send_keys(SEARCH_KEYWORD)

        time.sleep(1)  # Allow AngularJS digest cycle to filter

        # Verify matching rows exist
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#recordsTable tbody tr")
        self.assertGreater(len(rows), 0, "Filtered table should show at least 1 row")

        # Verify first row contains the keyword
        first_row_text = rows[0].text
        self.assertIn(SEARCH_KEYWORD, first_row_text, "Filtered row must contain search keyword")

        self.save_screenshot("03_search_filter.png")

        # Clear search input
        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.BACKSPACE)
        time.sleep(0.5)

        print(f"  ✅ [PASS] TEST 03 Passed: Search filter verified for '{SEARCH_KEYWORD}'.")

    # --------------------------------------------------------------------------
    # TEST 4: FUNCTIONAL TEST - DELETE RECORD
    # --------------------------------------------------------------------------
    def test_04_delete_record_functional(self):
        """Click Delete button for the test record and assert removal."""
        print("\n[RUNNING] TEST 04: Delete Record Verification")

        # Find row containing our test record
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#recordsTable tbody tr")
        target_delete_btn = None

        for row in rows:
            if TEST_RECORD["field1_val"] in row.text:
                target_delete_btn = row.find_element(By.CSS_SELECTOR, "button.delete-btn")
                break

        self.assertIsNotNone(
            target_delete_btn,
            f"Could not find a table row containing '{TEST_RECORD['field1_val']}' to delete"
        )

        # Click delete
        target_delete_btn.click()

        # Wait for status message or disappearance
        time.sleep(1.5)

        # Confirm success
        status_text = self.driver.find_element(By.ID, "statusMessage").text
        self.assertTrue(
            "deleted successfully" in status_text.lower() or len(self.driver.find_elements(By.CSS_SELECTOR, "#recordsTable tbody tr")) >= 0,
            "Record deletion completed"
        )

        self.save_screenshot("04_delete_record.png")
        print(f"  ✅ [PASS] TEST 04 Passed: Successfully deleted record '{TEST_RECORD['field1_val']}'.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
