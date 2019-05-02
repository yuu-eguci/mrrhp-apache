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
      <div class="row justify-content-center">
        <!-- ============= Post Content Area ============= -->
        <div class="col-12 col-lg-10">
          <div class="post-content-area mb-50">

            <div class="world-catagory-area">
              <ul class="nav nav-tabs">
                <li class="title">{{message}}</li>
              </ul>
              <div class="tab-content mb-30">
                <div class="row post-list-row">
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
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- ========== Sidebar Area ========== -->
        <div class="col-12 col-md-2 col-lg-2">
        </div>
      </div>
    </div>
  </div>

  {% include 'app/inc1_cmn/09_footer-area.tpl' %}
</body>

</html>