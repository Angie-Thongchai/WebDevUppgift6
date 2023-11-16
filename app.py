from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from sqlalchemy.exc import IntegrityError

app = Flask(__name__, template_folder = 'templetes')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datacreate.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate=Migrate(app,db)

class MENU(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pizza = db.Column(db.String(20), unique=False, nullable=False)
    size = db.Column(db.String(20), unique=False, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"pizza={self.pizza},size={self.size},amount={self.amount},price={self.price}"

class PAYMENT(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cardname = db.Column(db.String(20),unique=False, nullable=False)
    cardnumber = db.Column(db.Integer, nullable= False)
    exp = db.Column(db.Integer, nullable= False)
    cvv = db.Column(db.Integer, nullable= False)
    member = db.Column(db.Integer, nullable= False)

    def __repr__(self):
        return f"cardname={self.cardname},cardnumber={self.cardnumber},exp={self.exp},cvv={self.cvv},member={self.member}"

class BOOK(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guest = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    adults = db.Column(db.Integer, nullable=False)
    children = db.Column(db.Integer, nullable=False)
    checkin = db.Column(db.Integer, nullable= False)
    bookingtime = db.Column(db.Integer, nullable= False)

    def __repr__(self):
        return f"guest={self.guest},email={self.email},phone={self.phone},adults={self.adults},children={self.children},bookingtime={self.bookingtime}"

class REGISTER(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    firstname = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable= False)

    def __repr__(self):
        return f"email={self.email},password={self.password},firstname={self.firstname},lastname={self.lastname},gender={self.gender}"


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/menu/", methods=['POST'])
def menu():
    return render_template("menu.html",
                           n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/addlist1/", methods=['POST'])
def addlist1(): 
        pizza = request.form.get("pizza1")
        size = request.form.get("size1" )
        amount = request.form.get("amount1")
        price = request.form.get("price1" )

        print(pizza, size, amount, price)
        
        if pizza != '' and size != '' and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
                   
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        
@app.route("/addlist2/", methods=['POST'])
def addlist2(): 
        
        pizza = request.form.get("pizza2")
        size = request.form.get("size2" )
        amount = request.form.get("amount2")
        price = request.form.get("price2" )
        
        print(pizza, size, amount, price)

        
        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/addlist3/", methods=['POST'])
def addlist3(): 
        
        pizza = request.form.get("pizza3")
        size = request.form.get("size3" )
        amount = request.form.get("amount3")
        price = request.form.get("price3" )

        print(pizza, size, amount, price)
        
        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/addlist4/", methods=['POST'])
def addlist4(): 
        
        pizza = request.form.get("pizza4")
        size = request.form.get("size4" )
        amount = request.form.get("amount4")
        price = request.form.get("price4" )

        print(pizza, size, amount, price)
        
        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/addlist5/", methods=['POST'])
def addlist5(): 
        
        pizza = request.form.get("pizza5")
        size = request.form.get("size5" )
        amount = request.form.get("amount5")
        price = request.form.get("price5" )

        print(pizza, size, amount, price)
        
        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        
@app.route("/addlist6/", methods=['POST'])
def addlist6(): 
        
        pizza = request.form.get("pizza6")
        size = request.form.get("size6" )
        amount = request.form.get("amount6")
        price = request.form.get("price6" )

        print(pizza, size, amount, price)
        
        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/addlist7/", methods=['POST'])
def addlist7(): 
        
        pizza = request.form.get("pizza7")
        size = request.form.get("size7" )
        amount = request.form.get("amount7")
        price = request.form.get("price7" )

        print(pizza, size, amount, price)
       
        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        
@app.route("/addlist8/", methods=['POST'])
def addlist8(): 
        
        pizza = request.form.get("pizza8")
        size = request.form.get("size8" )
        amount = request.form.get("amount8")
        price = request.form.get("price8" )

        print(pizza, size, amount, price)

        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/addlist9/", methods=['POST'])
def addlist9(): 
        
        pizza = request.form.get("pizza9")
        size = request.form.get("size9" )
        amount = request.form.get("amount9")
        price = request.form.get("price9" )

        print(pizza, size, amount, price)

        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/addlist10/", methods=['POST'])
def addlist10(): 
        
        pizza = request.form.get("pizza10")
        size = request.form.get("size10" )
        amount = request.form.get("amount10")
        price = request.form.get("price10" )

        print(pizza, size, amount, price)
   
        if pizza != '' and size != ''and amount is not None and price is not None :
            m=MENU (pizza=pizza, size=size, amount=amount, price=price)
            db.session.add(m)
            db.session.commit()
            return render_template('menu.html',
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])
        else:
            flash('Invalid ordering. Please! fill your order again.')
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])

@app.route("/memLog/", methods=['POST'])
def memLog():
    return render_template("memLog.html")

@app.route("/address/", methods=['POST'])
def address():
    return render_template("address.html")

@app.route("/team/", methods=['POST'])
def team():
    return render_template("team.html")

@app.route("/book/", methods=['POST'])
def book():
    return render_template("book.html",data=[{'time':'select time'}, {'time':'13.00'},{'time':'14.00'},{'time':'15.00'}, {'time':'16.00'},{'time':'17.00'},{'time':'18.00'}, {'time':'19.00'},{'time':'20.00'}],
                           data1=[{'noc': 0}, {'noc': 1}, {'noc': 2}, {'noc': 3}, {'noc': 4}, {'noc': 5}])

@app.route("/index/", methods=['GET'])
def backhome():
    return render_template("index.html")

@app.route("/memreg/", methods=['POST'])
def register():
    return render_template("memreg.html",data2=[{'gender': 'gender'}, {'gender': 'Male'}, {'gender': 'Female'}])

@app.route("/addregister/", methods=['POST'])
def addregister():
        email = request.form.get("reemail")
        password = request.form.get("retypepassword")
        firstname = request.form.get("refirstname")
        lastname = request.form.get("relastname")
        gender = request.form.get("gender")

        if  email != ''and password != ''  and firstname !='' and lastname != '' and gender != '' :
            regis=REGISTER ( email=email, password=password,  firstname=firstname, lastname=lastname, gender=gender)
            db.session.add(regis)
            db.session.commit()
            return redirect('/')
        else:
            return render_template("memreg.html")

@app.route("/indexteam/", methods=['POST'])
def indexteam():
    return render_template("indexteam.html")

@app.route("/order/", methods=['POST','GET'])
def order():
    if request.method== "POST":
        menus = MENU.query.all()
        return render_template("order.html", menus=menus)
    else:
         return render_template("indexteam.html")

@app.route('/delete/<int:id>')
def erase(id):
    menu = MENU.query.get(id)
    db.session.delete(menu)
    db.session.commit()
    return render_template('order.html')

@app.route("/addbooks/", methods=['POST'])
def addbook():
        guest = request.form.get("guest")
        email = request.form.get("email")
        phone = request.form.get("phone")
        adults = request.form.get("adults")
        children = request.form.get("children")
        checkin = request.form.get("checkin")
        bookingtime = request.form.get("bookingtime")

        if guest != '' and email != ''and phone is not None and adults is not None and children !='' and checkin is not None and bookingtime is not None :
            b=BOOK (guest=guest, email=email, phone=phone, adults=adults, children=children, checkin=checkin, bookingtime=bookingtime)
            db.session.add(b)
            db.session.commit()
            return redirect('/')
        else:
            return render_template("book.html")

@app.route("/booking/", methods=['POST'])
def booking():
    bookings = BOOK.query.all()
    return render_template("booking.html", bookings=bookings)

@app.route('/delete2/<int:id>')
def erasebook(id):
    booking = BOOK.query.get(id)
    db.session.delete(booking)
    db.session.commit()
    return render_template('booking.html',)

@app.route("/payment/", methods=['POST'])
def payment():
    return render_template("payment.html")

@app.route("/addpayment/", methods=['POST'])
def addpayment():
        cardname = request.form.get("cardname")
        cardnumber = request.form.get("cardnumber")
        exp = request.form.get("exp")
        cvv = request.form.get("cvv")
        member = request.form.get("memcode")
        
        if cardname !='' and cardnumber is not None and exp is not None and cvv is not None and member is not None:
            pay=PAYMENT (cardname=cardname, cardnumber=cardnumber, exp=exp, cvv=cvv, member=member)
            db.session.add(pay)
            db.session.commit()
            flash('Thank you and enjoy the PIZZA')
            return redirect('/')
        else:
            return render_template("menu.html",
                            n1=[{'name': 'Margherita'}],s1=[{'size': 'Medium'}],
                           n2=[{'name': 'Pepperoni'}],s2=[{'size': 'Medium'}],
                           n3=[{'name': 'Hawaii'}],s3=[{'size': 'Medium'}],
                           n4=[{'name': 'Vegetarian'}],s4=[{'size': 'Medium'}],
                           n5=[{'name': 'Seafood'}],s5=[{'size': 'Medium'}],
                           n6=[{'name': 'Carbonara'}],s6=[{'size': 'Medium'}],
                           n7=[{'name': 'Quattro Stagioni'}],s7=[{'size': 'Medium'}],
                           n8=[{'name': 'Quattro Formaggi'}],s8=[{'size': 'Large'}],
                           n9=[{'name': 'Napoli'}],s9=[{'size': 'Large'}],
                           n10=[{'name': ' Calzone'}],s10=[{'size': 'Large'}])


if __name__=="__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, host='0.0.0.0')