# MongoDB Atlas Setup Guide
### Cloud Database for AngularJS + Node.js + Express + Mongoose

This guide explains how to switch the backend from a **local MongoDB Community Server** to **MongoDB Atlas** (free cloud database), what code changes are needed, and how to safely push credentials to GitHub.

---

## Table of Contents
1. [Why MongoDB Atlas?](#1-why-mongodb-atlas)
2. [Create a Free Atlas Account & Cluster](#2-create-a-free-atlas-account--cluster)
3. [Configure Network Access & Database User](#3-configure-network-access--database-user)
4. [Get Your Connection String](#4-get-your-connection-string)
5. [Code Changes Required](#5-code-changes-required)
6. [Environment Variable Files Explained](#6-environment-variable-files-explained)
7. [What to Push & What NOT to Push to GitHub](#7-what-to-push--what-not-to-push-to-github)
8. [`.gitignore` Setup](#8-gitignore-setup)
9. [Running Locally with Atlas](#9-running-locally-with-atlas)
10. [Switching Between Atlas & Local MongoDB](#10-switching-between-atlas--local-mongodb)
11. [Common Errors & Fixes](#11-common-errors--fixes)

---

## 1. Why MongoDB Atlas?

| Feature | Local MongoDB | MongoDB Atlas |
| :--- | :--- | :--- |
| Installation required | Yes (Windows service) | No |
| Works offline | Yes | Needs internet |
| Free tier | Free | Free (512 MB) |
| Accessible from any machine | No | Yes |
| Safe to share connection string | (local, no password) | No — use `.env` |

> **Rule of thumb:** Use **local MongoDB** in lab (no internet). Use **Atlas** when deploying or sharing via GitHub.

---

## 2. Create a Free Atlas Account & Cluster

1. Go to https://www.mongodb.com/cloud/atlas/register
2. Sign up with Google or email — it's **100% free**.
3. After login, click **"Build a Database"**.
4. Choose **M0 Free Tier** → Select a region close to you (e.g., `AWS / ap-south-1` for India).
5. Name your cluster (e.g., `web-lab-cluster`) → Click **Create**.

> Atlas takes ~1–3 minutes to provision the cluster.

---

## 3. Configure Network Access & Database User

### Step A: Add a Database User
1. In the Atlas sidebar, click **Database Access** → **Add New Database User**.
2. Choose **Password** authentication.
3. Enter a username (e.g., `sanjay`) and a strong password.
4. Under **Built-in Role**, select **"Read and Write to any database"**.
5. Click **Add User**.

### Step B: Allow Network Access (IP Whitelist)
1. In the sidebar, click **Network Access** → **Add IP Address**.
2. For development/testing, click **"Allow Access from Anywhere"** → `0.0.0.0/0`.
3. Click **Confirm**.

> For production, restrict this to your actual IP address.

---

## 4. Get Your Connection String

1. Go to **Database** → click **Connect** on your cluster.
2. Choose **"Drivers"**.
3. Select **Driver: Node.js**, **Version: 5.5 or later**.
4. Copy the connection string — it looks like:

```
mongodb+srv://sanjay:<password>@web-lab-cluster.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

5. Replace `<password>` with your actual password.
6. Append your database name before `?`:

```
mongodb+srv://sanjay:yourpassword@web-lab-cluster.xxxxx.mongodb.net/web_lab?retryWrites=true&w=majority
```

> **Save this string — you will put it in your `.env` file.**

---

## 5. Code Changes Required

### 5.1 Install `dotenv` Package

```bash
cd backend
npm install dotenv
```

### 5.2 Key Changes to `server.js`

```diff
+ require("dotenv").config();
+
+ const MONGO_URI = process.env.MONGO_URI || "mongodb://127.0.0.1:27017/web_lab";
+ const PORT = process.env.PORT || 5000;

- mongoose.connect("mongodb://127.0.0.1:27017/web_lab")
+ mongoose.connect(MONGO_URI)

- app.listen(5000, () => { console.log("Server running at http://localhost:5000"); });
+ app.listen(PORT, () => { console.log(`Server running at http://localhost:${PORT}`); });
```

### 5.3 Updated `package.json` — add dotenv

```json
{
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.19.2",
    "mongoose": "^8.3.1",
    "dotenv": "^16.4.5"
  }
}
```

---

## 6. Environment Variable Files Explained

### `.env` — your real file (NEVER push to GitHub)

```env
MONGO_URI=mongodb+srv://sanjay:yourpassword@web-lab-cluster.xxxxx.mongodb.net/web_lab?retryWrites=true&w=majority
PORT=5000
```

### `.env.example` — safe template (push to GitHub)

```env
# Copy this to .env and fill in real values. Never commit .env!

# OPTION A: MongoDB Atlas
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/web_lab?retryWrites=true&w=majority

# OPTION B: Local MongoDB (uncomment to use)
# MONGO_URI=mongodb://127.0.0.1:27017/web_lab

PORT=5000
```

---

## 7. What to Push & What NOT to Push to GitHub

| File | Push to GitHub? | Reason |
| :--- | :--- | :--- |
| `server.js` | YES | No credentials — reads from env |
| `package.json` | YES | Lists dependencies |
| `.env.example` | YES | Safe template with placeholder values |
| `.gitignore` | YES | Prevents secrets from being committed |
| `node_modules/` | NO | Too large; `npm install` recreates it |
| `.env` | **NEVER** | Contains real password / connection string |

---

## 8. `.gitignore` Setup

Create `backend/.gitignore` (or root `.gitignore`):

```gitignore
# Dependencies
node_modules/

# Environment secrets
.env

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*
```

---

## 9. Running Locally with Atlas

```bash
# 1. Install all dependencies (including dotenv)
cd backend
npm install

# 2. Copy the example env file and fill in real values
copy .env.example .env

# 3. Start the server
node server.js
```

Expected output:
```
MongoDB Connected: Atlas (Cloud)
Server running at http://localhost:5000
```

---

## 10. Switching Between Atlas & Local MongoDB

Edit `backend/.env` — no code changes required:

```env
# Use Atlas:
MONGO_URI=mongodb+srv://sanjay:password@cluster.mongodb.net/web_lab?retryWrites=true&w=majority

# Use Local (comment out Atlas, uncomment this):
# MONGO_URI=mongodb://127.0.0.1:27017/web_lab
```

Restart `node server.js` after editing.

---

## 11. Common Errors & Fixes

| Error | Cause | Fix |
| :--- | :--- | :--- |
| `MongoServerError: bad auth` | Wrong username/password in URI | Check Atlas → Database Access |
| `MongooseServerSelectionError` | IP not whitelisted | Atlas → Network Access → Add `0.0.0.0/0` |
| `Cannot find module 'dotenv'` | dotenv not installed | Run `npm install dotenv` |
| `MONGO_URI is undefined` | `.env` missing | Create `backend/.env` from `.env.example` |
| `MongoParseError` | URI still has `<password>` placeholder | Replace with actual password |
| Atlas connected but no data | Wrong database name in URI | Ensure URI ends with `/web_lab?` |

---

## Quick Reference Checklist

- [ ] Atlas cluster created (M0 Free Tier)
- [ ] Database user created with read/write access
- [ ] Network Access → `0.0.0.0/0` added
- [ ] Connection string copied with `/web_lab?` appended
- [ ] `dotenv` installed: `npm install dotenv`
- [ ] `server.js` uses `require("dotenv").config()` and `process.env.MONGO_URI`
- [ ] `backend/.env` created with real Atlas URI (NOT committed)
- [ ] `backend/.env.example` committed with placeholder values
- [ ] `.gitignore` includes `.env` and `node_modules/`
- [ ] `node server.js` prints `MongoDB Connected: Atlas (Cloud)`
