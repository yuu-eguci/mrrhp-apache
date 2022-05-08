{% load static %}

<div class="world-catagory-area">
  <ul class="nav nav-tabs" id="myTab" role="tablist">
    <li class="title">Latest</li>
  </ul>
  <div class="tab-content" id="myTabContent">
    <div class="tab-pane fade show active">

      {% for post in latest_posts %}
        <!-- Single Blog Post -->
        <div class="single-blog-post post-style-4 d-flex align-items-center click-to-link">
          <!-- Post Thumbnail -->
          <div class="post-thumbnail">
            <a href="/{{lang}}/{{post.code}}">
              <img src="{% if post.thumbnail %}/media/thumbnail/{{post.thumbnail}}{% else %}{% static 'app/img/core/blog-img-size.jpg' %}{% endif %}" alt="">
            </a>
          </div>
          <!-- Post Content -->
          <div class="post-content">
            <a href="/{{lang}}/{{post.code}}" class="headline">
              <h5>{{post.title}}</h5>
            </a>
            <!-- Post Meta -->
            <div class="post-meta">
              <p>
                <a class="post-date">{{post.publish_at_ago}}</a>
                <a class="post-author" href="/{{lang}}/tags/{{post.tag.code}}">{{post.tag.name}}</a>
              </p>
            </div>
          </div>
        </div>
      {% endfor %}

      <div class="single-blog-post text-center mt-3 p-3 click-to-link">
        <a href="/{{lang}}/years/{{latest_year}}">
          <i class="fas fa-calendar-alt"></i>
          {{latest_year}}年一覧
        </a>
    </div>
    </div>
  </div>
</div>
