$(document).ready(function() {
    var startText = $('#questions h3').html();
    $('#questions h3').html('Please wait while we load your customized questions...');
    $("#bottom_buttons").hide();
    navigator.geolocation.getCurrentPosition(
        function(position) {
            console.log(position.coords.latitude);
            console.log(position.coords.longitude);
            verifyAmerica(position.coords.latitude, position.coords.longitude);
        },
        function() {
            alert('Refresh the page and please share your locations we can give you the best results!');
        },
        {maximumAge:3600000});

    function verifyAmerica(latitude, longitude) {
        //$.getJSON('http://maps.googleapis.com/maps/api/geocode/json?latlng=' + latitude + ',' + longitude + '&sensor=true&callback=?',
        $.getJSON('http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20json%20where%20url%3D%22http%3A%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fgeocode%2Fjson%3Flatlng%3D' + latitude + ',' + longitude + '%26sensor%3Dtrue%22&format=json&callback=?',
            function(response) {
                response = response.query.results.json;
                var isAmerica = false;

                function handleResult(result) {
                    if(!("length" in result.address_components)) {
                        isAmerica = result.address_components.short_name == "US";
                    } else {
                        for(var j=0; j < result.address_components.length; j++) {
                            var component = result.address_components[j];
                            if(component.short_name == "US") {
                                isAmerica = true;
                                break;
                            }
                        }
                    }

                    if(isAmerica) {
                        $('#questions h3').html(startText);
                        $("#bottom_buttons").show();
                        var contButton = $('#bottom_buttons .continue');
                        contButton.attr('href', contButton.attr('href') + '?latitude=' + latitude + '&longitude=' + longitude);
                        getQuestions({"coords": {"latitude": latitude, "longitude": longitude}});

                        return true;
                    }

                }

                if(response.results.length > 0) {
                    for(var i=0; i<response.results.length; i++) {
                        var resultresult = handleResult(response.results[i]);
                        if(resultresult)
                            break;
                    }
                }
                if(!isAmerica) {
                    $('#questions h3').html('Sorry, but MunchyLunchy is currently only available in the US!');
                }
            });
    }

    function getQuestions(position) {
        var csrf = $('#questions input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: "POST",
            url: $('#questions').data('url'),
            data: {csrfmiddlewaretoken: csrf,
                   latitude: position.coords.latitude,
                   longitude: position.coords.longitude},
            success: function(response) {
                response = JSON.parse(response);
                if(response['result'] == 'okay') {
                    // Good to go, populate questions
                    for(t in response['tastes_pretty']) {
                        $('#questions').append(format('<div class="question"><a class="button round red square nah likes" data-taste="{0}" data-likes="nah">NAH</a><a class="close"><img src="/media/img/close.png" /></a><a class="button round green square yep likes" data-taste="{0}" data-likes="yep">YEP</a><p>{1}?</p></div>', response['tastes'][t], response['tastes_pretty'][t]));
                    }
                    $('#questions_left').html(response['to_ask']);
                    $('#bottom_buttons').show();

                    function sendLike(obj) {
                        $.ajax({
                            type: "POST",
                            url: $('#questions').data('likeurl'),
                            data: {csrfmiddlewaretoken: csrf,
                                   taste: $(obj).data('taste'),
                                   likes: $(obj).data('likes')}
                        });
                    }

                    function hideAndSubtract(obj) {
                        $(obj.parentNode).fadeOut();
                        var ql = $('#questions_left'),
                            new_number = parseInt(ql.text() - 1);
                        if(new_number == 0) {
                            $('#questions h3').fadeOut();
                        }
                        ql.html(new_number);
                    }

                    $('#questions .close').click(function() {
                        hideAndSubtract(this);
                    });
                    $('#questions .likes').click(function() {
                        sendLike(this);
                        hideAndSubtract(this);
                    });


                }
                else {
                    // Error on API server
                }
            },
            error: function() {
                // Error with AJAX request
            }
        });
    }

    /* Python(ish) string formatting:
     * >>> format('{0}', ['zzz'])
     * "zzz"
     * >>> format('{0}{1}', 1, 2)
     * "12"
     * >>> format('{x}', {x: 1})
     * "1"
     */
    var format = (function() {
        var re = /\{([^}]+)\}/g;
        return function(s, args) {
            if (!args) return;
            if (!(args instanceof Array || args instanceof Object))
                args = Array.prototype.slice.call(arguments, 1);
            return s.replace(re, function(_, match){ return args[match]; });
        };
    })();
});
