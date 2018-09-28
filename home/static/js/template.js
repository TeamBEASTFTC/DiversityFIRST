


$(function(){
	$('#message_field').change(function(){
		$('#message').html($('#message_field').val());
	});
});



var row_c = document.getElementById("GridBox");
var sm_down = document.getElementById("sm_down");
var lg_down = document.getElementById("lg_down");


if (row_c.offsetWidth >= 720){
	lg_down.style.display = 'none';
	sm_down.style.display = 'block';
} else {
	lg_down.style.display = 'block';
	sm_down.style.display = 'none';
}

/* Make preview set smaller once broken*/
var prebox1 = document.getElementById("box_js");
var width1 = prebox.offsetWidth;

var prebox2 = document.getElementById("box_js2");
var width2 = prebox2.offsetWidth;
prebox2.style.padding-top = width2 * 0.7071

/*if (prebox.getComputedStyle.width >= "500px"){ */
if ((width1 >= 500) || (width2 >= 500)){
	prebox1.style.height = (500*0.7071);
	alert("done");
	prebox2.style.height = (500*0.7071);
}