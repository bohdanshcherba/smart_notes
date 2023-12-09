from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QApplication, QLineEdit, QTextEdit, QPushButton, QListWidget, QInputDialog

import json

app = QApplication([])
window = QWidget()

text = QTextEdit()
lineText = QLineEdit()
notes_list = QListWidget()
tags_list = QListWidget()

mainline = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()

create_btn = QPushButton("Create note")
btn_save = QPushButton("Save")
delete_btn = QPushButton("Delete")

add_tag_btn = QPushButton("Create note")
search_tag_save = QPushButton("Save")
delete_tag_btn = QPushButton("Delete")

line1.addWidget(text)
line2.addWidget(notes_list)
line2.addWidget(create_btn)
line2.addWidget(btn_save)
line2.addWidget(delete_btn)

line2.addWidget(tags_list)
line2.addWidget(lineText)


line2.addWidget(search_tag_save)
line2.addWidget(add_tag_btn)
line2.addWidget(delete_tag_btn)

mainline.addLayout(line1, stretch=2)
mainline.addLayout(line2, stretch=1)

window.setLayout(mainline)


def save_note():
    note_text = text.toPlainText()
    note_name = notes_list.currentItem().text()

    notes[note_name]['text'] = note_text
    writeFile()


notes = {}

def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова замітка", "Назва замітки")
    if ok and note_name != "":
        notes[note_name] = {
            "text": "",
            "tags": [],
        }
        notes_list.addItem(note_name)

def show_note():
    note_name = notes_list.currentItem().text()
    text.setText(notes[note_name]['text'])

def add_tag():
    note_name = notes_list.currentItem().text()
    tag = lineText.text()

    notes[note_name]["tags"].append(tag)
    tags_list.addItem(tag)
    writeFile()


def writeFile():
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=True, sort_keys=True, indent=4)


def del_tag():
    note_name = notes_list.currentItem().text()
    tag_name = tags_list.currentItem().text()

    notes[note_name]["tags"].remove(tag_name)

    tags_list.clear()
    tags_list.addItems(notes[note_name]['tags'])

    writeFile()




add_tag_btn.clicked.connect(add_tag)

notes_list.itemClicked.connect(show_note)

with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

notes_list.addItems(notes)

create_btn.clicked.connect(add_note)

btn_save.clicked.connect(save_note)

window.show()
app.exec_()