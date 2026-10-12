# XML Formatters - Lab Guide & AI Prompting Templates

This folder contains XML data formatting and transformation files using **CSS** and **XSLT**.

---

## 📁 Files Overview

- [`books.xml`](books.xml): Well-formed XML document storing catalog data with stylesheet linking.
- [`books.css`](books.css): CSS rules to style raw XML elements for direct browser rendering.
- [`books.xsl`](books.xsl): XSLT stylesheet transforming XML data into a structured HTML table.

---

## 🎯 AI Prompt Templates (Same Size & Format)

Use these simple, uniform templates to generate files for any lab or exam question. Each prompt follows the **exact same 5-line structure**.

### 1. XML File Prompt
```text
Role: Generate a well-formed XML file named [FILENAME].xml.
Domain: [TOPIC] with root tag <[ROOT]> containing 3 <[ITEM]> entries.
Fields: Each <[ITEM]> has child elements: <[FIELD_1]>, <[FIELD_2]>, <[FIELD_3]>.
Stylesheet: Link stylesheet using <?xml-stylesheet type="text/[css|xsl]" href="[FILENAME].[css|xsl]"?>.
Format: Output only clean, valid XML code with realistic sample data.
```

### 2. CSS File Prompt
```text
Role: Generate a clean CSS file named [FILENAME].css.
Domain: Style raw XML tags for [TOPIC] directly in the browser.
Rules: Set [ROOT] to display:block; style [ITEM] as border cards with padding.
Fields: Style child elements [FIELD_1], [FIELD_2], and [FIELD_3] with distinct colors/weights.
Format: Output only valid CSS rules targeting tag names without HTML wrappers.
```

### 3. XSLT File Prompt
```text
Role: Generate an XSLT transformation file named [FILENAME].xsl.
Domain: Transform [TOPIC] XML data into an HTML table.
Rules: Root template matches "/" and outputs an HTML table with borders and styling.
Fields: Table headers for [FIELD_1], [FIELD_2], [FIELD_3]; loop with <xsl:for-each select="[ROOT]/[ITEM]">.
Format: Output only valid XSLT 1.0 code using <xsl:value-of> for data extraction.
```

### 4. All-in-One Prompt (Generate All 3 Files Together)
```text
Role: Generate [FILENAME].xml, [FILENAME].css, and [FILENAME].xsl files.
Domain: [TOPIC] with root <[ROOT]> and 3 <[ITEM]> entries.
Fields: Each item contains <[FIELD_1]>, <[FIELD_2]>, <[FIELD_3]>.
Specs: Link [FILENAME].xsl in XML, provide card styling in CSS, and table transformation in XSLT.
Format: Output each file in a separate code block ready to save.
```

---

## 🔄 How to Change Based on Any Question

To adapt the prompts for any exam question, simply replace the placeholders:

1. **`[FILENAME]`**: Name of your file (e.g., `books`, `students`, `employees`).
2. **`[TOPIC]`**: Topic description (e.g., `Book Inventory`, `Student Record`, `Employee Directory`).
3. **`[ROOT]`**: Outermost XML wrapper tag (e.g., `catalog`, `students`, `company`).
4. **`[ITEM]`**: Repeating entity tag (e.g., `book`, `student`, `employee`).
5. **`[FIELD_1], [FIELD_2], [FIELD_3]`**: Specific attributes or child tags requested in the question.

### 📋 Quick Question Mapping Table

| Question Topic | `[FILENAME]` | `[ROOT]` | `[ITEM]` | Fields (`[FIELD_1]`, `[FIELD_2]`, `[FIELD_3]`) |
| :--- | :--- | :--- | :--- | :--- |
| **Book Catalog (Current)** | `books` | `catalog` | `book` | `title`, `author`, `price` |
| **Student Marks** | `students` | `college` | `student` | `name`, `rollno`, `department` |
| **Employee Payroll** | `employees` | `company` | `employee` | `name`, `designation`, `salary` |
| **Product Inventory** | `products` | `inventory`| `product` | `name`, `category`, `price` |
| **Hospital Patients** | `patients` | `hospital` | `patient` | `name`, `age`, `disease` |

---

## 💡 Example: Changing from Books to Students

### Ready-to-Use Student XML Prompt:
```text
Role: Generate a well-formed XML file named students.xml.
Domain: Student Records with root tag <college> containing 3 <student> entries.
Fields: Each <student> has child elements: <name>, <rollno>, <department>.
Stylesheet: Link stylesheet using <?xml-stylesheet type="text/xsl" href="students.xsl"?>.
Format: Output only clean, valid XML code with realistic sample data.
```

### Ready-to-Use Student CSS Prompt:
```text
Role: Generate a clean CSS file named students.css.
Domain: Style raw XML tags for Student Records directly in the browser.
Rules: Set college to display:block; style student as border cards with padding.
Fields: Style child elements name, rollno, and department with distinct colors/weights.
Format: Output only valid CSS rules targeting tag names without HTML wrappers.
```

### Ready-to-Use Student XSLT Prompt:
```text
Role: Generate an XSLT transformation file named students.xsl.
Domain: Transform Student Records XML data into an HTML table.
Rules: Root template matches "/" and outputs an HTML table with borders and styling.
Fields: Table headers for Name, Roll No, Department; loop with <xsl:for-each select="college/student">.
Format: Output only valid XSLT 1.0 code using <xsl:value-of> for data extraction.
```

---

## ⚙️ Switching Stylesheets in XML

In line 2 of your XML file, toggle the stylesheet type depending on whether you are demonstrating CSS or XSLT:

- **For CSS Rendering:**
  ```xml
  <?xml-stylesheet type="text/css" href="books.css"?>
  ```
- **For XSLT Transformation:**
  ```xml
  <?xml-stylesheet type="text/xsl" href="books.xsl"?>
  ```

---

## 🚀 How to Run in Browser

1. Place both `.xml` and `.css` (or `.xml` and `.xsl`) in the same directory.
2. Open the `.xml` file directly in Microsoft Edge, Chrome, or Firefox.
3. *Note*: In modern Chromium browsers (Chrome/Edge), local file security policies (`CORS`) may require opening via VS Code **Live Server** extension to render XSLT transformations properly.
