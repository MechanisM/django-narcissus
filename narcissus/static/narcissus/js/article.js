$(function() {
  $('#article-description-input').hide();
  $('#article-show-description').click(function() {
    $('#article-description-input').toggle(500);
    return false;
  });
});