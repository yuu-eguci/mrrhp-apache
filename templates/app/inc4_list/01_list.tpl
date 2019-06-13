{% load static %}
 
<div class="world-catagory-area">

  {% for y in posts_dic.keys %}
    <ul class="nav nav-tabs">
      <li class="title">{{y}}</li>
    </ul>
    <div class="tab-content mb-30">
      <div class="row post-list-row">
        {% with posts_dic|ref_dic:y as posts %}
        {% for post in posts %}
        <div class="col-12">
          <div class="single-blog-post post-style-2 d-flex align-items-center click-to-link">
            <div class="post-content post-list-content-wrapper">
              <a href="/{{lang}}/{{post.code}}" class="headline">
                <h5 class="mt-15">
                  ({{post.publish_at}}) {{post.title}}
                </h5>
              </a>
              <ul class="post-tags">
                <li><a href="/{{lang}}/tags/{{post.tag.code}}">{{post.tag.name}}</a></li>
              </ul>
            </div>
          </div>
        </div>
        {% endfor %}
        {% endwith %}
      </div>
    </div>
  {% endfor %}
</div>
