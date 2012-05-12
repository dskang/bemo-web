function screen(s) {
    $('.overlay .phone .screen')
    .fadeOut(300, function() {
              $(this).attr('style', 'background-image: url(' + s + ');');
          });

}

$(document).ready(
    function() {

        $('[data-spy="scroll"]').each(function () {
                          var $spy = $(this).scrollspy('refresh')
                      });
        var default_screen = 'screen_push.png';
        screen(default_screen);

        $('.nav')
        .bind('activate', function(e) {
              screen(
                  $(e.target).find('a').attr('data-screen')
                  );
              });
    });
