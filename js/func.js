function addcode() {
  let host_name = document.getElementById("host_name").value;
  localStorage.setItem(JSON.stringify(host_name),undefined)
}