var DashboardForm = Class.$extend({
  
  __init__ : function(posttype, form_selector) {
    var self = this;
    
    self.posttype = posttype;
    self.$form = $(form_selector);
    self.$form.submit(function(e) {
      self.submit();
      return false;
    });
    
    $('.alert-message').alert();
    $('.tabs').tabs();
  },
  
  submit: function() {
    var self = this;
    
    self.clear_errors();
    
    self.$form.backdrop({}, function() {
      self.$form.spin();
      
      $.ajax({
        type: 'POST',
        url: self.$form.attr('action'),
        data: self.$form.serialize(),
        success: function(data) {
          self.$form.spin(false);
          self.$form.backdrop();
          
          if (data.success) {
            self.valid_form(data);
          } else {
            self.invalid_form(data);
          }
        },
        error: function(data) {
          self.$form.spin(false);
          self.$form.backdrop();
        },
        dataType: 'json'
      });
    });
    
    return false;
  },
  
  valid_form: function(data) {
    var self = this;
  },
  
  invalid_form: function(data) {
    var self = this;
    
    $.each(data.errors, function(field, errors) {
      $input = $('#id_' + self.posttype + '_' + field);
      $input.addClass('error').parent().parent().addClass('error');
      $input.after('<span class="help-inline">' + errors.join(' ') + '</span>');
    });
  },
  
  clear_errors: function(data) {
    $('div.input, div.input-prepend').each(function() {
      $(this).parent().removeClass('error');
      $(this).children('input, textarea, select').removeClass('error')
        .next('span.help-inline').remove();
    });
  }
  
});
