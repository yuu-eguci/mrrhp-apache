{% load static %}

<div class="title">
  <h5>Recently updated</h5>
</div>

{% for post in recently_updated_posts %}
<div class="single-blog-post post-style-2 d-flex align-items-center widget-post">
  <div class="post-thumbnail">
    <a href="/{{lang}}/{{post.code}}">
      <img src="{% static 'app/img/core/right-thumbnail.jpg' %}" alt="">
    </a>
  </div>
  <div class="post-content">
    <a href="/{{lang}}/{{post.code}}" class="headline">
      <h5 class="mb-0">{{post.title}}</h5>
    </a>
  </div>
</div>
{% endfor %}
