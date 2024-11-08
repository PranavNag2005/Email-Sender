from flask import Flask,render_template,redirect,url_for,flash
from flask_mail import Mail,Message
app=Flask(__name__)
app.config['MAIL_SERVER']="smtp.gmail.com"
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='janardhanravipati175@gmail.com'
app.config['MAIL_PASSWORD']='qzzb gsgi xhqs simz'
app.config['MAIL_DEFAULT_SENDER']='praveenkumarkalikiri@gmail.com'
mail=Mail(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email')
def send_email():
    try:
        msg=Message("Text email",recipients=['riyazvadapalli786@gmail.com']) #This is where the  name of the recipients should be
        msg.body='This is the body of the email'
        msg.html="<b>This is the body of the email in Html format </b>"#This is the text to send
       


        mail.send(msg)
        flash('Email sent successfully!','success')

    except Exception as e:
        flash(f"An error occured {e}",'danger')
    return redirect(url_for('index'))

if __name__=='__main__':
    app.secret_key="abcdef"
    app.run(debug=True)
        
