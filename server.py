from flask import Flask, request, render_template
import DDLF.DDLF_Server as srv
import static.create_ava as CAVA
app = Flask(__name__)
server = srv.Server('SERVER_V0.1', 'database.json')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        login = request.form['login']
        email = request.form['email']
        password = request.form['password']
        password_repeat = request.form['password_repeat']
        if password_repeat == password and server.is_correct_password(password) and server.is_correct_login(login):
            server.DataBase.count_update()
            if server.DataBase.add_user(login, email, password, CAVA.create_image(server.DataBase.count_of_users, 16, 16)):
                return render_template('login_form.html')
        server.send_message('User data isn\'t correct')
    return render_template('registration_form.html')

@app.route('/<id>', methods=['GET'])
def index(id):
    user = server.DataBase.get_user(id)
    if not user:
        return 'User not found', 404
    return render_template('acc.html', login=id, user=user, image_filename=user['image_index'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = server.DataBase.get_user(login)
        if user and user['password'] == password:
            return render_template('acc.html', login=login, user=user, image_filename=user['image_index'] )
    return render_template('login_form.html')

if __name__ == '__main__':
    server.send_message('server is started successfully!')
    app.run(host='0.0.0.0', port=5000, debug=True)