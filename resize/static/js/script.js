
document.getElementById("file").onchange = function () {

	var reader = new FileReader;

	reader.onload = function(e) {
	    var image = new Image();
	    image.src = e.target.result;
        document.getElementById("preview_image").src = image.src;
        document.getElementById("original_size").innerHTML = "Original Size: " + image.width + " X " + image.height;
	};

    // read the image file as a data URL.
    reader.readAsDataURL(this.files[0]);
};

function onWidthValueChanged() {

	if(document.getElementById("width").value == "") {
		return;
	}

	var currentWidth = document.getElementById("width").value;

	if(currentWidth <= 0) {
		document.getElementById("width").value = 1;
	}

	if(currentWidth > 5000) {
		document.getElementById("width").value = 5000;
	}

	if(document.getElementById("preview_image").src != "") {

	    var image = new Image();
	    image.src = document.getElementById("preview_image").src;

	    var width = image.width;
	    var height = image.height;

	    var factor = (height*100)/width;

	    var newHeight = parseInt(((factor*currentWidth)/100), 10);

	    if(newHeight <= 0) {
			document.getElementById("height").value = 1;
		}else if(newHeight > 5000) {
			document.getElementById("height").value = 5000;
		}else {
			document.getElementById("height").value = newHeight;
		}
	}
}

function onHeightValueChanged() {

	if(document.getElementById("height").value == "") {
		return;
	}

	var currentHeight = document.getElementById("height").value;

	if(currentHeight <= 0) {
		document.getElementById("height").value = 1;
		return;
	}

	if(currentHeight > 5000) {
		document.getElementById("height").value = 5000;
		return;
	}
}
