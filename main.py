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
    return render_template('agency.html', active='contact')

@app.route('/contact/booking')
def booking():
    return render_template('booking.html', active='contact')

@app.route('/contact/access')
def access():
    return render_template('access.html', active='contact')

@app.route('/presentation')
def presentation():
    return render_template('presentation.html', active='presentation')

@app.route('/presentation/pangalanes')
def pangalanes():
    return render_template('pangalanes.html', active='presentation')

@app.route('/presentation/boat')
def boat():
    return render_template('boat.html', active='presentation')

@app.route('/presentation/goldbook')
def goldbook():
    return render_template('goldbook.html', active='presentation')

@app.route('/media')
def media():
    return render_template('media.html', active='media')

@app.route('/media/videos')
def videos():
    return render_template('videos.html', active='media')

@app.route('/media/images')
def images():
    return render_template('images.html', active='media')

@app.route('/media/press')
def press():
    return render_template('press.html', active='media')

@app.route('/events')
def events():
    return render_template('events.html', active='events')

@app.route('/')
def index():
    return render_template('home.html', active='none')
