from flask import Flask, render_template, request, redirect
from markdown import markdown
import os
import re

app = Flask(__name__)

# Jinja tweaks
app.jinja_options['trim_blocks'] = True
app.jinja_options['lstrip_blocks'] = True
app.config['DOMAIN_NAME'] = 'cansucc.my'
app.config['REGEX_DATA'] = rf"(.+)\.{app.config['DOMAIN_NAME']}"
app.config['MARKDOWN_DATA_DIR'] = '~/.cansucc/md_docs'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:randomgarbage>')
def render_markdown():
    content = ''
    filename = ''
    if request.host == app.config['DOMAIN_NAME']:
        return redirect('/', 302)
    matches = re.findall(app.config['REGEX_DATA'], request.host)
    if len(matches) == 1:
        # Search for the file in disk
        filename = matches[0]
        path = os.path.join(app.config['MARKDOWN_DATA_DIR'], filename)
        # If file not found, return 404
        if not os.path.isfile(path):
            return render_template('index.html'), 404
        # Read markdown data
        # TODO: markdown parsing to HTML
        with open(path, encoding='utf8') as md_file:
            if not md_file.read():
                return render_template('index.html'), 500
            content = markdown(md_file.read())
    else:
        return render_template('index.html'), 404
    return render_template('index.html', document_name=filename, content=content)


if __name__ == '__main__':
    app.run()
