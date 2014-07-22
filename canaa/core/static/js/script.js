$(document).ready(function() {
	// Contact Maps
	$("#maps").gmap3({
		map: {
			options: {
			  center: [-7.559859, -35.020415],
			  zoom: 15,
			  scrollwheel: false
			}
		 },
		marker:{
			latLng: [-7.559859, -35.020415],
			options: {
			 icon: new google.maps.MarkerImage(
			   "https://dl.dropboxusercontent.com/u/29545616/Preview/marker.png",
			   new google.maps.Size(48, 48, "px", "px")
			 )
			}
		 }
	});

	/*var height = $("#k-header").height();
	$("div.navbar").attr("data-offset-top", function(){
		return ""+height;
	});*/

	/*var width = $("#wrapper").width();
	$("div.shadow2").width( width );*/
	/*$("div.k-logo-tony").( width );*/

	$(".gallery").fancybox({
		openEffect  : 'none',
		closeEffect	: 'none',

		helpers : {
			title : {
				type : 'over'
			}
		}
	});

	$(".gallery2").fancybox({
		wrapCSS    : 'fancybox-custom',
		closeClick : true,

		closeEffect	: 'elastic',

		helpers : {
			title : {
				type : 'inside'
			},
			overlay : {
				css : {
					'background' : 'rgba(238,238,238,0.85)'
				}
			}
		}
	});

	$(".galeri").fancybox({
		wrapCSS    : 'fancybox-custom',
		closeClick : true,
		openEffect : 'none',
		closeEffect	: 'elastic',

		helpers : {
			title : {
				type : 'inside'
			},
			overlay : {
				css : {
					'background' : 'rgba(238,238,238,0.85)'
				}
			}
		}
	});


	//Slider
	$("#homeslider").carousel({
		interval: 5000
	});

	$("#workslider").carousel({
		interval: 4000
	});
});
