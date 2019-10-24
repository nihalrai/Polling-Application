import os
import traceback

from flask import Flask, render_template, request, url_for, redirect

from dbsetup import Database


# Define app
app = Flask(__name__)

data = {
   'question' : 'Who is your favourite author?',
   'fields'   : ['Miguel de Cervantes', 'Charles Dickens', 'J.R.R. Tolkien', 'Antoine de Saint-Exuper']
}


@app.route('/')
def root():
    return render_template('poll.html', data=data)

@app.route('/poll')
def poll():
    try:
        vote = request.args.get('field')

        obj  = Database()
        obj.update(vote)
        return redirect(url_for('root'))
    except:
        traceback.print_exc()
        return render_template('error.html')

@app.route('/results')
def show_results():
    obj  = Database()
    data = obj.get_data()

    find = []
    for document in data:
        find.append(document)
    
    return str(find)


if __name__ == "__main__":
    # Fill the default data
    obj = Database()
    obj.document()

    app.run(debug=True)
