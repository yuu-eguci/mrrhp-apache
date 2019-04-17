{% load static %}

<h5>Get in Touch</h5>
<!-- Contact Form -->
<form action="#" method="post">
  <div class="row">
    <div class="col-12 col-md-6">
      <div class="group">
        <input type="text" name="name" id="name" required>
        <span class="highlight"></span>
        <span class="bar"></span>
        <label>Enter your name</label>
      </div>
    </div>
    <div class="col-12 col-md-6">
      <div class="group">
        <input type="email" name="email" id="email" required>
        <span class="highlight"></span>
        <span class="bar"></span>
        <label>Enter your email</label>
      </div>
    </div>
    <div class="col-12">
      <div class="group">
        <textarea name="message" id="message" required></textarea>
        <span class="highlight"></span>
        <span class="bar"></span>
        <label>Enter your comment</label>
      </div>
    </div>
    <div class="col-12">
      <button type="submit" class="btn world-btn">Post comment</button>
    </div>
  </div>
</form>
