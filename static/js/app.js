function screen(s) {
  $('.overlay .phone .screen')
    .fadeOut(300, function() {
      $(this).attr('style', 'background-image: url(' + s + ');');
    });
}

$(document).ready(
  function() {
    var default_screen = '/static/images/screen_push.png';
    screen(default_screen);

    $('[data-spy="scroll"]').each(function () {
      var $spy = $(this).scrollspy()
    });

    $('.nav')
      .bind('activate', function(e) {
        screen(
          $(e.target).find('a').attr('data-screen')
        );
      });
  });
