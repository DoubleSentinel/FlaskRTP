from flask import Flask, render_template, request, jsonify
from flask_recaptcha import ReCaptcha
import requests, os, json, re
import config

app = Flask( __name__ )

app.config.update({
    "RECAPTCHA_SITE_KEY": config.captchaKey,
    "RECAPTCHA_SITE_SECRET": config.captchaSecret,
    "RECAPTCHA_ENABLED": True
})

recaptcha = ReCaptcha(app=app)

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
        ("media/images/boat/boat_7.JPG","L'énergie électrique est 100% verte grâce aux panneaux solaires"),
        ("media/images/boat/boat_8.JPG","5 membres d'équipage (Capitaine, 2 matelos, cheffe cuisinière, guide)"),
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

@app.route('/media')
def media():
    images = []
    videos = []
    pattern = re.compile(".(gif|jpg|jpeg|JPG|png|PNG|mov|mp4|MP4)$")

    for subdir, dirs, files in os.walk("./static/media/images/gallery"):
        for file in files:
            if pattern.search(file):
                # print(os.path.join(subdir, file)[1:])
                images.append(os.path.join(subdir, file)[1:])

    for subdir, dirs, files in os.walk("./static/media/videos"):
        for file in files:
            if pattern.search(file):
                # print(os.path.join(subdir, file)[1:])
                videos.append(os.path.join(subdir, file)[1:])

    return render_template('media.html',
                            active='media',
                            images=images,
                            videos=videos)

@app.route('/press')
def press():
    # organizing data as {filetype : source-file, name}
    articles = {
    "Images" :
        [
             ("media/documents/press_1.jpg",
                "Fluvial n°267 (Novembre 2016)"),
             ("media/documents/press_2.jpg",
                "Info Tourisme Madagascar (Juin 2017)"),
             ("media/documents/press_3.jpg",
                "Info Tourisme Madagascar (Février 2019)")
        ],
    "PDF" :
        [
             ("media/documents/press_pdf_1.pdf",
                "Fluvial n°268 (Janvier 2017)")
        ]
    }
    return render_template('press.html',
                            active='press',
                            articles=articles)

@app.route('/')
def index():
    return render_template('home.html', active='home')

@app.route('/contact')
def contact():
    return render_template('contact/booking.html', active='contact')

@app.route('/contact/conditions')
def agency():
    return render_template('contact/conditions.html', active='contact')

@app.route('/contact/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        status = ''
        try:
            r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                          data = {'secret' :
                                  config.captchaSecret,
                                  'response' :
                                  request.form['g-recaptcha-response']})

            google_response = json.loads(r.text)

            if google_response['success']:
                status = "Email envoyé avec succès!"
                send_email(request.form)
            else:
                raise Exception("captcha","Veuillez cliquer sur le captcha au dessus du boutton 'Envoyer'")
        except Exception as e:
            if e.args[0] == 'captcha':
                status = e.args[1]
            else:
                status = "Une erreur s'est produite lors de l'envoi de l'e-mail. Veuillez contacter Chrismiatours directement si vous voyez ce message."
        return render_template('contact/booking.html',
                active='contact', status=status)
    else:
        return render_template('contact/booking.html', active='contact', captchaKey=config.captchaSecret)

@app.route('/contact/access')
def access():
    return render_template('contact/access.html', active='contact')

def send_email(form=None):
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    message = MIMEMultipart()
    message["Subject"] = form['subject']
    message["From"] = config.smtpuser
    message["To"] = config.targetmail
    message["Cc"] = ",".join([form['email']] + config.ccmails)

    contents_list = ["Email généré automatiquement pour ",
                    form['full_name'],
                    " (",
                    form['telephone'],
                    "). ",
                    "Ne répondez pas s'il vous plaît.\n\n",
                    form['message']]
    message.attach(MIMEText(''.join(contents_list), "plain"))

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    server = smtplib.SMTP(config.smtpserver, config.smtpport)
    server.starttls(context=context)
    server.login(config.smtpuser, config.smtppassword)
    print([config.targetmail, form['email']] + config.ccmails)
    server.sendmail(config.smtpuser,
                 [config.targetmail, form['email']]
                 + config.ccmails,
                 message.as_string())
    server.quit()
