/*
Vizion - Al/ML - Chatbot Responsive HTML5 Template
Author: iqonicthemes.in
Version: 1.0
Design and Developed by: iqonicthemes.in
*/
/*----------------------------------------------
Index Of Script
------------------------------------------------
 1 Page Loader
 2 Back To Top
 3 Tooltip
 4 Hide Menu
 5 Accordion
 6 Header
 7 About Menu
 8 Magnific Popup
 9 Countdown
10 Progress Bar
11 widget
12 counter
13 Wow Animation
14 Owl Carousel
15 Contact From
16 On Scroll
17 Cookie
------------------------------------------------
Index Of Script
----------------------------------------------*/

function openUrl(path){
    var win = window.open(path, '_blank');
    win.focus();
}

(function($) {

	"use strict";
	$(document).ready(function() {



		/*------------------------
		Page Loader
		--------------------------*/
		jQuery("#load").fadeOut();
		jQuery("#loading").delay(0).fadeOut("slow");



		/*------------------------
		Back To Top
		--------------------------*/
		$('#back-to-top').fadeOut();
		$(window).on("scroll", function() {
			if ($(this).scrollTop() > 250) {
				$('#back-to-top').fadeIn(1400);
			} else {
				$('#back-to-top').fadeOut(400);
			}
		});
		// scroll body to 0px on click
		$('#top').on('click', function() {
			$('top').tooltip('hide');
			$('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});



		/*------------------------
		Tooltip
		--------------------------*/
		$(function() {
			$('[data-toggle="tooltip"]').tooltip()
		})



		/*------------------------
		Hide Menu
		--------------------------*/
		$(".navbar a").on("click", function(event) {
			if (!$(event.target).closest(".nav-item.dropdown").length) {
				$(".navbar-collapse").collapse('hide');
			}
		});



		/*------------------------
		Accordion
		--------------------------*/
		$('.iq-accordion .iq-ad-block .ad-details').hide();
		$('.iq-accordion .iq-ad-block:first').addClass('ad-active').children().slideDown('slow');
		$('.iq-accordion .iq-ad-block').on("click", function() {
			if ($(this).children('div').is(':hidden')) {
				$('.iq-accordion .iq-ad-block').removeClass('ad-active').children('div').slideUp('slow');
				$(this).toggleClass('ad-active').children('div').slideDown('slow');
			}
		});



		/*------------------------
		Header
		--------------------------*/
		$('.navbar-nav li a').on('click', function(e) {
			var anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top - 0
			}, 1500);
			e.preventDefault();
		});
		$('.about-manu li a').on('click', function(e) {
			var anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $(anchor.attr('href')).offset().top - 170
			}, 1500);
			e.preventDefault();
		});
		$(window).on('scroll', function() {
			if ($(this).scrollTop() > 100) {
				$('header').addClass('menu-sticky');
			} else {
				$('header').removeClass('menu-sticky');
			}
		});



		/*------------------------
		About menu
		--------------------------*/
		$(window).on('scroll', function() {
			var window_top = $(window).scrollTop();
			var footer_top = $("footer").offset().top - 200;
			var div_top = $('.breadcrumbs').outerHeight();
			var div_height = $(".about-manu").height();
			if (window_top + div_height > footer_top)
				$('.about-manu').removeClass('menu-sticky');
			else if (window_top > div_top) {
				$('.about-manu').addClass('menu-sticky');
			} else {
				$('.about-manu').removeClass('menu-sticky');
			}
		});



		/*------------------------
		Magnific Popup
		--------------------------*/
		$('.popup-gallery').magnificPopup({
			delegate: 'a.popup-img',
			tLoading: 'Loading image #%curr%...',
			type: 'image',
			mainClass: 'mfp-img-mobile',
			gallery: {
				navigateByImgClick: true,
				enabled: true,
				preload: [0, 1]
			},
			image: {
				tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
			}
		});
		$('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
			type: 'iframe',
			disableOn: 700,
			mainClass: 'mfp-fade',
			preloader: false,
			removalDelay: 160,
			fixedContentPos: false
		});



		/*------------------------
		Countdown
		--------------------------*/
		$('#countdown').countdown({
			date: '10/01/2019 23:59:59',
			day: 'Day',
			days: 'Days'
		});



		/*------------------------
		Progress Bar
		--------------------------*/
		$('.iq-progress-bar > span').each(function() {
			var $this = $(this);
			var width = $(this).data('percent');
			$this.css({
				'transition': 'width 2s'
			});
			setTimeout(function() {
				$this.appear(function() {
					$this.css('width', width + '%');
				});
			}, 500);
		});



		/*------------------------
		widget
		--------------------------*/
		$('.iq-widget-menu > ul > li > a').on('click', function() {
			var checkElement = $(this).next();
			$('.iq-widget-menu li').removeClass('active');
			$(this).closest('li').addClass('active');
			if ((checkElement.is('ul')) && (checkElement.is(':visible'))) {
				$(this).closest('li').removeClass('active');
				checkElement.slideUp('normal');
			}
			if ((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
				$('.iq-widget-menu ul ul:visible').slideUp('normal');
				checkElement.slideDown('normal');
			}
			if ($(this).closest('li').find('ul').children().length === 0) {
				return true;
			} else {
				return false;
			}
		});



		/*------------------------
		counter
		--------------------------*/
		$('.timer').countTo();



		/*------------------------
		Wow Animation
		--------------------------*/
		var wow = new WOW({
			boxClass: 'wow',
			animateClass: 'animated',
			offset: 0,
			mobile: false,
			live: true
		});
		wow.init();



		/*------------------------
		Owl Carousel
		--------------------------*/
		$('.owl-carousel').each(function() {
			var $carousel = $(this);
			$carousel.owlCarousel({
				items: $carousel.data("items"),
				loop: $carousel.data("loop"),
				margin: $carousel.data("margin"),
				nav: $carousel.data("nav"),
				dots: $carousel.data("dots"),
				autoplay: $carousel.data("autoplay"),
				autoplayTimeout: $carousel.data("autoplay-timeout"),
				navText: ['<i class="fa fa-angle-left fa-1x"></i>', '<i class="fa fa-angle-right fa-1x"></i>'],
				responsiveClass: true,
				responsive: {
					// breakpoint from 0 up
					0: {
						items: $carousel.data("items-mobile-sm")
					},
					// breakpoint from 480 up
					480: {
						items: $carousel.data("items-mobile")
					},
					// breakpoint from 786 up
					786: {
						items: $carousel.data("items-tab")
					},
					// breakpoint from 1023 up
					1023: {
						items: $carousel.data("items-laptop")
					},
					1199: {
						items: $carousel.data("items")
					}
				}
			});
		});



		/*------------------------
		Contact From
		--------------------------*/
		$('#contact').submit(function(e) {
			var form_data = $(this).serialize();
			var flag = 0;
			e.preventDefault(); // Prevent Default Submission
			$('.require').each(function() {
				if ($.trim($(this).val()) == '') {
					$(this).css("border", "1px solid red");
					e.preventDefault(); // Prevent Default Submission
					flag = 1;
				} else {
					$(this).css("border", "1px solid grey");
					flag = 0;
				}
			});

			const scriptURL = 'https://script.google.com/macros/s/AKfycbwnlvrGb4o9AnwRJRjSTKPJEKKbLbxA2_FrXavk7I4lATNL9SpS/exec'
            const form = document.forms['submit-to-google-sheet']

            function onSuccess(){
                console.log("successfully");
                $("#result").html('Message successfully sent.');
                $("#result").css({
                    'display': 'inherit',
                    'color': 'green'
                });
                $('#contact')[0].reset();
            }

            function onFailure(){
                $("#result").html('Message failed to sent.');
                $("#result").css({
                    'display': 'inherit',
                    'color': 'red'
                });
                console.log("fail");
            }

            e.preventDefault()
            fetch(scriptURL, { method: 'POST', body: new FormData(form)})
            .then(response => onSuccess())
            .catch(error => onFailure())
		});
	});



	/*------------------------
	On Scroll
	--------------------------*/
	jQuery(window).on("scroll", onScroll);
	jQuery('.about-manu a[href^="#"]').on('click', function(e) {
		// jQuery(window).off("scroll");
		$(window).on('scroll', function() {
			if ($(this).scrollTop() > 100) {
				$('header').addClass('menu-sticky');
			} else {
				$('header').removeClass('menu-sticky');
			}
		});



		$(window).on('scroll', function() {

			var window_top = $(window).scrollTop();
			var footer_top = $("footer").offset().top - 200;
			var div_top = $('.breadcrumbs').outerHeight();
			var div_height = $(".about-manu").height();
			if (window_top + div_height > footer_top)
				$('.about-manu').removeClass('menu-sticky');
			else if (window_top > div_top) {
				$('.about-manu').addClass('menu-sticky');
			} else {
				$('.about-manu').removeClass('menu-sticky');
			}
		});
		var target = this.hash;
		//if( target.length ) {
		var nav = jQuery(target);
		if (nav.length) {
			var contentNav = nav.offset().top;
			//e.preventDefault();
			jQuery('html, body').stop().animate({
				'scrollTop': contentNav
			}, 500, 'swing', function() {
				window.location.hash = target;
				jQuery(window).on("scroll", onScroll);
			});
		}
	});

	function onScroll(event) {
		var scrollPos = jQuery(window).scrollTop() + 80;
		jQuery('.about-manu a[href^="#"]').each(function() {
			if (jQuery(this).attr("href").indexOf('https://') == -1) {
				var refElement = jQuery(jQuery(this).attr("href"));
			} else {
				var refElement = jQuery(this);
			}
			if (jQuery(this).attr("href").indexOf('https://') == -1) {
				if (!refElement.length) return; // if the length is 0 (nothing selected) skip the rest of this iteration where the accessing of the position happens
				if (refElement.position().top <= scrollPos) {
					jQuery(document).find('.about-manu li').removeClass("active");
					jQuery(this).parent().addClass("active");
				} else {
					jQuery(this).parent().removeClass("active");
				}
			}
		});
	}

	/*------------------------
	Cookie
	--------------------------*/
//	$(window).load(function() {
//		var user = getCookie("chabot");
//		if (user == "") {
//			$('#cookie_div').css("display", "inherit");
//		}
//		$('#cookie').on('click', function() {
//			checkCookie();
//		});
//	});

//	function setCookie(cname, cvalue) {
//		var d = new Date();
//		d.setTime(d.getTime() + (24 * 60 * 60 * 1000));
//		var expires = "expires=" + d.toGMTString();
//		// document.cookie = cname + "=" + cvalue + "," + expires + ", path=/";
//		document.cookie = cname + "=" + cvalue + ";" + expires + "; path=/";
//		$('#cookie_div').css("display", "none");
//	}

//	function getCookie(cname) {
//		var name = cname + "=";
//		var ca = document.cookie.split(';');
//		for (var i = 0; i < ca.length; i++) {
//			var c = ca[i];
//			var cookie_ = c.trim().split('=') || [];
//			if (cookie_ != [] && cname == cookie_[0]) {
//				return cookie_[1];
//			}
//		}
//		return "";
//	}

//	function checkCookie() {
//		var user = getCookie("chabot");
//		if (user == "") {
//			$('#cookie_div').css("display", "none");
//			setCookie("chabot", "skdfdfdfdfdfgsdf");
//		} else {
//			$('#cookie_div').css("display", "inherit");
//		}
//	}
})(jQuery);