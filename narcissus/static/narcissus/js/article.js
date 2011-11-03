$(function() {
  $('#article_description_input').hide();
  $('#article_show_description').click(function() {
    $('#article_description_input').toggle(500);
    return false;
  });
});