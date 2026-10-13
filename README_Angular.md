# Angular + Node.js + MongoDB – Model Lab Commands

For **Windows PowerShell (VS Code)**.

---

## 1. Angular Frontend

```powershell
npm install -g @angular/cli
ng new frontend
cd frontend
npm install
ng serve
```

Open: <http://localhost:4200>

---

## 2. Node.js + MongoDB Backend

Open a **new terminal** in the main project folder:

```powershell
mkdir backend
cd backend
npm init -y
npm install express mongoose cors
npm pkg set scripts.start="node server.js"
npm start
```

---

## 3. MongoDB

Open **PowerShell as Administrator** (if installed as a Windows service):

```powershell
net start MongoDB
```

Open **another terminal**:

```powershell
mongosh
```

Inside the MongoDB shell:

```js
show dbs
use modellab
show collections
db.books.find()
```

> Replace `modellab` and `books` with your actual database and collection names.

---

## 4. Useful Angular Commands

| Command | Purpose |
|---|---|
| `ng new frontend` | Create Angular project |
| `ng serve` | Run Angular application |
| `ng serve --open` | Run and open browser |
| `ng generate component home` | Create component |
| `ng generate service api` | Create service |
| `npm install` | Install dependencies |
| `Ctrl + C` | Stop application |
