{% load static %}

<!-- Widget Area -->
<div class="sidebar-widget-area">
  <h5 class="title">緑色 @midori-mate</h5>
  <div class="widget-content">
    <p class="centering">
      <img src="{% static 'app/img/core/midori-icon.jpg' %}" style="width:100px;">
    </p>
    <p>
      {% if lang == 'ja' %}
        緑色さんの多目的ブログ、みろりえいちぴーです。 ごゆるりとおくつろぎあさーせ。
      {% else %}
        Midori's blog for multi-purposes: Mirori-HP. Welcome, strangers.
      {% endif %}
    </p>
    <div class="social-area d-flex justify-content-between">
      <a href="https://gitlab.com/midori-mate"><i class="fa fa-gitlab"></i></a>
      <a href="https://twitter.com/miroriiro"><i class="fa fa-twitter"></i></a>
      <a href="https://www.instagram.com/hitorenshuu/"><i class="fa fa-instagram"></i></a>
      <a><i class="fa fa-ban"></i></a>
      <a><i class="fa fa-ban"></i></a>
      <a><i class="fa fa-ban"></i></a>
    </div>
  </div>
</div><!-- Widget Area Ends -->
