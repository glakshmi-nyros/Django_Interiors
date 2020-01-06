
// function for on body load in register form//
function isValue(){ 
	var storedValue = JSON.parse(localStorage.getItem("sliderValue"))
	$("#furn").val(storedValue);
}
 
