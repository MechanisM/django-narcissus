$(function() {
  $("#status_count").twipsy({
    placement: 'left'
  })
  
  // Character count
  $("#id_update_message").bind('keyup, keydown', function() {
    var max = 300;
    var remaining = max - $(this).val().length;
    $('#status_count').text(remaining);
    
    if (remaining > 0) {
      $('#status_count').removeClass('error');
    } else {
      $('#status_count').addClass('error');
    }
  });
});