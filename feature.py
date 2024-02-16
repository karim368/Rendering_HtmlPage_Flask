from flask import Flask,render_template

FAI = Flask(__name__)

@FAI.route('/karim')
def karim():
    return render_template('karim.html',name='Phatan Karim and Khallu')

if __name__ == '__main__':
    FAI.run(debug=True)