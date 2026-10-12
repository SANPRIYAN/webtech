# Full-Stack Web Model Lab Setup Guide
### AngularJS + Node.js + Express + Mongoose + MongoDB Community Server

Complete step-by-step setup guide for your Windows lab computer to configure, run, and test the full-stack CRUD application during your practical exam.

---

## 📑 Table of Contents
1. [Architecture Overview](#1-architecture-overview)
2. [Prerequisites & Official Downloads](#2-prerequisites--official-downloads)
3. [MongoDB Community Server Setup (Windows)](#3-mongodb-community-server-setup-windows)
4. [MongoDB Compass Setup (GUI)](#4-mongodb-compass-setup-gui)
5. [Node.js & npm Verification](#5-nodejs--npm-verification)
6. [Backend Setup & Run](#6-backend-setup--run)
7. [Frontend Setup & Run](#7-frontend-setup--run)
8. [Ports & Connection Reference](#8-ports--connection-reference)
9. [Common Errors & Fixes](#9-common-errors--fixes)
10. [Commands to Memorize for Exam](#10-commands-to-memorize-for-exam)
11. [Final Pre-Lab Checklist](#11-final-pre-lab-checklist)
12. [Automated Selenium Testing](#12-automated-selenium-testing)

---

## 1. Architecture Overview

```text
[ Browser: AngularJS Frontend ] 
        │
        │ HTTP (GET, POST, DELETE) via Port 5000
        ▼
[ Node.js + Express.js Backend ] (server.js)
        │
        │ Mongoose ODM via Port 27017
        ▼
[ MongoDB Community Server ] (Local Database: web_lab)
```

- **Mongoose** is an npm package (ODM library), **not** a database server.
- **MongoDB Community Server** is the local database engine that must be installed and running.
- **MongoDB Compass** is an optional GUI tool to visually view databases and collections.

---

## 2. Prerequisites & Official Downloads

| Software | Purpose | Default Port | Official Link |
| :--- | :--- | :--- | :--- |
| **MongoDB Community Server** | Local database engine | `27017` | [Download Community Server (MSI)](https://www.mongodb.com/try/download/community) |
| **MongoDB Compass** | Visual database GUI | Connects to `27017` | [Download MongoDB Compass](https://www.mongodb.com/try/download/compass) |
| **Node.js & npm (LTS)** | Backend JavaScript runtime | — | [Download Node.js](https://nodejs.org/en/download) |
| **AngularJS 1.8.2** | Frontend framework | CDN / Local JS | [AngularJS Official Site](https://angularjs.org/) |

---

## 3. MongoDB Community Server Setup (Windows)

### Step 1: Install MongoDB as a Windows Service
1. Download the **MSI installer** from the official MongoDB page.
2. Run the installer and choose **Complete** setup.
3. On the **Service Configuration** screen:
   - Check **"Install MongoD as a Service"**.
   - Select **"Run service as Network Service user"**.
   - Service Name: `MongoDB`.
   - Data and Log directories: leave as default (`C:\Program Files\MongoDB\Server\<version>\data\`).
4. Finish installation.

### Step 2: Verify and Start MongoDB Service
Open **Command Prompt as Administrator** (Press `Win` → type `cmd` → right click → **Run as administrator**):

```cmd
sc query MongoDB
```

Expected output:
```text
STATE : 4 RUNNING
```

If the service is stopped, start it:
```cmd
net start MongoDB
```

> **⚠️ If you get error `1060` (Service does not exist):**
> 1. Check if `mongod.exe` exists in `C:\Program Files\MongoDB\Server\<version>\bin\mongod.exe`.
> 2. If missing, reinstall Community Server.
> 3. If present, manually run:
>    ```cmd
>    "C:\Program Files\MongoDB\Server\<version>\bin\mongod.exe" --dbpath="C:\data\db"
>    ```

---

## 4. MongoDB Compass Setup (GUI)

1. Open **MongoDB Compass**.
2. In the connection string bar, enter:
   ```text
   mongodb://127.0.0.1:27017
   ```
3. Click **Connect**.
4. You do **not** need to create the database manually — Mongoose automatically creates `web_lab` and the `records` collection when your first record is inserted.

---

## 5. Node.js & npm Verification

Open Command Prompt or PowerShell and verify versions:

```cmd
node -v
npm -v
```

Both commands should display version numbers (e.g., `v20.x` or `v22.x`, and npm `10.x`).

---

## 6. Backend Setup & Run

### Step 1: Navigate to Backend Directory
```cmd
cd backend
```

### Step 2: Install Required Packages
```cmd
npm init -y
npm install express mongoose cors
```

### Step 3: Start the Backend Server
```cmd
node server.js
```

Expected output:
```text
MongoDB Connected
Server running at http://localhost:5000
```

> Keep this terminal open. If you modify `server.js`, restart it with `Ctrl + C` followed by `node server.js`.

---

## 7. Frontend Setup & Run

1. Open `frontend/index.html` directly in your browser (Double-click or drag into Chrome/Edge).
2. Or in **VS Code**: Right-click `index.html` → **Open with Live Server**.
3. Test the operations:
   - **Add**: Enter Name, Department, Age → Click **Add Student**.
   - **View**: Record appears immediately in the table.
   - **Search**: Type in search box to filter rows in real-time.
   - **Delete**: Click **Delete** next to any record.
4. Verify data in **MongoDB Compass**:
   - Refresh databases → open `web_lab` → open collection `records`.

---

## 8. Ports & Connection Reference

| Component | Port / URL | Description |
| :--- | :--- | :--- |
| **MongoDB Server** | `mongodb://127.0.0.1:27017/web_lab` | Database port used by Mongoose and Compass |
| **Express Backend** | `http://localhost:5000/api/records` | REST API endpoints (GET, POST, PUT, DELETE) |
| **AngularJS Frontend** | `file:///...` or `http://127.0.0.1:5500` | Browser UI interacting with port 5000 |

---

## 9. Common Errors & Fixes

| Error | Root Cause | Quick Solution |
| :--- | :--- | :--- |
| `ECONNREFUSED 127.0.0.1:27017` | MongoDB Server is not running | Run `net start MongoDB` as Administrator. |
| `FAILED 1060` from `sc query` | Windows service is not registered | Reinstall MongoDB Community Server with service option checked. |
| `Cannot find module 'mongoose'` | Packages not installed | Run `npm install express mongoose cors` in the `backend` folder. |
| `Cannot find module 'express'` | Run from wrong folder | Make sure terminal path is inside `backend/`. |
| `ERR_CONNECTION_REFUSED` on port 5000 | Backend server not running | Run `node server.js` and ensure it displays `Server running`. |
| AngularJS CDN blocked / offline | No internet in lab | Download `angular.min.js` and use local path: `<script src="angular.min.js"></script>`. |
| Port 5000 already in use | Previous process lingering | Change `app.listen(5000)` to `5001` in `server.js` and update `API` URL in `index.html`. |

---

## 10. Commands to Memorize for Exam

```cmd
:: 1. Check software versions
node -v
npm -v

:: 2. Check MongoDB Service status
sc query MongoDB

:: 3. Start MongoDB Service (if stopped)
net start MongoDB

:: 4. Backend installation (inside backend folder)
npm init -y
npm install express mongoose cors

:: 5. Start Backend Server
node server.js
```

---

## 11. Final Pre-Lab Checklist

- [ ] MongoDB Community Server installed and service running (`STATE : 4 RUNNING`)
- [ ] MongoDB Compass connects to `mongodb://127.0.0.1:27017`
- [ ] Node.js and npm verified via terminal
- [ ] Backend dependencies installed (`express`, `mongoose`, `cors`)
- [ ] `node server.js` displays `MongoDB Connected` and `Server running at http://localhost:5000`
- [ ] `frontend/index.html` loads and successfully adds, reads, and deletes records
- [ ] Inserted records verified inside Compass under `web_lab.records`
- [ ] Selenium tests pass via `python selenium_test.py` and screenshots saved

---

## 12. Automated Selenium Testing

A complete automated Selenium test suite is included in [`selenium_test.py`](selenium_test.py).
For instructions on how to run tests and adapt the script to any exam question, see the [Selenium Testing Guide](SELENIUM_GUIDE.md).

```cmd
:: Install Selenium dependencies
pip install selenium webdriver-manager

:: Run test suite (with node server.js running)
python selenium_test.py
```
