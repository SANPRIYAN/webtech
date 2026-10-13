# Backend Setup & Run Guide

## Prerequisites
- [Node.js (LTS)](https://nodejs.org/en/download) installed
- MongoDB running (Atlas **or** local — see below)

---

## Step 1 — Navigate to Backend Folder

```bash
cd backend
```

---

## Step 2 — Install Dependencies

```bash
npm install
```

> Installs `express`, `mongoose`, `cors`, and `dotenv` from `package.json`.

---

## Step 3 — Configure Database Connection

### Option A — MongoDB Atlas (Cloud)

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

> Get the URI from: **Atlas → Your Cluster → Connect → Drivers → Node.js**

---

### Option B — MongoDB Compass / Local (No .env needed)

1. Start the MongoDB Windows service (run CMD as Administrator):

```cmd
net start MongoDB
```

2. In `server.js`, comment out **Option A** and uncomment **Option B**:

```js
// const MONGO_URI = "mongodb://127.0.0.1:27017/web_lab";
// const PORT = 5000;   // ← hardcoded, no .env needed for Compass
```

> PORT is hardcoded to `5000`. No `.env` file required.

---

## Step 4 — Start the Server

```bash
node server.js
```

### Expected Output

**Atlas:**
```
MongoDB Connected: Atlas (Cloud)
Server running at http://localhost:5000
```

**Local / Compass:**
```
MongoDB Connected: Local (Compass)
Server running at http://localhost:5000
```

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/records` | Fetch all records |
| `POST` | `/api/records` | Create a new record |
| `PUT` | `/api/records/:id` | Update a record by ID |
| `DELETE` | `/api/records/:id` | Delete a record by ID |

---

## Common Errors & Fixes

| Error | Cause | Fix |
| :--- | :--- | :--- |
| `Cannot find module 'express'` | Dependencies not installed | Run `npm install` inside `backend/` |
| `ECONNREFUSED 127.0.0.1:27017` | Local MongoDB not running | Run `net start MongoDB` as Admin |
| `MongoServerError: bad auth` | Wrong Atlas credentials | Check username/password in `.env` |
| `MongooseServerSelectionError` | Atlas IP not whitelisted | Atlas → Network Access → Add `0.0.0.0/0` |
| `Cannot find module 'dotenv'` | dotenv not installed | Run `npm install dotenv` |
| `MONGO_URI is undefined` | `.env` file missing | Run `copy .env.example .env` and fill in URI |
| Port 5000 already in use | Another process using port | Change `PORT=5001` in `.env` and restart |

---

## Stop the Server

Press `Ctrl + C` in the terminal.
