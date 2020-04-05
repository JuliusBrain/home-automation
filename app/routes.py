from app import app, db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import ItemForm
from app.models import User
from app.models import Item
from flask import render_template, request, redirect, flash, url_for
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/index")
@login_required
def index():
    items = Item.query.all()
    return render_template("index.html", items=items)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/add", methods=["POST"])
def add_item():
    form = ItemForm()
    if request.method == "POST":
        item = Item(
            name=form.name.data, description=form.description.data, user=current_user
        )
        db.session.add(item)
        db.session.commit()
        flash("Your Home item is now added!")
        return redirect(url_for("index"))


@app.route("/update/<int:id>")
def update_route(id):
    if not id or id != 0:
        item = Item.query.get(id)
        if item:
            return render_template("update.html", item=item)


@app.route("/update/<int:id>", methods=["POST"])
def update_item(id):
    if not id or id != 0:
        item = Item.query.get(id)
        form = ItemForm()
        if item:
            item.name = form.name.data
            item.description = form.description.data
            db.session.commit()
        return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete_item(id):
    if not id or id != 0:
        item = Item.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
        return redirect(url_for("index"))


@app.route("/turn/<int:id>")
def turn(id):
    if not id or id != 0:
        item = Item.query.get(id)
        if item:
            item.status = not item.status
            db.session.commit()
        return redirect(url_for("index"))

