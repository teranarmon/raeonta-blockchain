fetch("/api/chain")
  .then(res => res.json())
  .then(data => {
    document.getElementById("chain").innerHTML =
      "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
  });
