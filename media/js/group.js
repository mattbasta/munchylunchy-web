$(document).ready(function() {
    var csrf = $('#group_choices input[name=csrfmiddlewaretoken]').val();
    var map = $('#mapcanvas_group');

    function get_ll(lat, lon) {
        return new google.maps.LatLng(parseFloat(lat), parseFloat(lon));
    }

    var orig_center = get_ll(map.data('lat'), map.data('lon'));
    var myOptions = {
        zoom: 15,
        center: orig_center,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var mapobj = new google.maps.Map(document.getElementById("mapcanvas_group"), myOptions);
    var center_marker = new google.maps.MarkerImage("/media/img/circle_green.png",
                                                    new google.maps.Size(48, 48),
                                                    new google.maps.Point(0, 0),
                                                    new google.maps.Point(24, 24));
    var marker = new google.maps.Marker({
        position: orig_center,
        map: mapobj,
        icon: center_marker
    });

    var people = {};
    var places_m = {};

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
                    memberlist.append('<li>' + members[i][0] + '</li>');
                    if(members[i][0] in people)
                        continue;
                    people[members[i][0]] = true;
                    var marker = new google.maps.Marker({position: get_ll(members[i][1], members[i][2]), map: mapobj});
                }

                var placelist = $('#group_choice_wrap');
                placelist.html('');
                var places = response['choices'];
                for(var i=0; i<places.length; i++) {
                    placelist.append('<p><small>(' + places[i]['points'] + ' points)</small><span class="round">' + places[i]['name'] + '</span></p>');
                    if(places[i]["name"] in places_m)
                        continue;
                    places_m[places[i]["name"]] = true;
                    var marker = new google.maps.Marker({position: get_ll(places[i]["latitude"], places[i]["longitude"]), map: mapobj, title: places[i]["name"]});
                }
                mapobj.setCenter(get_ll(response["latitude"], response["longitude"]));

            }
        });
    }, 5000);
});
