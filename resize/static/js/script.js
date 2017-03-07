
// Maximum width and height
const maximum = 5000;

// Default image size
var imgWidth  = 100;
var imgHeight = 100;

document.getElementById("file").onchange = function () {

	var reader = new FileReader;

	// Reset size
	imgWidth  = 100;
	imgHeight = 100;

	reader.onload = function(e) {
	    var image = new Image();
	    image.src = e.target.result;

	    // Set the preview_image source
        document.getElementById("preview_image").src = image.src;
        
        // Load the image before get its width and height
		image.onload = function() {
	        if( image.width != 0 && image.height != 0 ) {
		        // Show the image original size
		        document.getElementById("original_size").innerHTML = "Original Size: " + image.width + " X " + image.height;

		        // Store the original size of the image
				imgWidth  = image.width;
				imgHeight = image.height;

				// Update the height based on the width
			    onWidthValueChanged();
	    	}
    	}
	};

    // Read the image file as a data URL
    reader.readAsDataURL(this.files[0]);
};

function onWidthValueChanged() {
 
	if(document.getElementById("width").value == "") {
		return;
	}

	var currentWidth = document.getElementById("width").value;

	// Minimum should be 1
	if(currentWidth <= 0) {
		document.getElementById("width").value = 1;
	}

	// Maximum should be 5000
	if(currentWidth > maximum) {
		document.getElementById("width").value = maximum;
	}

	// If has some image in the preview_image
	if(document.getElementById("preview_image").src != "") {

		// Calculates the factor based on the size of the original image
	    var factor = (imgHeight*100)/imgWidth;

	    // Calculates the new height
	    var newHeight = parseInt(((factor*currentWidth)/100), 10);

	    if(newHeight <= 0) {
			document.getElementById("height").value = 1;
		}else if(newHeight > maximum) {
			document.getElementById("height").value = maximum;
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

	// Minimum should be 1
	if(currentHeight <= 0) {
		document.getElementById("height").value = 1;
		return;
	}

	// Maximum should be 5000
	if(currentHeight > maximum) {
		document.getElementById("height").value = maximum;
		return;
	}
}
