
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

	if(document.getElementById("preview_image").src != "") {

	    var image = new Image();
	    image.src = document.getElementById("preview_image").src;

	    var width = image.width;
	    var height = image.height;

	    var factor = (height*100)/width;

		document.getElementById("height").value = parseInt(((factor*document.getElementById("width").value)/100), 10);
	}
}
