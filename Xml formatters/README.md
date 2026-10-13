# XML Formatters (CSS & XSLT)

This folder contains:
- `books.xml` — XML data file
- `books.css` — CSS styling for raw XML
- `books.xsl` — XSLT stylesheet (renders HTML table)

---

## 🚀 How to Run

1. Keep all 3 files in the same folder.
2. In `books.xml` (line 2), choose which formatter to view:
   - **For CSS**: `<?xml-stylesheet type="text/css" href="books.css"?>`
   - **For XSLT**: `<?xml-stylesheet type="text/xsl" href="books.xsl"?>`
3. Open `books.xml` in browser (or right-click → **Open with Live Server** in VS Code).

---

## 🤖 Single Prompt for All 3 Files

Copy and paste this single prompt to generate all three files at once:

```text
Generate 3 files: [NAME].xml, [NAME].css, and [NAME].xsl for [TOPIC].
- Root tag <[ROOT]> containing 3 <[ITEM]> records.
- Each <[ITEM]> has child tags: <[FIELD1]>, <[FIELD2]>, <[FIELD3]>.
- [NAME].xml: Link [NAME].xsl using <?xml-stylesheet?>.
- [NAME].css: Style elements with block display, borders, padding, and font styles.
- [NAME].xsl: Transform XML into a styled HTML table using <xsl:for-each>.
Give only valid code for all 3 files in separate code blocks.
```

---

## ✏️ How to Change Based on Question

Just replace the placeholders in the prompt:

| Question | `[NAME]` | `[TOPIC]` | `[ROOT]` | `[ITEM]` | Fields (`[FIELD1]`, `[FIELD2]`, `[FIELD3]`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Books** | `books` | Book Store | `catalog` | `book` | `title`, `author`, `price` |
| **Students** | `students` | Student Info | `college` | `student` | `name`, `rollno`, `dept` |
| **Employees** | `employees` | Employee List | `company` | `employee` | `name`, `designation`, `salary` |
| **Products** | `products` | Product Store | `inventory` | `product` | `name`, `category`, `price` |
