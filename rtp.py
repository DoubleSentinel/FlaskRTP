from flask import Flask, render_template, request, jsonify

app = Flask( __name__ )

@app.route('/circuits')
def circuits():
    # organizing data as {duration : source-file, name}
    circuits = {
    "Un jour" :
        [
            ("media/documents/excursion-pangalanes-reine-tina-1.pdf",
                "Excursion sur les Pangalanes")
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
    "Quattre jours, trois nuits" :
        [
             ("media/documents/croisiere-vohibola-4j-3n.pdf",
                "Croisière Vohibola"),
             ("media/documents/croisiere-aye-aye.pdf",
                "Croisière Aye Aye"),
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
    return render_template('presentation/boat.html', active='presentation')

@app.route('/presentation/goldbook')
def goldbook():
    pages = [
        ("media/images/goldbook/page1.jpg", "", ""),
        ("media/images/goldbook/page2.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page3.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page4.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page5.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page6.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page7.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page8.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page9.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page10.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page11.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page12.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page13.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page14.jpg", "titre", "descriptif"),
        ("media/images/goldbook/page15.jpg", "titre", "descriptif")
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
    #password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = form['subject']
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Cc"] = form['email']

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(form['message'], "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(config.smtpserver, config.smtpport, conext=context) as server:
        server.login(sender_email, "1234")
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
