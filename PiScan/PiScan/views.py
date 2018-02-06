"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask.helpers import url_for
from flask import render_template
from PiScan import app
import socket




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/doscan')
def doscan():
    """ Scans for open ssh servers """
    TCP_PORT = 22
    BUFFER_SIZE = 20
    ssh_ips = []
    for last_octet in range(0,254,1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(.1)
        
        try:
            s.connect((str('10.1.10.' + str(last_octet)), TCP_PORT))
            
            data = s.recv(BUFFER_SIZE)
            ssh_ips.append(last_octet)
        except ConnectionRefusedError as IP:
            ssh_ips.append(last_octet)
        except Exception as E:
            print(E)
        
     

    return(str (ssh_ips))
with app.test_request_context():   
    scanurl = url_for('doscan')