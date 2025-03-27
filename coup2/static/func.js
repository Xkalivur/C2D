function addcode() {
  var value = document.getElementById('host_name').value;
            $.ajax({
                url: '/process',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ "value": value })
            });
}