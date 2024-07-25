from flask import Flask, render_template
from utils import Candidate

candid = Candidate('candidate.json')
dict_ = candid.load_candidates_in_dict()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('list.html', candidates=dict_)


@app.route('/candidate/<x>')
def candidate(x):
    """
    YOU ENTER THE PARAMETER AND GET PERSON WITH THIS ID
    """
    dictionary = candid.get_data_from_id(x)
    picture = dictionary['picture']
    name = dictionary['name']
    position = dictionary['position']
    skills = dictionary['skills']
    return render_template('single.html', name=name, position=position, picture=picture, skills=skills)


@app.route('/search/<candidate_name>')
def name_search(candidate_name):
    """
    YOU ENTER THE PARAMETER AND GET PERSON WITH THIS NAME
    """
    dictionary = candid.get_candidates_by_name(candidate_name)
    length = len(dictionary)
    return render_template('search.html', dictionary=dictionary, length=length, name=candidate_name)


@app.route('/skill/<skill_name>')
def skill_info(skill_name):
    """
    YOU ENTER THE PARAMETER AND GET PERSON WITH THESE SKILLS
    """
    dictionary = candid.get_candidates_by_skill(skill_name)
    length = len(dictionary)
    return render_template('skill.html', length=length, dictionary=dictionary)


app.run()
