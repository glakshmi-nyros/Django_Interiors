window.addEventListener('load', (event) => {
      var styleIds = [];
      function initStyles() {
        var storedNames = JSON.parse(localStorage.getItem("styles") || '[]');
        styleIds = storedNames.map(element => JSON.parse(element).id);
      }
      function addArrToList() {
        var select = document.getElementById("design");
        for (var i = 0; i < styleIds.length; i++) {
          var option = document.createElement("OPTION");
          var txt = document.createTextNode(styleIds[i]);
          option.appendChild(txt);
          option.setAttribute("selected",styleIds[i]);
          select.appendChild(option);
}
}

initStyles();
addArrToList();

});