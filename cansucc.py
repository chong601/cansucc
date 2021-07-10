from flask import Flask, render_template, request, redirect
from markdown import markdown
import os
import re
import random

app = Flask(__name__)

# Jinja tweaks
app.jinja_options['trim_blocks'] = True

# TODO: use Flask configuration functionalities
app.config['DOMAIN_NAME'] = 'cansucc.my'
app.config['REGEX_DATA'] = rf"(.+)\.{app.config['DOMAIN_NAME']}"
app.config['MARKDOWN_DATA_DIR'] = 'markdown_docs'

# I have no regrets.
flavorful_text = ['dick', 'dong', 'ass']


@app.errorhandler(500)
def youfuckeditup(e):
    return render_template('youfuckeditup.html', errordata=e), 500


@app.route('/')
def home():
    matches = re.findall(app.config['REGEX_DATA'], request.host)
    if request.host == app.config['DOMAIN_NAME']:
        return render_template('homepage.html')
    elif len(matches) == 1:
        return redirect(f'/{random.choice(flavorful_text)}')
    else:
        return '', 204


@app.route('/<string:randomgarbage>')
def render_markdown(randomgarbage):
    if request.host == app.config['DOMAIN_NAME']:
        return redirect('/', 302)
    matches = re.findall(app.config['REGEX_DATA'], request.host)
    if len(matches) == 1:
        # Search for the file in disk
        filename = matches[0]
        filename = os.path.join(app.config['MARKDOWN_DATA_DIR'], filename+'.md')
        # If file not found, return 404
        if not os.path.isfile(filename):
            return render_template('index.html'), 404
        # Read markdown data
        # TODO: markdown parsing to HTML
        with open(filename, encoding='utf8') as md_file:
            if not os.path.isfile(filename):
                return render_template('index.html'), 500
            content = markdown(md_file.read())
    else:
        return render_template('index.html'), 404
    return render_template('renderrrrrrr.html',
                           document_name=matches[0],
                           content=content,
                           randomgarbage=randomgarbage)


if __name__ == '__main__':
    app.run(host='cansucc.my', port=80)
