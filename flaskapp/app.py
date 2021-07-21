from flask import Flask, render_template, redirect, url_for, session, flash, request, logging
from flask_mysqldb import MySQL
from wtforms import Form , StringField, TextField, TextAreaField, PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

#Config MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] ='myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#initialize MYSQL
mysql = MySQL(app)


def is_logged_in(f):
   @wraps(f)
   def wrap(*args, **kwargs):
       if 'logged_in' in session:
           return f(*args, **kwargs)
       else:
           flash('UnAuthorised, Please Login','danger')
           return redirect(url_for('login'))
   return wrap

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')    
@app.route('/articles')
def articles():    
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM articles')
    articles = cur.fetchall()
    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = "No Article Found"
        return render_template('articles.html', msg=msg)    
    cur.close()
    return render_template('dashboard.html')   
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM articles WHERE id=%s',[id])
    article = cur.fetchone()
    return render_template('article.html', article=article)

@app.route('/edit_article/<string:id>/',methods=['GET','POST'])
@is_logged_in
def edit_article(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM articles WHERE id=%s',[id])
    article = cur.fetchone()
    form = ArticleForm(request.form)
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        cur = mysql.connection.cursor()
        cur.execute("""UPDATE articles SET title=%s, body=%s WHERE id=%s""",(title, body, id))

        mysql.connection.commit()
        cur.close()
        flash('Article Updated Successfully','success')
        return redirect(url_for('dashboard'))
    return render_template('edit_article.html', form=form)

@app.route('/delete_article/<string:id>/',methods=['GET','POST'])
@is_logged_in
def delete_article(id):
    cur = mysql.connection.cursor()
    result = cur.execute('DELETE FROM articles WHERE id=%s',[id])
    mysql.connection.commit()
    cur.close()
    flash('Article Deleted Successfully', 'success')

    return redirect(url_for('dashboard'))

 
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1,max=50), validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=4,max=30),validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6,max=50),validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), 
    validators.EqualTo('confirm', message="Password do not match")])
    confirm  = PasswordField('Confirm Password',[validators.DataRequired()])

class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=300)])
    body = TextAreaField('Body', [validators.Length(min=1, max=100000)])

@app.route('/add_article',methods=['GET','POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO articles(title, body, author)
        VALUES(%s, %s, %s)""",(title, body, session['username']))

        mysql.connection.commit()
        cur.close()
        flash('Article Created Successfully','success')
        return redirect(url_for('dashboard'))
    return render_template('add_article.html', form=form)

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO users(name, email,username, password)
        VALUES(%s, %s, %s, %s)""",(name, email, username, password))
        
        mysql.connection.commit()
        cur.close()
        flash('You are registered succesfully','success')
        return redirect(url_for('index'))
        
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users WHERE username = %s",[username])
        if result > 0:
            data = cur.fetchone()
            password = data['password']
            if sha256_crypt.verify(password_candidate,password):
                app.logger.info('PASSWORD MATCHED')
                session['logged_in'] = True
                session['username'] = username

                flash('You are now Succesfully Logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error="Invalid Login Password"
                return render_template('login.html',error=error)
            cur.close()
        else:
            error="Username Not Found"
            return render_template('login.html',error=error)    
    
    return render_template('login.html')

 

@app.route('/dashboard')
@is_logged_in
def dashboard():
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM articles')
    articles = cur.fetchall()
    if result > 0:
        return render_template('dashboard.html', articles=articles)
    else:
        msg = "No Article Found"
        return render_template('dashboard.html', msg=msg)    
    cur.close()
    return render_template('dashboard.html')   

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now Succesfully Logged Out', 'success')
    return redirect(url_for('login'))
     

if __name__=="__main__":
    app.secret_key = "secret123"
    app.run(debug=True)