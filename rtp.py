from flask import Flask, render_template, request, jsonify

app = Flask( __name__ )

@app.route('/circuits')
def circuits():
    # organizing data as {duration : source-file, name}
    circuits = {
    "Un jour" :
        [
            ("media/documents/excursion-palmeraie.pdf",
                "Excursion à la Palmeraie")
        ],
    "Deux jours, une nuit" :
        [
             ("media/documents/croisiere-east-coast-tapakala.pdf",
                "Croisière East Coast Tapakala"),
             ("media/documents/croisiere-varecia.pdf",
                "Croisière Varecia"),
             ("media/documents/croisiere-macaco.pdf",
                "Croisière Macaco")
        ],
    "Trois jours, deux nuits" :
        [
             ("media/documents/croisiere-indri-indri.pdf",
                "Croisière Indri Indri"),
             ("media/documents/croisiere-vohibola.pdf",
                "Croisière Vohibola")
        ],
    "Quatre jours, trois nuits" :
        [
             ("media/documents/croisiere-vohibola-4j-3n.pdf",
                "Croisière Vohibola"),
             ("media/documents/croisiere-aye-aye.pdf",
                "Croisière Aye Aye"),
        ],
     "Six jours, cinq nuits" :
        [
            ("media/documents/croisiere-vatomandry.pdf",
               "Croisière Vatomandry")
        ]
    }
    return render_template('circuits.html',
                            active='circuits',
                            circuits=circuits)

@app.route('/presentation')
def presentation():
    return render_template('presentation.html', active='presentation')

@app.route('/presentation/pangalanes')
def pangalanes():
    images = ["media/images/pangalanes/pangalanes_1.jpg",
              "media/images/pangalanes/pangalanes_2.jpg",
              "media/images/pangalanes/pangalanes_3.jpg",]
    return render_template('presentation/pangalanes.html',
            active='presentation', images=images)

@app.route('/presentation/boat')
def boat():
    features = [
        ("media/images/boat/boat_1.JPG","Salon détente à l'avant du bateau"),
        ("media/images/boat/boat_2.JPG","Table d'hôte pour 10 convives"),
        ("media/images/boat/boat_3.JPG","Bar sur le pont à l'arrière du bateau"),
        ("media/images/boat/boat_4.JPG","Cuisine avec réchaud à gaz, réfrigérateur, et congélateur"),
        ("media/images/boat/boat_5.JPG","Cabine tout confort avec lit double et rangements"),
        ("media/images/boat/boat_6.JPG","Salle de bain privative (WC, douche, et lavabo)"),
        ("media/images/boat/boat_7.JPG","L'energie électrique est 100% verte grâce au panneau solaires"),
        ("media/images/boat/boat_8.JPG","Quatre membres d'équipage (Chef cuisinière, capitaine, stewards)"),
        ]
    return render_template('presentation/boat.html',
            active='presentation', features=features)

@app.route('/presentation/goldbook')
def goldbook():
    pages = [
        ("media/images/goldbook/page_1.JPG", "Septembre 2016"),
        ("media/images/goldbook/page_2.JPG", "Septembre 2016"),
        ("media/images/goldbook/page_3.JPG", "Septembre 2016"),
        ("media/images/goldbook/page_4.JPG", "Octobre 2016"),
        ("media/images/goldbook/page_5.JPG", "Octobre 2016"),
        ("media/images/goldbook/page_6.JPG", "Octobre 2016"),
        ("media/images/goldbook/page_7.JPG", "Octobre 2016"),
        ("media/images/goldbook/page_8.JPG", "Octobre 2016"),
        ("media/images/goldbook/page_9.JPG", "Octobre 2016")
        ]
    return render_template('presentation/goldbook.html',
            active='presentation', goldbook=pages)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', active='gallery')

@app.route('/gallery/videos')
def videos():
    return render_template('gallery/videos.html', active='gallery')

@app.route('/gallery/images')
def images():
    return render_template('gallery/images.html', active='gallery')

@app.route('/gallery/press')
def press():
    return render_template('gallery/press.html', active='gallery')

@app.route('/events')
def events():
    return render_template('events.html', active='events')

@app.route('/')
def index():
    return render_template('home.html', active='none')

@app.route('/contact')
def contact():
    return render_template('contact.html', active='contact')

@app.route('/contact/conditions')
def agency():
    return render_template('contact/conditions.html', active='contact')

@app.route('/contact/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        status = ''
        #try:
        send_email(request.form)
        #except:
        #    status = ''
        return render_template('contact/booking.html',
                active='contact', status=status)
    else:
        return render_template('contact/booking.html', active='contact')

@app.route('/contact/access')
def access():
    return render_template('contact/access.html', active='contact')

def send_email(form=None):
    import smtplib, ssl, config
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = config.smtpuser
    receiver_email = config.targetmail #mia's email

    message = MIMEMultipart("alternative")
    message["Subject"] = form['subject']
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Cc"] = form['email']

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(MIMEText(form['message'], "plain"))

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    server = smtplib.SMTP(config.smtpserver, config.smtpport)
    server.starttls(context=context)
    server.login(sender_email, config.smtppassword)
    #print(message.as_string())
    server.sendmail(sender_email, receiver_email, message.as_string())
