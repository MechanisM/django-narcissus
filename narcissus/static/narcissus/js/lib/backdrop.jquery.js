/* Backdrop
 *
 * Set or clear a backdrop, with an optional callback on the end of the
 * animation.  Modified from Twitter's Bootstrap Modal class.
 */
(function($) {
  
  $.fn.backdrop = function(opts, callback) {
    var data = $(this).data(),
        transitionEnd,
        defaults = {
          "animate": true,
    			"static": true
    		},
    		settings = $.extend({}, defaults, opts);
    
      // set CSS transition event type
      if ( $.support.transition ) {
        transitionEnd = "TransitionEnd"
        if ( $.browser.webkit ) {
        	transitionEnd = "webkitTransitionEnd"
        } else if ( $.browser.mozilla ) {
        	transitionEnd = "transitionend"
        } else if ( $.browser.opera ) {
        	transitionEnd = "oTransitionEnd"
        }
      }
      
    if (data.backdrop) {
      // There's already a backdrop.  Kill it.
      data.backdrop.removeClass('in');

      function removeElement() {
        data.backdrop.remove();
        delete data.backdrop;
      }

      if ($.support.transition && data.backdrop.hasClass('fade')) {
        data.backdrop.one(transitionEnd, removeElement);
      } else {
        removeElement();
      }
      
    } else {
      var doAnimate = $.support.transition && settings.animate,
          fade = doAnimate ? 'fade' : '';

      data.backdrop = $('<div class="modal-backdrop ' + fade + '" />')
        .appendTo(document.body);

      if (!settings.static) {
        data.backdrop.click($.proxy(this.hide, this));
      }

      if (doAnimate) {
        data.backdrop[0].offsetWidth; // force reflow
      }

      data.backdrop.addClass('in');

      if (callback) {
        if (doAnimate) {
          data.backdrop.one(transitionEnd, callback);
        } else {
          callback();
        }
      }
    }
  }

})(jQuery);
