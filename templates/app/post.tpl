{% load static %}

<!DOCTYPE html>
<html lang="{{lang}}">

<head>
  {% include 'app/inc1_cmn/01_head.tpl' %}
</head>

<body>
  {% include 'app/inc1_cmn/02_header-area.tpl' %}
  {% include 'app/inc3_post/01_hero-area.tpl' %}

  <div class="main-content-wrapper section-padding-50">
    <div class="container">

      {% comment %} Row1 {% endcomment %}
      <div class="row justify-content-center">
        {% comment %} Left Area {% endcomment %}
        <div class="col-12 col-lg-10 p-0-sp">
          <div class="single-blog-content mb-70">
            {% include 'app/inc3_post/02_content.tpl' %}
          </div>
        </div>
        {% comment %} Right Area {% endcomment %}
        <div class="d-none d-lg-block col-lg-2">
          <div class="single-blog-content sticky-top">
            <div class="toc-wrapper">
              <div class="markdown-body">
                {% comment %} The area is where div.toc is moved in by JS. {% endcomment %}
              </div>
            </div>
          </div>
        </div>
      </div>
      {% comment %} Row1 ends {% endcomment %}

      {% comment %} Row2 {% endcomment %}
      {% if linked_from %}
      <div class="row justify-content-center">
        <div class="col-12 col-lg-10 p-0-sp">
          {% include 'app/inc3_post/06_linked-from.tpl' %}
        </div>
        <div class="col-12 col-md-2 col-lg-2">
        </div>
      </div>
      {% endif %}
      {% comment %} Row2 ends {% endcomment %}

      {% comment %} Row3 {% endcomment %}
      <div class="row justify-content-center">
        {% include 'app/inc3_post/03_related-post.tpl' %}
      </div>
      {% comment %} Row3 ends {% endcomment %}

      {% comment %} Row4 
      <div class="row">
        <div class="col-12 col-lg-8">
          <div class="post-a-comment-area mt-70">
            {% include 'app/inc3_post/04_contact.tpl' %}
          </div>
        </div>
        {% endcomment %}

        <div class="col-12 col-lg-8">
          <!-- Comment Area Start -->
          <div class="comment_area clearfix mt-70">
            {% include 'app/inc3_post/05_comment.tpl' %}
          </div>
        </div>
      </div>
      {% comment %} Row4 ends {% endcomment %}

    </div>
  </div>

  {% include 'app/inc1_cmn/09_footer-area.tpl' %}
  {% include 'app/inc3_post/09_link-button.tpl' %}
</body>

</html>