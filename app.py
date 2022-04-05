from flask import Flask, render_template
from data import users
from data import connection
from data import get_same_interests
from data import get_user_id

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('main.html')


@app.route('/signin')
def signin():

    return render_template('signin.html')


@app.route('/signup')
def signup():

    return render_template('signup.html')

# For the signed in user, view profile and adjust settings


@app.route('/user_profile/<int:user_id>')
def user_profile(user_id):

    profile = users[user_id]

    return render_template('user_profile.html', profile=profile)

# View other peoples' profiles


@app.route('/profile/<int:user_id>')
def profile(user_id):

    profile = users[user_id]

    return render_template('profile.html', profile=profile)

# When 4 other people are found, bring user to this page to get confirmation if they want to meet each other


@app.route('/connect/<int:connection_id>')
def connect(connection_id):

    profile = connection[connection_id]

    common_interests = get_same_interests(connection_id)

    # List of User IDs to link to the appropriate profile

    profile_ids = []

    profile_ids.append(get_user_id(profile[0]))
    profile_ids.append(get_user_id(profile[1]))
    profile_ids.append(get_user_id(profile[2]))
    profile_ids.append(get_user_id(profile[3]))
    profile_ids.append(get_user_id(profile[4]))

    return render_template('connect.html', profile=profile, common_interests=common_interests, profile_ids=profile_ids)

# If all users confirm to meet each other, bring users to this page and set a date and location to meet

@app.route('/meet/<int:connection_id>')
def meet(connection_id):

    profile = connection[connection_id]

    common_interests = get_same_interests(connection_id)

    profile_ids = []

    profile_ids.append(get_user_id(profile[0]))
    profile_ids.append(get_user_id(profile[1]))
    profile_ids.append(get_user_id(profile[2]))
    profile_ids.append(get_user_id(profile[3]))
    profile_ids.append(get_user_id(profile[4]))

    return render_template('meet.html', profile=profile, common_interests=common_interests, profile_ids=profile_ids)
