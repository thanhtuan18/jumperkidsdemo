$(document).ready(function (){
   $(".smooth-scroll").click(function (){
       $('html, body').animate({
           scrollTop: $("#link-banner").offset().top
       }, 500);
   });
});
