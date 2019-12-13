// JavaScript Document
var ww = document.body.clientWidth;
jQuery(document).ready(function () {
jQuery(".menu li a").each(function () {
if (jQuery(this).next().length > 0) {
jQuery(this).addClass("parent");
}
;
})
jQuery(".toggleMenu").click(function (e) {
e.preventDefault();
jQuery(this).toggleClass("active");
jQuery(".main-nav").slideToggle();
});
adjustMenu();
})
jQuery(window).bind('resize orientationchange', function () {
ww = document.body.clientWidth;
adjustMenu();
});
var adjustMenu = function () {
if (ww <= 991) {
jQuery(".toggleMenu").css("display", "inline-block");
if (!jQuery(".toggleMenu").hasClass("active")) {
jQuery(".main-nav").hide();
} else {
jQuery(".main-nav").show();
}
jQuery(".menu li").unbind('mouseenter mouseleave');
jQuery(".menu li a.parent").unbind('click').bind('click', function (e) {
// must be attached to anchor element to prevent bubbling
e.preventDefault();
jQuery(this).parent("li").toggleClass("hover");
});
} else if (ww > 991) {
jQuery(".toggleMenu").css("display", "none");
jQuery(".main-nav").show();
jQuery(".menu li").removeClass("hover");
jQuery(".menu li a").unbind('click');
jQuery(".menu li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function () {
// must be attached to li so that mouseleave is not triggered when hover over submenu
jQuery(this).toggleClass('hover');
});
}
}

jQuery('.carousel-inner').each(function () {
if (jQuery(this).children('div').length === 1)
jQuery(this).siblings('.carousel-control-prev, .carousel-control-next, .carousel-indicators').hide();
});

jQuery(document).ready(function(){
jQuery('[data-toggle="tooltip"]').tooltip();
});

$(document).ready(function() {
var owl = $('.CarouselOwl');
owl.owlCarousel({
margin: 30,
nav: true,
loop: true,
responsive: {
0: {items: 1},
480: {items: 1},
544: {items: 1},
768: {items: 1},
992: {items: 1},
1200: {items: 1}
}
})
})



jQuery(function () {
jQuery(".img-crop").responsiveImageCropper();
});

!function (e) {
var t = function () {};
t.prototype = {targetElements: void 0, options: void 0, run: function (e) {
var t = this;
this.targetElements = new Array, e.each(function (e) {
var i = jQuery(this);
i.css({display: "none"});
var a = new Image;
a.onload = function () {
i.css({position: "absolute"}), t.targetElements.push(i), t.croppingImageElement(i), i.css({display: "block"})
}, a.src = i.attr("src")
}), jQuery(window).resize(function (e) {
t.onResizeCallback()
})
}, onResizeCallback: function () {
var t = this;
e.each(this.targetElements, function (e) {
var i = this;
t.croppingImageElement(i)
})
}, croppingImageElement: function (t) {
var i, a;
t.data("crop-image-wrapped") ? (a = t.data("crop-image-outer"), i = t.data("crop-image-inner")) : (a = e("<div>"), i = e("<div>"), a.css({overflow: "hidden", margin: t.css("margin"), padding: t.css("padding")}), t.css({margin: 0, padding: 0}), i.css({position: "relative", overflow: "hidden"}), t.after(a), a.append(i), i.append(t), t.data("crop-image-outer", a), t.data("crop-image-inner", i), t.data("crop-image-wrapped", !0)), this.desideImageSizes(t)
}, desideImageSizes: function (e) {
var t = e.data("crop-image-outer"), i = e.data("crop-image-inner"), a = e.data("crop-image-ratio");
a || (a = 1);
var n = t.width() * a;
i.height(n), e.width(t.width()), e.height("auto"), e.css({position: "absolute", left: 0, top: -(e.height() - t.height()) / 2}), n > e.height() && (e.width("auto"), e.height(n), e.css({position: "absolute", left: -(e.width() - t.width()) / 2, top: 0}))
}, setOptions: function (e) {
this.options = e
}}, e.fn.responsiveImageCropper = function (i) {
var i = e.extend(e.fn.responsiveImageCropper.defaults, i), a = e(this);
return cropper = new t, cropper.setOptions(i), cropper.run(a), this
}, e.fn.responsiveImageCropper.defaults = {}
}(jQuery);