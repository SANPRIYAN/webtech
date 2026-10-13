
require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());
app.use(express.static("public"));

const User = mongoose.model("User", new mongoose.Schema({
    username: String,
    password: String
}));

app.post("/login", async (req, res) => {
    const user = await User.findOne(req.body);

    if (user) {
        res.json({ message: "Login Successful" });
    } else {
        res.status(401).json({
            message: "Invalid username or password"
        });
    }
});

async function start() {
    await mongoose.connect(process.env.MONGO_URI);

    await User.findOneAndUpdate(
        { username: "suruthi" },
        { $set: { password: "1234" } },
        { upsert: true }
    );

    app.listen(5000, () => {
        console.log("Server running on port 5000");
    });
}

start().catch(console.error);
