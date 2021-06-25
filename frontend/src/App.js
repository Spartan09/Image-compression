import { useState } from "react";
import "./App.css";
import image from "./Assets/Group.png";

function App() {
  let file;
  const [filePresent, setFilePresent] = useState(false);
  const [fileName, setFileName] = useState(false);
  const allowDrop = (e) => {
    e.preventDefault();
  };
  const fileDrop = (e) => {
    e.preventDefault();
    file = e.dataTransfer.files[0];
    setFilePresent(true);
    setFileName(file.name);
    console.log(file);
  };
  const compress = (e) => {
    var data = new FormData();
    data.append("primary", file, file.name);
    data.append("name", "test");
    console.log(data);
    fetch("compress", {
      method: "POST",
      body: data,
    })
      .then((response) => response.blob())
      .then((blob) => {
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "compressed_" + file.name;
        document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
        a.click();
        a.remove(); //afterwards we remove the element again
      });
  };
  return (
    <div className="App">
      <div className="container">
        <div className="left">
          <div className="content">
            <div className="heading">
              <span id="mainHeading">Compress</span>
              <br />
              <span id="subHeading">Away</span>
            </div>
            <div className="body">
              Made with the power of Singular Value Decomposition and NodeJs.
              Served to you on ReactJs.
            </div>
            <div className="footer">
              <img src={image} alt="github logo" />
              <div className="repoBg">
                <a
                  href="https://github.com/Spartan09/Image-Compression"
                  id="repoName"
                >
                  Spartan09/Image-Compression
                </a>
              </div>
            </div>
          </div>
        </div>
        <div className="right">
          <div
            className="dragArea"
            onDrop={(e) => {
              fileDrop(e);
            }}
            onDragOver={allowDrop}
          >
            <span
              className="iconify"
              data-inline="false"
              data-icon="ant-design:file-twotone"
            ></span>
            <span className="dragText">{fileName || "Drag File Here"}</span>
          </div>
          <button className="btn" onClick={compress} disabled={!filePresent}>
            <span>Compress</span>
          </button>
          <div id="bottomText">
            <a id="bottomText" href="http://www.asrtechexpert.com">
              Made with ♥️ by Ayush
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
