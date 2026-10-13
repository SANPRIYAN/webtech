# Backend Setup & Run Guide

## Table of Contents
1. [Download & Install Required Software](#1-download--install-required-software)
2. [MongoDB Community Server Setup (Windows)](#2-mongodb-community-server-setup-windows)
3. [MongoDB Compass Setup](#3-mongodb-compass-setup)
4. [Navigate to Backend Folder](#4-navigate-to-backend-folder)
5. [Install Node Dependencies](#5-install-node-dependencies)
6. [Configure Database Connection](#6-configure-database-connection)
7. [Start the Server](#7-start-the-server)
8. [API Endpoints](#8-api-endpoints)
9. [Common Errors & Fixes](#9-common-errors--fixes)

---

## 1. Download & Install Required Software

| Software | Purpose | Download Link |
| :--- | :--- | :--- |
| **Node.js (LTS)** | JavaScript runtime for backend | [nodejs.org/en/download](https://nodejs.org/en/download) |
| **MongoDB Community Server** | Local database engine | [mongodb.com/try/download/community](https://www.mongodb.com/try/download/community) |
| **MongoDB Compass** | GUI to view/manage local database | [mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass) |

> MongoDB Compass is optional but recommended to visually inspect your data.

---

## 2. MongoDB Community Server Setup (Windows)

### Step 1 — Download & Install

1. Go to [mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
2. Select:
   - **Version**: Latest (e.g. 7.x or 8.x)
   - **Platform**: Windows
   - **Package**: MSI
3. Click **Download** and run the `.msi` installer.
4. Choose **Complete** setup type.
5. On the **Service Configuration** screen:
   - ✅ Check **"Install MongoD as a Service"**
   - Select **"Run service as Network Service user"**
   - Service Name: `MongoDB`
   - Leave Data and Log directories as default
6. **Uncheck "Install MongoDB Compass"** (we install it separately below).
7. Click **Install** → **Finish**.

### Step 2 — Verify MongoDB Service is Running

Open **Command Prompt as Administrator** (`Win` → type `cmd` → right-click → **Run as administrator**):

```cmd
sc query MongoDB
```

Expected output:
```
STATE : 4  RUNNING
```

If stopped, start it:
```cmd
net start MongoDB
```

If you get **error 1060** (service not found):
```cmd
"C:\Program Files\MongoDB\Server\<version>\bin\mongod.exe" --dbpath="C:\data\db"
```

---

## 3. MongoDB Compass Setup

### Step 1 — Download & Install

1. Go to [mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass)
2. Select:
   - **Version**: Latest stable
   - **Platform**: Windows (64-bit)
   - **Package**: EXE
3. Click **Download** and run the installer — it installs automatically.

### Step 2 — Connect to Local MongoDB

1. Open **MongoDB Compass**.
2. In the connection bar, enter:
   ```
   mongodb://127.0.0.1:27017
   ```
3. Click **Connect**.
4. You will see your databases listed on the left.

> The `web_lab` database and `records` collection are created automatically when the first record is inserted via the app — no manual creation needed.

### Step 3 — Verify Data (After Running the App)

- In Compass: expand `web_lab` → open `records` collection.
- Click **Refresh** to see newly inserted documents.

---

## 4. Navigate to Backend Folder

```bash
cd backend
```

---

## 5. Install Node Dependencies

```bash
npm install
```

> Installs `express`, `mongoose`, `cors`, and `dotenv` from `package.json`.

---

## 6. Configure Database Connection

### Option A — MongoDB Atlas (Cloud)

> Requires an internet connection. No local MongoDB installation needed.

1. Copy the sample env file:

```bash
# Windows
copy .env.example .env

# Mac / Linux
cp .env.example .env
```

2. Open `.env` and replace the placeholder with your real Atlas URI:

```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/web_lab?retryWrites=true&w=majority
PORT=5000
```

> Get the URI from: **Atlas Dashboard → Your Cluster → Connect → Drivers → Node.js**

---

### Option B — MongoDB Compass / Local (No .env needed)

> Requires MongoDB Community Server installed and running (see Section 2).

1. Make sure MongoDB service is running:

```cmd
net start MongoDB
```

2. In `server.js`, **comment out Option A** and **uncomment Option B**:

```js
// const MONGO_URI = "mongodb://127.0.0.1:27017/web_lab";
// const PORT = 5000;   // ← hardcoded, no .env needed for Compass
```

> PORT is hardcoded to `5000`. No `.env` file required.

---

## 7. Start the Server

```bash
node server.js
```

### Expected Output

**Atlas (Option A):**
```
MongoDB Connected: Atlas (Cloud)
Server running at http://localhost:5000
```

**Local / Compass (Option B):**
```
MongoDB Connected: Local (Compass)
Server running at http://localhost:5000
```

To stop the server: press `Ctrl + C`

---

## 8. API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/records` | Fetch all records |
| `POST` | `/api/records` | Create a new record |
| `PUT` | `/api/records/:id` | Update a record by ID |
| `DELETE` | `/api/records/:id` | Delete a record by ID |

---

## 9. Common Errors & Fixes

| Error | Cause | Fix |
| :--- | :--- | :--- |
| `Cannot find module 'express'` | Dependencies not installed | Run `npm install` inside `backend/` |
| `ECONNREFUSED 127.0.0.1:27017` | Local MongoDB not running | Run `net start MongoDB` as Admin |
| `FAILED 1060` from `sc query` | Service not registered | Reinstall Community Server with service option checked |
| `MongoServerError: bad auth` | Wrong Atlas credentials | Check username/password in `.env` |
| `MongooseServerSelectionError` | Atlas IP not whitelisted | Atlas → Network Access → Add `0.0.0.0/0` |
| `Cannot find module 'dotenv'` | dotenv not installed | Run `npm install dotenv` |
| `MONGO_URI is undefined` | `.env` file missing | Run `copy .env.example .env` and fill in URI |
| Port 5000 already in use | Another process using port | Change `PORT=5001` in `.env` and restart |
