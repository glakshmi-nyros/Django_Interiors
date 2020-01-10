//furniture
window.onload = function()
{
  var imagePath = "../static/images/";
  var localStorageSliderNumber;
  var localStorageImagePath; 
  if (window.localStorage.getItem('sliderValue') != null) {
    localStorageSliderNumber = window.localStorage.getItem('sliderValue');
  } else {
    window.localStorage.setItem('sliderValue', '1');
    localStorageSliderNumber = 1;
  }
  if (window.localStorage.getItem('imagePath') != null) {
    imagePath = imagePath + window.localStorage.getItem('imagePath') + ".jpg";
  }
  var rangeslider = document.getElementById("sliderRange");
  var output = document.getElementById("sliderOutput");
  var images = document.getElementById("sliderImages");

  rangeslider.addEventListener('input', function() {
    for (var i = 0; i < output.children.length; i++) {
      output.children[i].style.display = 'none';
      images.children[i].style.display = 'none';
    }
    i = Number(this.value) - 1;
    output.children[i].style.display = 'block';
    images.children[i].style.display = 'block';
    window.localStorage.setItem('imagepath', rangeslider.getAttribute('value'));
    window.localStorage.setItem('sliderValue', (i+1));

    



});

}
