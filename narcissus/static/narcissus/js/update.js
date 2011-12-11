$(function() {
  var UpdateForm = DashboardForm.$extend({

    __init__: function(posttype, form_selector) {
      var self = this;

      $("#status_count").twipsy({
        placement: 'left'
      })

      $("#id_update_message").bind('keyup, keydown', self.character_count)
        .bind('keyup, keydown', self.prefill_url);

      self.$super(posttype, form_selector);
    },

    character_count: function() {
      console.log(this);
      var max = 300;
      var remaining = max - $(this).val().length;
      $('#status_count').text(remaining);

      if (remaining > 0) {
        $('#status_count').removeClass('error');
      } else {
        $('#status_count').addClass('error');
      }
    },

    prefill_url: function() {
      $('#id_update_slug').val(URLify($(this).val(), 50));
    }

  });

  var update_form = UpdateForm('update', '#update-form');
});
