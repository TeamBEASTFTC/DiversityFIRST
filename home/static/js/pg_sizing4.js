function prevSizing(){
	var width = $('#box_js2').width();
	var h = width * (210 / 297);
	//dimensioning it to be roughly A4 size
	$('#box_js2').height(h);
	$('#box_js').height(h);

	var size = 0.05 * width
	var padR = width * 0.275
	
	// font-size
	$('.pretitle').css('font-size', size);
	$('.predetails').css('font-size', size);

	//message padding (right)
	$('.predetails').css('padding-right', padR);

	//message so I know
}

function downBtnLoc(){
	if ($(window).width() < 700){
		//grid off
		$('#sm_down').css('display', 'none');
		$('#lg_down').css('display', 'block');
	} else {
		//grid on
		$('#sm_down').css('display', 'block');
		$('#lg_down').css('display', 'none');
	}
}

function TeamPhotoSize(){
	if ($('.team_photo').height > $('.team_photo').width){
		var portrait = true;
	} else{
		var portrait = false;
	}
	if (portrait){
	img_h_dimension = (($(window).height()) * 0.75);
	$('.team_photo').height(img_h_dimension);		
	} else{
	img_w_dimension = (($(window).width()) * 0.75);
	$('.team_photo').width(img_w_dimension);	
	}

};

$(function(){
	$('#message_field').change(function(){
		$('#message').html($('#message_field').val());
	});
	prevSizing();
	downBtnLoc();
	TeamPhotoSize();
});

$(window).resize(function(){
	prevSizing();
	downBtnLoc();
	TeamPhotoSize();
});

$('#carouselExampleIndicators').on('slid.bs.carousel', function(){
	TeamPhotoSize();
})

/*
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
*/
//Make preview set smaller once broken
/* 
var prebox1 = document.getElementById("box_js");
var width1 = prebox.offsetWidth;

var prebox2 = document.getElementById("box_js2");
var width2 = prebox2.offsetWidth;
prebox2.style.padding-top = width2 * 0.7071
*/

/*
//if (prebox.getComputedStyle.width >= "500px"){ 
if ((width1 >= 500) || (width2 >= 500)){
	prebox1.style.height = (500*0.7071);
	alert("done");
	prebox2.style.height = (500*0.7071);
}
*/