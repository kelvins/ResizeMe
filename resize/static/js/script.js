
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