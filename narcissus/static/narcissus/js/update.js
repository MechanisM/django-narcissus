$(function() {
  var UpdateForm = DashboardForm.$extend({

    __init__: function(posttype, form_selector, url_value) {
      var self = this;

      $("#status_count").twipsy({
        placement: 'left'
      })

      $(url_value).bind('keyup keydown', self.character_count);

      self.$super(posttype, form_selector, url_value);
    },

    character_count: function() {
      var max = 300;
      var remaining = max - $(this).val().length;
      $('#status_count').text(remaining);

      if (remaining > 0) {
        $('#status_count').removeClass('error');
      } else {
        $('#status_count').addClass('error');
      }
    }

  });

  var update_form = UpdateForm('update', '#update-form', '#id_update_message');
});
