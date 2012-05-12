function screen(s) {
  $('.overlay .phone .screen')
    .fadeOut(300, function() {
      $(this).attr('style', 'background-image: url(' + s + ');');
      console.log(this);
    });
}

$(document).ready(
  function() {
    var default_screen = 'images/screen_push.png';
    screen(default_screen);

    $('[data-spy="scroll"]').each(function () {
      var $spy = $(this).scrollspy('refresh')
    });

    $('.nav')
      .bind('activate', function(e) {
        screen(
          $(e.target).find('a').attr('data-screen')
        );
      });
  });
