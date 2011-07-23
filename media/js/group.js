$(document).ready(function() {
    var csrf = $('#group_choices input[name=csrfmiddlewaretoken]').val();
    var map = $('#mapcanvas_group');

    function get_ll(lat, lon) {
        return new google.maps.LatLng(parseFloat(lat), parseFloat(lon));
    }

    var orig_center = get_ll(map.data('lat'), map.data('lon'));
    var myOptions = {
        zoom: 17,
        center: orig_center,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var mapobj = new google.maps.Map(document.getElementById("mapcanvas_group"), myOptions);

    setInterval(function() {
        $.ajax({
            type: "GET",
            url: $('#group_choices').data('foodurl'),
            data: {csrfmiddlewaretoken: csrf},
            dataType: 'json',
            success: function(response) {
                var memberlist = $('#memberlist');
                memberlist.html('');
                var members = response['members'];
                for(var i=0; i<members.length; i++) {
                    memberlist.append('<li>' + members[i] + '</li>');
                }

                var placelist = $('#group_choice_wrap');
                placelist.html('');
                var places = response['choices'];
                for(var i=0; i<places.length; i++) {
                    placelist.append('<p><small>(' + places[i]['points'] + ' points)</small><span class="round">' + places[i]['name'] + '</span></p>');
                }
                mapobj.setCenter(get_ll(response["latitude"], response["longitude"]));

            }
        });
    }, 5000);
});
