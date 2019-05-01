{% load static %}
 
<div class="world-catagory-area">

  {% for y in posts_by_year.keys %}
    <ul class="nav nav-tabs">
      <li class="title">{{y}}</li>
    </ul>
    <div class="tab-content mb-30">
      <div class="row post-list-row">
        {% with posts_by_year|ref_dic:y as posts %}
        {% for post in posts %}
        <div class="col-12">
          <div class="single-blog-post post-style-2 d-flex align-items-center">
            <div class="post-content">
              <div class="post-meta">
                <p>
                </p>
              </div>
              <a href="/{{lang}}/{{post.code}}" class="headline">
                <h5 class="mt-15">({{post.publish_at}}) {{post.title}}</h5>
              </a>
            </div>
          </div>
        </div>
        {% endfor %}
        {% endwith %}
      </div>
    </div>
  {% endfor %}
</div>
