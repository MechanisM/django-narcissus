$(function() {
  $('.alert-message').alert();
  $('.tabs').tabs();
  
  $('#update-form').submit(function() {
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function(data) {
        
      },
      error: function(data) {
        
      },
      dataType: 'json'
    });
    
    return false;
  });
})

