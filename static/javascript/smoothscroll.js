$(document).ready(function (){
   $(".smooth-scroll").click(function (){
       $('html, body').animate({
           scrollTop: $("#teleport").offset().top
       }, 500);
   });
});
