""""
Title : Cook's Room
Description : A mini website that features different recipe and influencers/ food enthusiast.
                The purpose of this website is to appreciate more our filipino recipe and those influencers
                also embracing and wnats to level up our culture on their contents. We want to give our users who
                loves to cook different learnings by providing them some channels that they can watch and recipes
                that they can try aon their owm./
Programmers:
            John Rupert S. Caingal
            Ernesto E. Esguerra
            Christian H. Salamat
            Jimwell F. Seminiano

Date submitted : October 23, 2022

"""

from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cr-mainpage.html')


@app.route('/Influencers-page/')
def page2():
    return render_template('cr-page2.html')

@app.route('/recipe-page/')
def page3():
    return render_template('cr-recipe.html')




if __name__ == '__main__':
    app.run()