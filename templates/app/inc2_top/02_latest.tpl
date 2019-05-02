{% load static %}

<div class="world-catagory-area">
  <ul class="nav nav-tabs" id="myTab" role="tablist">
    <li class="title">Latest</li>
  </ul>
  <div class="tab-content" id="myTabContent">
    <div class="tab-pane fade show active">

      {% for post in latest_posts %}
        <!-- Single Blog Post -->
        <div class="single-blog-post post-style-4 d-flex align-items-center">
          <!-- Post Thumbnail -->
          <div class="post-thumbnail">
            <img src="{% if post.thumbnail %}/media/thumbnail/{{post.thumbnail}}{% else %}{% static 'app/img/core/blog-img-size.jpg' %}{% endif %}" alt="">
          </div>
          <!-- Post Content -->
          <div class="post-content">
            <a href="/{{lang}}/{{post.code}}" class="headline">
              <h5>{{post.title}}</h5>
            </a>
            <!-- Post Meta -->
            <div class="post-meta">
              <p><a class="post-date">{{post.publish_at}}</a></p>
            </div>
          </div>
        </div>
      {% endfor %}

    </div>
  </div>
</div>
