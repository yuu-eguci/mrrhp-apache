{% load static %}

{% for post in related_posts %}
<!-- ========== Single Blog Post ========== -->
<div class="col-12 col-md-6 col-lg-4">
  <div class="single-blog-post post-style-3">
    <div class="post-thumbnail">
      <img src="/media/thumbnail/{{post.thumbnail}}" alt="">
      <div class="post-content d-flex align-items-center justify-content-between">
        <div class="post-tag"><a href="/{{lang}}/tags/{{post.tag.code}}">{{post.tag.name}}</a></div>
        <a href="/{{lang}}/{{post.code}}" class="headline">
          <h5>{{post.title}}</h5>
        </a>
        <div class="post-meta">
          <p><a href="#" class="post-date">{{post.publish_at}}</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
{% endfor %}
