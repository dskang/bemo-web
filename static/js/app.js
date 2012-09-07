function screen(s) {
  $('.overlay .phone .screen')
    .fadeOut(300, function() {
      $(this).attr('style', 'background-image: url(' + s + ');');
    });
}

$(function() {
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

  $('.email-form').submit(function() {
      var url = $(this).attr('action');
      var success = function() {
        alert('Thanks for signing up!');
        // Clear email field
        $('.email-form .email').val('');
      };
      var error = function() {
        alert('Please enter a valid email.');
      }
      // Submit form via ajax
      $.ajax({
        type: 'POST',
        url: url,
        data: $(this).serialize(),
        success: success,
        error: error
      });
      return false;
    });
});
