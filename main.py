from flask import Flask, render_template, request, jsonify

app = Flask( __name__ )

@app.route('/circuits')
def circuits():
    return render_template('circuits.html', active='circuits')

@app.route('/contact')
def contact():
    return render_template('contact.html', active='contact')

@app.route('/contact/agency')
def agency():
    return render_template('contact/agency.html', active='contact')

@app.route('/contact/booking')
def booking():
    return render_template('contact/booking.html', active='contact')

@app.route('/contact/access')
def access():
    return render_template('contact/access.html', active='contact')

@app.route('/presentation')
def presentation():
    return render_template('presentation.html', active='presentation')

@app.route('/presentation/pangalanes')
def pangalanes():
    images = ["media/images/pangalanes/pangalanes_1.jpg",
              "media/images/pangalanes/pangalanes_2.jpg",
              "media/images/pangalanes/pangalanes_3.jpg",
              "media/images/pangalanes/pangalanes_4.jpg",
              "media/images/pangalanes/pangalanes_5.jpg"]
    return render_template('presentation/pangalanes.html',
            active='presentation', images=images)

@app.route('/presentation/boat')
def boat():
    return render_template('presentation/boat.html', active='presentation')

@app.route('/presentation/goldbook')
def goldbook():
    pages = [
        ("media/images/goldbook/page1.jpg", "titre", "descriptif"),
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

@app.route('/media')
def media():
    return render_template('media.html', active='media')

@app.route('/media/videos')
def videos():
    return render_template('media/videos.html', active='media')

@app.route('/media/images')
def images():
    return render_template('media/images.html', active='media')

@app.route('/media/press')
def press():
    return render_template('media/press.html', active='media')

@app.route('/events')
def events():
    return render_template('events.html', active='events')

@app.route('/')
def index():
    return render_template('home.html', active='none')
