{% load static %}

<!-- ***** Footer Area Start ***** -->
<footer class="footer-area">
  <div class="container">
    <div class="row">
      <div class="col-12 col-md-4">
        <div class="footer-single-widget">
          <a href="#"><img src="{% static 'app/img/core/mrrhp-logo-white.png' %}" alt=""></a>
          <div class="copywrite-text mt-30">
            <p>
              Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
            </p>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-8">
        <div class="footer-single-widget">
          <ul class="footer-menu d-flex justify-content-between">
            <li><a href="#">Home</a></li>
            <li><a href="#">Fashion</a></li>
            <li><a href="#">Lifestyle</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Gadgets</a></li>
            <li><a href="#">Video</a></li>
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
