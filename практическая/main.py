from flask import Flask, render_template, request, redirect
import json
import os.path

app = Flask(__name__)

class Database:
    def __init__(self):
        self.notes = self.get_notes()

    def get_notes(self):
        if os.path.exists('notes.json'):
            with open('notes.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_notes(self):
        with open('notes.json', 'w', encoding='utf-8') as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=4)

db = Database()


@app.route('/')
def index():
    return render_template('main.html', notes=db.notes)


@app.route('/<string:note_name>')
def note_details(note_name):
    for note in db.notes:
        if note['title'] == note_name:
            note['views'] += 1
            db.save_notes()
            return render_template('note.html', note=note)
    return 'Заметка не найдена'


@app.route('/add-note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    text = request.form.get('text')
    new_note = {"views": 0, "title": title, "text": text}

    for note in db.notes:
        if note['title'] == title:
            return ('Заметка с таким названием уже существует<br>'
                    '<a href="/">← Назад к списку</a>')
    db.notes.append(new_note)
    db.save_notes()
    return redirect('/')


@app.route('/top-3')
def top_3():
    top_notes = sorted(db.notes, key=lambda k: k['views'], reverse=True)[:3]
    return render_template('three notes.html', top_notes=top_notes)


if __name__ == "__main__":
    app.run(debug=True)