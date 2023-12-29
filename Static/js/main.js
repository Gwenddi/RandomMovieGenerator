(function ($) {
"use strict";

// preloader
$(window).on('load', function() {
	$("#loading").fadeOut(500);
});

// background image loaded
$("[data-background]").each(function(){
    $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
})
$("[data-background]").each(function(){
    $(this).css("background", $(this).attr("data-bg-color"))
})

// One Page Nav
var top_offset = $('.header-bottom-area').height() - 10;
$('.main-menu nav ul').onePageNav({
	currentClass: 'active',
	scrollOffset: top_offset,
});


// nice select
$('select').niceSelect();


// meanmenu
$('#mobile-menu').meanmenu({
	meanMenuContainer: '.mobile-menu',
	meanScreenWidth: "991"
});

// header sticky
$(window).on('scroll', function () {
	var scroll = $(window).scrollTop();
	if (scroll < 45) {
		$(".header-sticky").removeClass("sticky");
	} else {
		$(".header-sticky").addClass("sticky");
	}
});

// counter
$('.counter').counterUp({
    delay: 10,
    time: 1000
});

// properties active
$('.properties-active').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    responsive: [{
        breakpoint: 1292,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            dots: true,
            arrows: false
        }
    }, {
        breakpoint: 993,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            dots: true,
            arrows: false
        }
    }, {
        breakpoint: 768,
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: true,
            arrows: false
        }
    }]
});
// news active
$('.news-active').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    dots: true,
    arrows: false,
    responsive: [{
        breakpoint: 1292,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            dots: true,
            arrows: false
        }
    }, {
        breakpoint: 993,
        settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            dots: true,
            arrows: false
        }
    }, {
        breakpoint: 768,
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: true,
            arrows: false
        }
    }]
});

/*back to top*/
	$(document).on('click', '.back-to-top', function () {
		$("html,body").animate({
			scrollTop: 0
		}, 1000);
	});

    $(window).on("scroll", function() {
    /*---------------------------------------
    sticky menu activation && Sticky Icon Bar
    -----------------------------------------*/

    var mainMenuTop = $(".navbar-area");
    if ($(window).scrollTop() >= 1) {
        mainMenuTop.addClass('navbar-area-fixed');
    }
    else {
        mainMenuTop.removeClass('navbar-area-fixed');
    }
    
    var ScrollTop = $('.back-to-top');
    if ($(window).scrollTop() > 500) {
        ScrollTop.fadeIn(1000);
    } else {
        ScrollTop.fadeOut(1000);
    }
});

// WOW active
new WOW().init();

})(jQuery);