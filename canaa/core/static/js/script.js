$(document).ready(function() {
	// Contact Maps
	$("#maps").gmap3({
		map: {
			options: {
			  center: [-7.850147, -34.907205],
			  zoom: 15,
			  scrollwheel: false
			}  
		 },
		marker:{
			latLng: [-7.850147, -34.907205],
			options: {
			 icon: new google.maps.MarkerImage(
			   "https://dl.dropboxusercontent.com/u/29545616/Preview/marker.png",
			   new google.maps.Size(48, 48, "px", "px")
			 )
			}
		 }
	});
	
});
