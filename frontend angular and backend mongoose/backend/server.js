const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(cors());
app.use(express.json());
// Serve frontend static files
app.use(express.static(path.join(__dirname, "../frontend")));

// Connect to local MongoDB
mongoose.connect("mongodb://127.0.0.1:27017/web_lab")
.then(() => {
    console.log("MongoDB Connected");
})
.catch(err => {
    console.log("MongoDB Connection Error:", err.message);
});

// Flexible schema for lab applications
const schema = new mongoose.Schema({}, {
    strict: false,
    timestamps: true
});

const Record = mongoose.model("Record", schema);

// CREATE
app.post("/api/records", async (req, res) => {
    try {
        const record = await Record.create(req.body);
        res.status(201).json({
            message: "Record added successfully",
            record: record
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
        const record = await Record.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true }
        );

        if (!record) {
            return res.status(404).json({
                message: "Record not found"
            });
        }

        res.json({
            message: "Record updated successfully",
            record: record
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// DELETE
app.delete("/api/records/:id", async (req, res) => {
    try {
        const record = await Record.findByIdAndDelete(req.params.id);

        if (!record) {
            return res.status(404).json({
                message: "Record not found"
            });
        }

        res.json({
            message: "Record deleted successfully"
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Start server only after MongoDB connects
mongoose.connection.once("open", () => {
    app.listen(5000, () => {
        console.log("Server running at http://localhost:5000");
    });
});
