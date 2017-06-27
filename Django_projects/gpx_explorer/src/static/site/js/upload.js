@import "//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css";

html, body{
    height:100%;		/* For full height images */
}

.starter-template {
  padding: 40px 15px;
  text-align: center;
}

.footer {
  padding-top: 40px;
  padding-bottom: 40px;
  margin-top: 40px;
  border-top: 1px solid #eee;
}

.alert {
    margin-top: 55px;
    margin-bottom: 0;
}

body>.navbar-transparent {
    background-color: transparent;
    border-color: transparent;
    box-shadow: none;
}

.navbar-transparent .navbar-nav > .active > a {
    background-color: transparent;
}

.navbar-form {
    margin-right: 0;
}

.navbar-nav>li>a.profile-menu {
    padding-top: 10px;
    padding-bottom: 10px;
}

.navbar-nav>.btn{
    margin-top:10px;
    margin-right: 1.7em;
}

.navbar-nav > li > a {
    font-size: 16px;
}

.navbar-brand {
    font-weight: bold;
}

.navbar-brand > img {
    float: left;
    margin-right: 10px;
}

.btn {
    background-image: none;
    -webkit-box-shadow: 0px 1px 0px #ddd;
    -moz-box-shadow: 0px 1px 0px #ddd;
    box-shadow: 0px 1px 0px #ddd;
}

/* Home page styling */
.corporate-jumbo {
    background-image: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0)),
      url("/static/site/img/banner.jpg");
    background-repeat: no-repeat;
    background-position: 80% center;
    background-attachment: fixed;
    -webkit-background-size: cover;
    background-size: cover;
    color: #f5f5f5;
    padding: 10em 0;
    margin-bottom: 0;
    height: 100%;
}

.corporate-jumbo .well {
    background-color: rgba(245, 245, 245, .7);
}

.corporate-jumbo p, .corporate-jumbo h1 {
    color: #eee;
    text-shadow: 0px 0px 2px black;
}

.corporate-jumbo p {
    font-weight: 500;
}

.corporate-jumbo .well legend {
    color: #333;
}

.corporate-jumbo > .container {
    display: block;
    position: absolute;
    bottom: 2em;
    left: 15px;
}

.contact-banner {
    padding: 100px 0;
    background: #e0e0e0;
    margin-top: 100px;
}

.footer a:hover {
    text-decoration: none;
}

/* About page styling */
#sec1 {
    background:url("/static/site/img/ribbon.jpg");
    background-size: cover;
    background-position: 0% 30%;
    opacity:0.35;
}

#sec12 {
    background:url(
        data:image/png;
        base64,
        iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAJklEQVQIW2NkAIILFy78NzAwYATRjCABZEGwAEwFiA1WBlIOUwkA72gTdDIYVO4AAAAASUVORK5CYII=
        )
        repeat;
}

/* Profile page styling */
.profile-head {
    background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAJklEQVQIW2NkAIILFy78NzAwYATRjCABZEGwAEwFiA1WBlIOUwkA72gTdDIYVO4AAAAASUVORK5CYII=) repeat;
    padding: 70px 0px 30px 20px;
}
.profile-body {
    padding: 4px 0px;
}

.text-page {
    padding: 120px 0;
}

#map-outer {
    height: 440px;
    padding: 40px 20px;
    margin-bottom: 20px;
    background-color:#FFF
}

#map-container {
    height: 400px
}

.img-dim {
    opacity: 0.5;
    box-shadow: inset 0px 0px 64px 64px #EA1717, 0px 0px 4px 4px #EA1717;
}

/* Authentication forms */
.form-box form,
.form-box .form-message {
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}

.form-box form .checkbox {
  margin-bottom: 10px;
}

.form-box form .checkbox {
  font-weight: normal;
}

.form-box form .form-control {
  position: relative;
  height: auto;
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
  padding: 10px;
  font-size: 16px;
}

.form-box form .form-control:focus {
  z-index: 2;
}