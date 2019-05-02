{% load static %}

<!DOCTYPE html>
<html lang="{{lang}}">

<head>
  {% include 'app/inc1_cmn/01_head.tpl' %}
</head>

<body>
  <h1 style="display:none;">みろりHP</h1>
  {% include 'app/inc1_cmn/02_header-area.tpl' %}
  {% include 'app/inc2_top/01_hero-area.tpl' %}

  <div class="main-content-wrapper section-padding-50">
    <div class="container">

      {% comment %} Row1 {% endcomment %}
      <div class="row justify-content-center">

        {% comment %} Left Area {% endcomment %}
        <div class="col-12 col-lg-8">
          <div class="post-content-area mb-100">
            {% include 'app/inc2_top/02_latest.tpl' %}
          </div>
        </div>

        {% comment %} Right Area {% endcomment %}
        <div class="col-12 col-md-8 col-lg-4">
          <div class="post-sidebar-area mb-50">
            {% include 'app/inc2_top/03_writer.tpl' %}
            {% include 'app/inc2_top/04_pickup.tpl' %}
          </div>
        </div>

      </div>
      {% comment %} Row1 ends {% endcomment %}

      {% comment %} Row2 {% endcomment %}
      <div class="row justify-content-center">
        {% include 'app/inc2_top/05_recommend.tpl' %}
      </div>
      {% comment %} Row2 ends {% endcomment %}

      {% comment %} Row3 {% endcomment %}
      <div class="world-latest-articles">
        <div class="row">
          <div class="col-12 col-lg-8">
            {% include 'app/inc2_top/06_activity.tpl' %}
          </div>
          <div class="col-12 col-lg-4">
            {% include 'app/inc2_top/07_updated.tpl' %}
          </div>
        </div>
      </div>

    </div><!-- container -->
  </div><!-- main-content-wrapper -->

  {% include 'app/inc1_cmn/09_footer-area.tpl' %}
</body>

</html>