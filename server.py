from flask import Flask, render_template, request, url_for, redirect # render_template will send the html file

import csv

app = Flask(__name__) # we use Flask class to instantiate ann app
#print(__name__) # to know what it is (it is __main__ )



@app.route('/') 
def my_home():
    return render_template('./index.html') 


@app.route('/<string:page_name>')  # this open the url page and the html file with the same name. 
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./database.txt', mode='a') as database:
        email =data['email']
        subject=data['subject']
        message=data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('./database.csv',newline='', mode='a') as database2:
        email =data['email']
        subject=data['subject']
        message=data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)        
        csv_writer.writerow([email,subject,message])                  

@app.route('/submit_form', methods=['POST', 'GET']) #POST (me sending data to the server) means the browser wants us to save infos and GET to send   
def submit_form():
    if request.method == 'POST': #if we say the method is going to be 'post' in contact.html
        try:
            data = request.form.to_dict() # we re going to grab that data ['message']['email'][subject] /
            # with to_dict method
            # email = request.form['email']   # you turn the form data into a dictionary
            write_to_file(data)
            write_to_csv(data)
            #return redirect('./thankyou.html') # to redirect to another htlm page
            return render_template('./thankyou.html', email=data['email'], data=data['subject'])
        except:
            return 'did not save to database'
    else:
        return 'somthing went wrong'

'''
    return 'form submitted horray'
    
    
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    
    
    return render_template('login.html', error=error)
    '''


'''
@app.route('/index.html') 
def my_home2():
    return render_template('./index.html') 

@app.route('/works.html')  
def works():
    return render_template('./works.html')

@app.route('/about.html')  
def about_me():
    return render_template('./about.html')

@app.route('/contact.html')  
def contact():
    return render_template('./contact.html')

@app.route('/components.html')  
def components():
    return render_template('./components.html')

'''


'''

@app.route('/<username>')  
def hello_world3(username = None):
    return render_template('index_flask.html', name = username)


<body>
    {{ name }}
    {{ post_identity }}
    blabla
    <script src='static\script.js'></script>
</body>



@app.route('/<username>/<int:post_id>')  
def hello_world2(username = None, post_id = None):
    return render_template('./index_flask.html', name = username, post_identity = post_id) 


'''

    
