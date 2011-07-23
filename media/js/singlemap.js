$(document).ready(function() {
    if($('#mapcanvas').length) {
        var map = $('#mapcanvas');
        var latlng = new google.maps.LatLng(parseFloat(map.data('lat')), parseFloat(map.data('long')));
        var myOptions = {
            zoom: 17,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var mapobj = new google.maps.Map(document.getElementById("mapcanvas"), myOptions);
        var marker = new google.maps.Marker({
            position: latlng,
            map: mapobj
        });
    }
});
