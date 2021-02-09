from mysql import *


@app.route('/')
@app.route('/index')
def index():
    datas = getData('make_group')



@app.route('/upload/', methods=['GET'])
def upload_page():
    return render_template('upload.html')
    pass


@app.route('/upload/', methods=['POST'])
def upload():
    uploadData = request.form.to_dict()
    uploadData['username'] = current_user.get_id()
    insert(uploadData, 'make_group')
    return redirect(url_for('upload'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))