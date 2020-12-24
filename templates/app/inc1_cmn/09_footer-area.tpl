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
              Copyright &copy;
              <span class="full-year"></span> All rights reserved
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
                  <i class="fas fa-tag"></i> {{tag.name}}
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
<script defer src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
<!-- Popper js -->
<script defer src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
<!-- Bootstrap js -->
<script defer src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js"></script>
<!-- Plugins js -->
<script defer src="{% static 'app/js/plugins.js' %}"></script>
<!-- highlight.js -->
<!-- https://laboradian.com/how-to-use-highlightjs/ -->
<script defer src="{% static 'app/vendor/highlight/highlight.pack.js' %}"></script>
<!-- Active js -->
<script defer src="{% static 'app/js/active.js' %}"></script>
