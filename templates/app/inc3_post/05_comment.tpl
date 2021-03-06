{% load static %}

<ol>

  {% for comment in comments %}
  <!-- Single Comment Area -->
  <li class="single_comment_area">
    <!-- Comment Content -->
    <div class="comment-content">
      <!-- Comment Meta -->
      <div class="comment-meta d-flex align-items-center justify-content-between">
        <p><a class="post-author">{{comment.name}}</a> on <a class="post-date">{{comment.comment_at}}</a></p>
        {% comment %}<a class="comment-reply btn world-btn">Reply</a>{% endcomment %}
      </div>
      <p>{{comment.body|safe}}</p>
    </div>
  </li>
  {% endfor %}

  {% comment %}
  <!-- Single Comment Area -->
  <li class="single_comment_area">
    <!-- Comment Content -->
    <div class="comment-content">
      <!-- Comment Meta -->
      <div class="comment-meta d-flex align-items-center justify-content-between">
        <p><a href="#" class="post-author">Katy Liu</a> on <a href="#" class="post-date">Sep 29, 2017 at 9:48 am</a></p>
        <a href="#" class="comment-reply btn world-btn">Reply</a>
      </div>
      <p>Pick the yellow peach that looks like a sunset with its red, orange, and pink coat skin, peel it off with your teeth. Sink them into unripened...</p>
    </div>
    <ol class="children">
      <li class="single_comment_area">
        <!-- Comment Content -->
        <div class="comment-content">
          <!-- Comment Meta -->
          <div class="comment-meta d-flex align-items-center justify-content-between">
            <p><a href="#" class="post-author">Katy Liu</a> on <a href="#" class="post-date">Sep 29, 2017 at 9:48 am</a></p>
            <a href="#" class="comment-reply btn world-btn">Reply</a>
          </div>
          <p>Pick the yellow peach that looks like a sunset with its red, orange, and pink coat skin, peel it off with your teeth. Sink them into unripened...</p>
        </div>
      </li>
    </ol>
  </li>
  {% endcomment %}

</ol>
