const express = require("express");
const spawn = require("child_process").spawn;
const multer = require("multer");
const app = express();
const port = 5000;

app.use(express.json());
app.use(express.static("public"));

const uploading = multer({
  dest: __dirname + "/images/",
});

app.post("/compress", uploading.single("primary"), (req, res) => {
  const pythonProcess = spawn("python", [
    "./Image-Compression/SVD.py",
    req.file.filename,
  ]);
  pythonProcess.stdout.on("data", (data) => {
    res.download(data.toString().split("\n")[0] + "_r=500.jpeg");
  });
  pythonProcess.stderr.on("data", (error) => {
    console.log(error.toString());
  });
  pythonProcess.on("close", (code) => console.log(code.toString()));
});

// app.post("/compress", uploading.single("primary"), (req, res) => {
//   res.send(200);
// });

app.listen(port, () => {
  console.log(`at http://localhost:${port}`);
});
