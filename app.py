from flask import Flask, render_template, redirect, url_for, request, session
from models.post import Post
import mlab
from mongoengine import DoesNotExist
from slugify.slugify import slugify
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "xichdunhunnhaytopdauthitruonghanoi@@@@2018"

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/xich-du-nhun-nhay-jumperkids')
def sp():
    return render_template('page_sp.html')

@app.route('/new_post', methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template('new_post.html')
    elif request.method == "POST":
        form = request.form
        title = form["title"]
        content = form["content"]
        link = slugify(title)
        try:
            bai_viet = Post.objects().get(link = link)
            if link == bai_viet.link:
                return "Tiêu đề đã tồn tại, vui lòng đặt tiêu đề mới"
        except DoesNotExist:
            new_post = Post(title=title, link=link, content=content)
            new_post.save()
            return "bài viết đã được tạo"

@app.route('/<link_to_find>')
def link(link_to_find):
    try:
        # get_info = assertRaises(DoesNotExist, Post.objects.get, link = link_to_find)
        get_info = Post.objects().get(link = link_to_find)

        path = "./templates/html_file.html"
        html_str = get_info.content
        html_file= open(path,"w", encoding='utf-8')
        html_file.write(html_str)
        html_file.close()

        return render_template('page_bai_viet.html', get_info = get_info)
    except DoesNotExist:
        return "Lỗi 404! Vui lòng kiểm tra lại đường link."

@app.route('/admin')
def admin():
    if "logged_in" in session and session["logged_in"] == True:
        posts = Post.objects()
        return render_template('admin.html', posts = posts)
    else:
        return redirect(url_for("login"))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        if username == "admin" and password == "tuan@2018":
            session["logged_in"] = True
            return redirect(url_for("admin"))
        else:
            return "Sai mật khẩu, vui lòng đăng nhập lại"

@app.route('/update/<link_to_find2>', methods=["GET", "POST"])
def update(link_to_find2):
    get_post = Post.objects().get(link = link_to_find2)
    if request.method == "GET":
        return render_template('update.html', get_post=get_post)
    elif request.method == "POST":
        form = request.form
        title = form["title"]
        content = form["content"]
        get_post.update(set__title=title, set__content=content)
        return "Bài viết đã cập nhật"

if __name__ == '__main__':
  app.run(debug=True)
