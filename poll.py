import io
import os
import json
import plotly

import plotly.graph_objs as go
import chart_studio.plotly as py

from flask import Flask, render_template, request, url_for, redirect

from dbsetup import Database


# Define app
app = Flask(__name__)

data = {
   'question' : 'Who is your favourite author?',
   'fields'   : ['Miguel de Cervantes', 'Charles Dickens', 'J.R.R. Tolkien', 'Antoine de Saint-Exuper']
}

def dbconnect():
    try:
        obj  = Database()
        obj.connection()
        return obj
    except:
        return render_template('error.html')

@app.route('/')
def root():
    return render_template('poll.html', data=data)

@app.route('/poll')
def poll():
    try:
        vote = request.args.get('field')
        dbconnect().update(vote)
        
        return redirect(url_for('root'))
    except:
        return render_template('error.html')

@app.route('/results')
def show_results():
    found = dbconnect().get_data()

    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
    labels, values = [], []

    for document in found:
        if "name" in document:
            labels.append(document["name"])
            values.append(document["vote"])
    chart = [go.Bar(
            x=labels,
            y=values,
            text=values,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]
    filename = os.path.join(".%s" % (os.sep), "templates", "output.html")
    plotly.offline.plot(chart, output_type="file", filename=filename , auto_open=False)
    
    return render_template("output.html")
    

if __name__ == "__main__":
    try:
        # Fill the default data
        obj = dbconnect()
        obj.document()

        app.run(debug=True)
    except:
        print ("Error Occured")