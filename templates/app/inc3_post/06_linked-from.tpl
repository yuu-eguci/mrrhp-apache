{% load static %}

<p>以下の記事からリンクされています</p>
<div class="tab-content mb-30">
  <div class="row post-list-row">
    {% for post in linked_from %}
    <div class="col-12">
      <div class="single-blog-post post-style-2 d-flex align-items-center click-to-link">
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
  </div>
</div>
