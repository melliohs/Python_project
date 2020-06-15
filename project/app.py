import os
import secrets
from PIL import Image
from flask import Flask, render_template, redirect, url_for, flash, session, request, jsonify
from data import db_session
from data.users import Сharacter, News, User, Guides
from forms import RegistrationForm, LoginForm, UpdateAccountForm, AddNewsForm, AddGuidesForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '804cf34dc523c19e4f1bd87a6c90459f'
db_session.global_init("db/game_portal.sqlite")
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



@app.route('/index')
def index():
    form = UpdateAccountForm()
    session = db_session.create_session()
    characters = session.query(Сharacter).all()
    news = session.query(News).all()
    image = url_for('static', filename='images/')
    bg = url_for('static', filename='images/bg/site-background.jpg')
    mini = url_for('static', filename='images/mini_jett.png')
    return render_template('index.html', characters=characters, image=image, news=news, bg=bg, mini=mini, form=form)



@app.route('/session_test/')
def session_test():
    if 'visits_count' in session:
        session['visits_count'] = session.get('visits_count') + 1
    else:
        session['visits_count'] = 1
    # дальше - код для вывода страницы



@app.route('/')
@app.route('/main')
def main():
    image = url_for('static', filename='images/')
    logo = url_for('static', filename='images/logo.png')
    bg = url_for('static', filename='images/bg/site-background.jpg')
    user = current_user
    return render_template('main.html',  image=image, news=news, bg=bg, logo=logo, user=user)

@app.route('/guides')
def guides():
    session = db_session.create_session()
    characters = session.query(Сharacter).all()
    guides = session.query(Guides).all()
    logo = url_for('static', filename='images/logo.png')
    image = url_for('static', filename='images/')
    mini = url_for('static', filename='images/mini_jett.png')
    return render_template('guides.html', guides=guides, characters=characters, image=image, logo=logo, mini=mini)



@app.route('/characters')
def characters():
    session = db_session.create_session()
    characters = session.query(Сharacter).all()
    logo = url_for('static', filename='images/logo.png')
    image = url_for('static', filename='images/')
    return render_template('characters.html', characters=characters, image=image, logo=logo)

@app.route('/character/<int:id>/')
def character(id):
    with app.app_context():
        session = db_session.create_session()
        character = session.query(Сharacter).all()
        image = url_for('static', filename='images/')
        logo = url_for('static', filename='images/logo.png')
        images = url_for('static', filename='images/abilities/jett/')
        video =  url_for('static', filename='images/abilities/jett/video/')
    return render_template('character.html', characters=character[id], image=image, images=images, video=video, logo=logo)

@app.route('/news')
def new():
    session = db_session.create_session()
    news = session.query(News).all()
    image = url_for('static', filename='images/')
    logo = url_for('static', filename='images/logo.png')
    return render_template('news.html', news=news, image=image, logo=logo)



@app.route('/news/<int:id>/')
def news(id):
    with app.app_context():
        session = db_session.create_session()
        news = session.query(News).all()
        image = url_for('static', filename='images/')
        logo = url_for('static', filename='images/logo.png')
    return render_template('post-single.html', news=news[id], image=image, logo=logo)

@app.route('/guides/<int:id>/')
def guide(id):
    with app.app_context():
        session = db_session.create_session()
        guide = session.query(Guides).all()
        image = url_for('static', filename='images/')
        logo = url_for('static', filename='images/logo.png')
    return render_template('guide_single.html', guide=guide[id], image=image, logo=logo)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/profile_pics', picture_fn)

    output_size = (146, 146)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if form.email.data != current_user.email:
            if session.query(User).filter(User.email == form.email.data).first():
                flash('Этот email уже занят', 'danger')
                icons_file = url_for('static', filename='/images/profile_pics/' + current_user.image_file)
                logo = url_for('static', filename='images/logo.png')
            return render_template('profile.html', title='Профиль', icons_file=icons_file,
                                   form=form, logo=logo)
        if form.username.data != current_user.username:
            if session.query(User).filter(User.username == form.username.data).first():
                flash('Это имя уже занято', 'danger')
                icons_file = url_for('static', filename='/images/profile_pics/' + current_user.image_file)
                logo = url_for('static', filename='images/logo.png')
            return render_template('profile.html', title='Профиль', icons_file=icons_file,
                                   form=form, logo=logo)
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.surname = form.surname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        session.add(current_user)
        session.commit()
        flash('Аккаунт успешно изменен', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.surname.data = current_user.surname
        form.username.data = current_user.username
        form.email.data = current_user.email
    icons_file = url_for('static', filename='/images/profile_pics/' + current_user.image_file)
    logo = url_for('static', filename='images/logo.png')
    return render_template('profile.html', title='Профиль',
                           icons_file=icons_file, form=form, logo=logo)


def save_image(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    i = Image.open(form_picture)
    i.save(picture_path)

    return picture_fn

@app.route('/add-news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = AddNewsForm()
    if form.validate_on_submit():
        session = db_session.create_session()

        news = News(
            name=form.name.data,
            author=form.author.data,
            category=form.category.data,
            description=form.description.data,
            small_description=form.small_description.data,
            image=save_image(form.image.data)
        )
        session.add(news)
        session.commit()
        flash('Статья успешна создана', 'success')
        return redirect(url_for('new'))
    elif request.method == 'GET':
        form.author.data = current_user.name
    logo = url_for('static', filename='images/logo.png')
    return render_template('add_news.html', title='Профиль',
                            form=form, logo=logo)


@app.route('/add-guides', methods=['GET', 'POST'])
@login_required
def add_guides():
    form = AddGuidesForm()
    if form.validate_on_submit():
        session = db_session.create_session()

        guides = Guides(
            name=form.name.data,
            author=form.author.data,
            description=form.description.data,
            small_description=form.small_description.data,
            image=save_image(form.image.data)
        )
        session.add(guides)
        session.commit()
        flash('Статья успешна создана', 'success')
        return redirect(url_for('new'))
    elif request.method == 'GET':
        form.author.data = current_user.name
    logo = url_for('static', filename='images/logo.png')
    return render_template('add_guide.html', title='Профиль',
                            form=form, logo=logo)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            flash('Такой пользователь уже есть', 'danger')
            return render_template('register.html', form=form)
        if session.query(User).filter(User.username == form.username.data).first():
            flash('Такой пользователь уже есть', 'danger')
            return render_template('register.html', form=form)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
                    name=form.name.data,
                    surname=form.surname.data,
                    username=form.username.data,
                    email=form.email.data,
                    hashed_password=hashed_password
                    )
        session.add(user)
        session.commit()
        flash(f'Аккаунт был успешно создан', 'success')
        return redirect(url_for('login'))
    logo = url_for('static', filename='images/logo.png')
    return render_template('register.html',  form=form, logo=logo)

@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    forms = LoginForm()
    if forms.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == forms.email.data).first()
        if user and bcrypt.check_password_hash(user.hashed_password, forms.password.data):
            login_user(user, remember=forms.remember_me.data)
            return redirect(url_for('main'))
        flash('Пользователя с таким e-mail не существует или введен неверный пароль', 'danger')
        return render_template('login.html', forms=forms)
    return render_template('login.html', title='Авторизация', forms=forms)





if __name__ == '__main__':
    app.run()
