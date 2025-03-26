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