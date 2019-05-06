{% load static %}

<!-- Widget Area -->
{% if pickup_post %}
<div class="sidebar-widget-area">
  <h5 class="title">Pickup</h5>
  <div class="widget-content">
    <div class="single-blog-post todays-pick">
      <div class="post-thumbnail">
        <a href="/{{lang}}/{{pickup_post.code}}">
          <img src="{% if pickup_post.thumbnail %}/media/thumbnail/{{pickup_post.thumbnail}}{% else %}{% static 'app/img/core/blog-img-size.jpg' %}{% endif %}" alt="">
        </a>
        <div class="post-cta"><a href="/{{lang}}/tags/{{pickup_post.tag.code}}">{{pickup_post.tag.name}}</a></div>
      </div>
      <div class="post-content px-0 pb-0">
        <a href="/{{lang}}/{{pickup_post.code}}" class="headline">
          <h5>{{pickup_post.title}}</h5>
        </a>
        <div class="post-meta">
          <p><a class="post-date">{{pickup_post.publish_at}}</a></p>
        </div>
      </div>
    </div>
  </div>
</div><!-- Widget Area Ends -->
{% endif %}
