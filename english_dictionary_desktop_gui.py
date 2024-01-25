from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

import json

# Open the local file with json
data = json.load(open("C:\\Users\\mhmts\\PycharmProjects\\currency_converter\\data.json"))

# Take the input text from output_label and match it with other words in data.json. 
# If a word matches, the program show the description, otherwise the gui returns a text says the word doesn't exist in the dictionary.
def convert():
    w = text.text()
    w = w.lower()
    if w in data:
        results = data[w]
        output_label.setText("\n".join(results))
    else:
        output_label.setText("This word doesn't exist in the dictionary. Try another word.")

# Create the app instance
app = QApplication([])
window = QWidget()
window.setWindowTitle("English Dictionary")

# Main layout of the gui
layout = QVBoxLayout()

# Horizontal layout for text box and button
layout1 = QHBoxLayout()
layout.addLayout(layout1)

# Second layout for the text description of the word
layout2 = QVBoxLayout()
layout.addLayout(layout2)

# Text entry to enter the words
text = QLineEdit()
layout1.addWidget(text)

# Button to call description
btn = QPushButton("Convert")
layout1.addWidget(btn)
btn.clicked.connect(convert)

# Output string is set as empty. After our logic runs, this place will be replaced with the description text
output_label = QLabel("")
layout2.addWidget(output_label)
                          
window.setLayout(layout)
window.setMinimumSize(600,200)
window.show()
app.exec()