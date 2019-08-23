{% load static %}

<!-- ***** Footer Area Start ***** -->
<footer class="footer-area custom-footer-area">
  <div class="container">
    <div class="row">
      <div class="col-12 col-md-4">
        <div class="footer-single-widget">
          <a href="/{{lang}}/">
            <img src="{% static 'app/img/core/mrrhp-logo-black.png' %}" alt="">
          </a>
          <div class="copywrite-text mt-30">
            <p>
              {{site_version}}
            </p>
            <p>
              Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved
            </p>
            <p>
              This site is made by Midoriiro
            </p>
            <p>
              This template is made by <a href="https://colorlib.com" target="_blank">Colorlib</a>
            </p>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-8">
        <div class="footer-single-widget">
          <ul class="footer-menu d-flex justify-content-between">
            {% for tag in tags %}
              <li>
                <a href="/{{lang}}/tags/{{tag.code}}">
                  <i class="fa fa-tag"></i> {{tag.name}}
                </a>
              </li>
            {% endfor %}
          </ul>
        </div>
      </div>
    </div>
  </div>
</footer>
<!-- ***** Footer Area End ***** -->

<!-- jQuery (Necessary for All JavaScript Plugins) -->
<script src="{% static 'app/js/jquery/jquery-2.2.4.min.js' %}"></script>
<!-- Popper js -->
<script src="{% static 'app/js/popper.min.js' %}"></script>
<!-- Bootstrap js -->
<script src="{% static 'app/js/bootstrap.min.js' %}"></script>
<!-- Plugins js -->
<script src="{% static 'app/js/plugins.js' %}"></script>
<!-- Active js -->
<script src="{% static 'app/js/active.js' %}"></script>
<!-- highlight.js -->
<!-- https://laboradian.com/how-to-use-highlightjs/ -->
<script src="{% static 'app/vendor/highlight/highlight.pack.js' %}"></script>
<script>hljs.initHighlightingOnLoad();</script>
<!-- Click div to click link -->
<script>
  $(function() {
    $('.click-to-link').click(function() {
      this.querySelector('div a').click();
    });
  });
</script>
<!-- Just for kidding -->
<script>
  var originalPageTitle = document.title;

  function switchTitle() {
    document.title = document.hidden ? 'もどってきて♥' : originalPageTitle;
  }

  $(function () {
    $(document).on('visibilitychange', function () {
      setTimeout(switchTitle, 200);
    });
  });
</script>
