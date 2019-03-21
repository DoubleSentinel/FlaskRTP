// This document contains various MaterializeCSS JS initialization functions

//initializing parallax for
$(document).ready(function(){
    $('.parallax').parallax();
  });

// initialize mobile navbar
$(document).ready(function(){
  $('.sidenav').sidenav();
});

// initialize dropdown triggers
$(document).ready(function(){
  $(".dropdown-trigger").dropdown();
});

// initialize carousel
$(document).ready(function(){
    $('.carousel').carousel();
  });

// initialize carousel-slider fullwidth to true
$('.carousel.carousel-slider').carousel({
   fullWidth: true,
   indicators: true
 });

// initialize material boxed media
$(document).ready(function(){
   $('.materialboxed').materialbox();
 });

// initialize collapsible lists
$(document).ready(function(){
  $('.collapsible').collapsible();
});
