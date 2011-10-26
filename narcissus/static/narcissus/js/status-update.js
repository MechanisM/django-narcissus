$(function() {
  $("#status-count").twipsy({
    placement: 'left'
  })
  
  // Character count
  $("#status-update").bind('keyup, keydown', function() {
    var max = 300;
    var remaining = max - $(this).val().length;
    $('#status-count').text(remaining);
    
    if (remaining > 0) {
      $('#status-count').removeClass('error');
    } else {
      $('#status-count').addClass('error');
    }
  });
});