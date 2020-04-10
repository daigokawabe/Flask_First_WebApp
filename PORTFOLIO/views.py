from .database import db
from .app import app
from flask import Flask, render_template, request, redirect, url_for, session
from .models import Login, User, Post
import os

app.config["IMAGE_UPLOADS"] = 'static/img'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signupform')
def signupform():
    return render_template("signup.html")

@app.route('/signup', methods =['POST', 'GET'])
def signup():
    if request.method == 'POST':
        login = Login(username = request.form['username'], password=request.form['password'])

        try:
            db.session.add(login)
            db.session.commit()

            db.session.refresh(login)
            print(login.id)

            user = User(login_id=login.id, email=request.form['email'], name=request.form['name'], username=request.form['username'], password=request.form['password'])
            db.session.add(user)
            db.session.commit()

            print('finish')
            return redirect('/login')
        except:
            return 'Error'
    else:
        return render_template('signup.html')

@app.route('/login', methods =['POST','GET'])
def login():
    if request.method == 'POST':
        login = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if login:
            session['id'] = login.id        # save to computer
            print(login.id)
            return redirect('/topform')
            # return render_template('top.html', userinfo=login)
        else:
            return 'Error in loggin'
    else:
        return render_template('login.html')

@app.route('/topform')
def topform():
    if 'id' in session:
        login_id = session['id'] 
        user = User.query.filter_by(id=login_id).first()
        # post_username = user.username
        post = Post.query.order_by(Post.updated_at.desc()).all()
        friend = User.query.order_by(User.username).all()
        post_all_user = Post.query.order_by(Post.updated_at.desc()).all()
        return render_template('top.html', userinfo=user, posts=post, friends=friend, postsalluser=post_all_user)
    else:
        return 'Error'


@app.route('/profileform')
def profileform():
    if 'id' in session:
        login_id = session['id'] 
        user = User.query.filter_by(id=login_id).first()
        post = Post.query.filter_by(login_id=login_id).order_by(Post.updated_at.desc())
        return render_template('top_profile.html', userinfo=user, posts=post)
    else:
        return 'Error'
    user = User.query.get_or_404(id)
    return render_template("top_profile.html", userinfo=user)
# @app.route('/profileform/<int:id>')
# def profileform(id):
#     user = User.query.get_or_404(id)
#     return render_template("top_profile.html", userinfo=user)


@app.route('/list_post')
# @login_required
def list_post():
    if 'id' in session:
        login_id = session['id']
        post = Post.query.order_by(Post.id.desc()).all()
        user = User.query.filter_by(id=login_id).first()
        
        return render_template('top_profile.html', posts=post, userinfo=user)

@app.route('/upload', methods =['POST','GET'])
def upload():
    login_id = session['id']
    if request.method == 'POST':
        images = request.files['image']
        pic_name = images.filename
        images.save(os.path.join(app.config["IMAGE_UPLOADS"], images.filename))
        user = User.query.filter_by(id=login_id).first()
        # print(username)
        upload = Post(login_id=login_id, tagpost=request.form['tag'], photopost=pic_name, username=user.username)
        print(upload)
        try:
            db.session.add(upload)
            db.session.commit()
            print('New Photo was successfully posted')
            # post = Post.query.order_by(Post.id.desc()).all()
            print(upload)
            return redirect('/list_post')
            # return render_template('top_profile.html', posts=post)
        except:
            return 'Error'
    else:
        # login_id = session['id']
        user = User.query.filter_by(id=login_id).first()
        return render_template('top_profile_upload.html', userinfo=user)






# ############ post ###############
# @app.route('/post/<int:id>')
# def post(id):
#     if request.method == 'POST':
#         post = Post(login_id=id, tag = request.form['text'])
#         print(id)
#         try:
#             db.session.add(post)
#             db.session.commit()
#             # print(todo.id)
#             return redirect('/viewtimeline') 
#         except:
#             return 'Error'
#     else:
#         return render_template('top_profile.html')

# @app.route('/viewtimeline')
# def viewtimeline():
#     post = Post.query.order_by(Post.login_id).all()
#     return render_template('top_prifile.html', usersuserinfo=post)


#########################################



# @app.route('/pytweets/<int:pytweet_id>')
# # @login_required
# def show_pytweet(pytweet_id):
#     pytweet = Pytweet.query.get(pytweet_id)
#     return render_template('pytweet/show.html', pytweet=pytweet)


# @app.route('/pytweets/new/', methods=['GET', 'POST'])
# # @login_required
# def create_pytweet():
#     form = PytweetForm()
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             pytweet = Pytweet(user=current_user,
#                               body=form.body.data)
#             db.session.add(pytweet)
#             db.session.commit()
#             flash('New Pytweet was successfully posted')
#             return redirect(url_for('list_pytweets'))

#     return render_template('pytweet/edit.html', form=form)
#########################################


# ######### profile-edit ############

@app.route('/profile-edit/<int:id>', methods=['POST','GET'])
def profile_edit(id):
    user = User.query.get_or_404(id)
    post = Post.query.order_by(Post.updated_at.desc()).all()

    if request.method == 'POST':
        user.email = request.form['email']
        user.name = request.form['name']
        user.username = request.form['username']
        user.password = request.form['password']

        try:
            db.session.commit()
            return render_template('top_profile.html', userinfo=user, posts=post)
        except:
            return 'Error in updating'
    else:
        return render_template('top-profile-edit.html', user=user, posts=post)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

