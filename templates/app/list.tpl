{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
  {% include 'app/inc1_cmn/01_head.tpl' %}
</head>

<body>
  {% include 'app/inc1_cmn/02_header-area.tpl' %}
  {% include 'app/inc3_post/01_hero-area.tpl' %}

  <div class="main-content-wrapper section-padding-50">
    <div class="container">
      <div class="row justify-content-center">
        <!-- ============= Post Content Area ============= -->
        <div class="col-12 col-lg-10">
          <div class="post-content-area mb-50">
            {% include 'app/inc4_list/01_list.tpl' %}
          </div>
        </div>

        <!-- ========== Sidebar Area ========== -->
        <div class="col-12 col-md-2 col-lg-2">
        </div>
      </div>
    </div>
  </div>

  {% include 'app/inc1_cmn/09_footer-area.tpl' %}
</body>

</html>