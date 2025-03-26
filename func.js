import fs from "fs"

function create_code() {
    const fs = require("fs");
    var x = document.getElementById("host_name").value;
    let code = {};
    code[x] = undefined;

    var data = JSON.stringify(code);
    fs.writeFile("communicate.json", data, (error) => {
        // throwing the error
        // in case of a writing problem
        if (error) {
          // logging the error
          console.error(error);
      
          throw error;
        }
      
        console.log("Room code successfully created");
    });
}

function addcode() {
  try {
    var x = Document.getElementById("host_name").value;
    let data = new Object();
    data[x] = undefined;

    fs.writeFileSync("code.json", JSON.stringify(data, null, 2), 'utf8');
    console.log('Data successfully saved to disk');
  } catch (error) {
    console.log('An error has occurred ', error);
  };
}