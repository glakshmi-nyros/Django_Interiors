window.addEventListener('load', (event) => {
      var goalIds = [];
      function initGoals() {
        var storedNames = JSON.parse(localStorage.getItem("goal") || '[]');
        goalIds = storedNames.map(element => JSON.parse(element).id);
      }
      function addArrToList() {
        var select = document.getElementById("goal");
        for (var i = 0; i < goalIds.length; i++) {
          var option = document.createElement("OPTION");
          var txt = document.createTextNode(goalIds[i]);
          option.appendChild(txt);
          option.setAttribute("selected",goalIds[i]);
          option.selected("selected",goalIds[i])
          selected.appendChild(option);

}
}

initGoals();
addArrToList();

});