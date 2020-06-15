(function($) {
    "use strict";
$(window).on('load', function() {
        $(".preloader").fadeOut("slow", function() {
            $(".preloader-left").addClass("slide-left");
        });
$('#lionhero').owlCarousel({
            animateOut: 'fadeOut',
            nav: true,
            navText: [
                '<i class="ion-ios-arrow-thin-left"></i>',
                '<i class="ion-ios-arrow-thin-right"></i>'
            ],
            items: 1,
            navSpeed: 400,
            loop: true,
            autoplay: true,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
        });

        $('#liontextslider').owlCarousel({
            nav: false,
            items: 1,
            navSpeed: 400,
            loop: true,
            autoplay: true,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
        });

        $('#liontestimonial').owlCarousel({
            nav: true,
            navText: [
                '<i class="ion-ios-arrow-thin-left"></i>',
                '<i class="ion-ios-arrow-thin-right"></i>'
            ],
            items: 1,
            navSpeed: 400,
            loop: true,
            autoplay: true,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
        });
    });



    //Custom Cursor
    if (('.cursor').length > 0) {
        var $circleCursor = $('.cursor');

        function moveCursor(e) {
            var t = e.clientX + "px",
                n = e.clientY + "px";
            TweenMax.to($circleCursor, .2, {
                left: t,
                top: n,
                ease: 'Power1.easeOut'
            });
        }
        $(window).on('mousemove', moveCursor);

        function zoomCursor() {
            TweenMax.to($circleCursor, .2, {
                borderWidth: '1px',
                opacity: 0.1,
                scale: 2,
                ease: 'Power1.easeOut'
            });
        }

        $(document).on('mouseenter', 'a, .zoom-cursor, .menu-item', zoomCursor);

        function noCursor() {
            TweenMax.to($circleCursor, .2, {
                opacity: 0,
                ease: 'Power1.easeOut'
            });
        }
        $(document).on('mouseenter', 'button, .btn', noCursor);

        function defaultCursor() {
            TweenLite.to($circleCursor, .1, {
                borderWidth: '2px',
                opacity: 0.5,
                scale: 1,
                ease: 'Power1.easeOut'
            });
        }

        $(document).on('mouseleave', 'a, .zoom-cursor, .menu-item, button, .btn', defaultCursor);

        $(document).ready(function() {

            $('.cursor').css('transform', 'scale(1)');
        });
    }

    //Leaflet Map

    var mymap = L.map('map').setView([40.6700, -73.9400], 14);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: '',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(mymap);

    var icon = L.divIcon({
        className: 'custom-div-icon',
        html: "<div class='map-marker'></div>",
        iconSize: [30, 30],
        iconAnchor: [15, 15]
    });

    L.marker([40.6700, -73.9400], { icon: icon }).addTo(mymap);

})(jQuery);