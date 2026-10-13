const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

// ═══════════════════════════════════════════════════════════════
//  OPTION A — MongoDB Atlas (Cloud)  ← ACTIVE
//  Requires: .env file with MONGO_URI set to your Atlas URI
//  Steps:
//    1. npm install dotenv
//    2. Create backend/.env and add:
//       MONGO_URI=mongodb+srv://<user>:<pass>@<cluster>.mongodb.net/web_lab?retryWrites=true&w=majority
//    3. node server.js
// ═══════════════════════════════════════════════════════════════
require("dotenv").config();
const MONGO_URI = process.env.MONGO_URI;
const PORT = process.env.PORT || 5000;

mongoose
  .connect(MONGO_URI)
  .then(() => {
    console.log("MongoDB Connected: Atlas (Cloud)");
  })
  .catch((err) => {
    console.log("MongoDB Connection Error:", err.message);
  });

// ───────────────────────────────────────────────────────────────
//  OPTION B — MongoDB Compass / Local  ← COMMENTED OUT
//  No .env file needed. Just make sure MongoDB service is running.
//  To use: comment out OPTION A above and uncomment lines below.
//  Steps:
//    1. Start MongoDB service: net start MongoDB
//    2. node server.js
// ───────────────────────────────────────────────────────────────
// const MONGO_URI = "mongodb://127.0.0.1:27017/web_lab";
// const PORT = 5000;
//
// mongoose
//   .connect(MONGO_URI)
//   .then(() => {
//     console.log("MongoDB Connected: Local (Compass)");
//   })
//   .catch((err) => {
//     console.log("MongoDB Connection Error:", err.message);
//   });

// ═══════════════════════════════════════════════════════════════
//  SCHEMA & MODEL
// ═══════════════════════════════════════════════════════════════
const schema = new mongoose.Schema(
  {},
  {
    strict: false,
    timestamps: true,
  }
);

const Record = mongoose.model("Record", schema);

// ═══════════════════════════════════════════════════════════════
//  ROUTES
// ═══════════════════════════════════════════════════════════════

// CREATE
app.post("/api/records", async (req, res) => {
  try {
    const record = await Record.create(req.body);
    res.status(201).json({
      message: "Record added successfully",
      record: record,
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// READ
app.get("/api/records", async (req, res) => {
  try {
    const records = await Record.find();
    res.json(records);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// UPDATE
app.put("/api/records/:id", async (req, res) => {
  try {
    const record = await Record.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });

    if (!record) {
      return res.status(404).json({ message: "Record not found" });
    }

    res.json({ message: "Record updated successfully", record: record });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// DELETE
app.delete("/api/records/:id", async (req, res) => {
  try {
    const record = await Record.findByIdAndDelete(req.params.id);

    if (!record) {
      return res.status(404).json({ message: "Record not found" });
    }

    res.json({ message: "Record deleted successfully" });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ═══════════════════════════════════════════════════════════════
//  START SERVER
// ═══════════════════════════════════════════════════════════════
mongoose.connection.once("open", () => {
  app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
  });
});
