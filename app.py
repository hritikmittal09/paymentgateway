from flask import Flask,render_template,request
import smtplib
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/payment_details",methods= ["GET","POST"])
def payment_details():
       
    return render_template("payment_details.html")
@app.route("/finish",methods=["POST"])
def finish():
    if request.method =="POST":
        email = request.form.get("email")
        money = request.form.get("money")
        payment = request.form.get("payment_method")
        #server=smtplib.SMTP("smtp.gmail.com",587)
        #server.starttls()
        #server.login("botpythonhritk@gmail.com","Python@09")
        #server.sendmail("botpythonhritk@gmail.com", email, "thanks")
        #server.quit()

        
        print("mail sent")
        

    return render_template("thankyou.html",email= email,payment = payment, money = money)    


        


if __name__  == "__main__":
    app.run(debug=True)   