
var goal = []
var goalIds = [];
function getGoal(id) {
  if (goal.length > 0) {
    var data = {
      id: id,
      content: $("#cont_" + id).text()
    }
    var x = JSON.stringify(data)
    var index = goal.indexOf(x)
    if (index == -1) {
      goal.push(x)
    } else {
      goal.splice(index, 1)
    }
  } else {
    var data = {
      id: id,
      content: $("#cont_" + id).text()
    }
    var x = JSON.stringify(data)
    goal.push(x)
  }
  localStorage.setItem("goal", JSON.stringify(goal))
  goalIds = goal.map(element => JSON.parse(element).id);
  console.log(goalIds)
  issample();
}

function issample() {
  var select = document.getElementById("goal");
  for (var i = 0; i < goalIds.length; i++) {
    var option = document.createElement("OPTION");
    var txt = document.createTextNode(goalIds[i]);
    option.appendChild(txt);
    option.setAttribute("value",goalIds[i]);
    select.appendChild(option);
  }
}
function initGoals() {
  var storedNames = JSON.parse(localStorage.getItem("goal") || '[]');
  goalIds = storedNames.map(element => JSON.parse(element).id);
}