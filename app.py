from flask import Flask, render_template, redirect, url_for, request, session
from models.post import Post
import mlab
from mongoengine import DoesNotExist
from slugify import slugify, Slugify, UniqueSlugify

app = Flask(__name__)

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

        list_link = []
        posts = Post.objects()
        for post in posts:
            list_link.append(post.link)

        slug = UniqueSlugify(uids=list_link, to_lower=True)
        link = slug(title)

        new_post = Post(title=title, link=link, content=content)
        new_post.save()

        return "bài viết đã được tạo"

@app.route('/<link_to_find>')
def link(link_to_find):
    try:
        # get_info = assertRaises(DoesNotExist, Post.objects.get, link = link_to_find)
        get_info = Post.objects().get(link = link_to_find)
        return render_template('page_bai_viet.html', get_info = get_info)
    except DoesNotExist:
        return "Lỗi 404! Vui lòng kiểm tra lại đường link."

@app.route('/admin')
def admin():
    posts = Post.objects()
    return render_template('admin.html', posts = posts)

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
