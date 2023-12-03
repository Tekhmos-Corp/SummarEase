import os
import sys
from PyQt5 import QtWidgets
from Ui_SummarEase import Ui_SumarEase
from openai import OpenAI

def get_prompt_answer(text, type):
    
    if type == "summarize":
        prompt = "Summarize: " + text 
    else:
        prompt = "Explain the following: " + text
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", temperature=1, max_tokens=40,
                                             messages=[{"role":"system", "content": prompt}])
    
    return response.choices[0].message.content


client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

class SumarEase(QtWidgets.QMainWindow):
    def __init__(self):
        super(SumarEase, self).__init__()
        self.ui = Ui_SumarEase()
        self.ui.setupUi(self)
        #if no radio button is toggled, toggle the first one. Else, do nothing
        if not self.ui.summarizeradio.isChecked() and not self.ui.explainradio.isChecked():
            self.ui.summarizeradio.toggle()
        # deselect the other radio button if one is selected
        self.ui.summarizeradio.toggled.connect(lambda: self.ui.explainradio.setChecked(False))
        self.ui.explainradio.toggled.connect(lambda: self.ui.summarizeradio.setChecked(False))
        # at button press, call button_clicked
        self.ui.send.clicked.connect(self.button_clicked)
        self.show()

    def get_input(self):
        return self.ui.Input.toPlainText()
    #Si el boton de enviar ha sido clicado, comprueba que radio button esta seleccionado y llama a la funcion correspondiente
    def button_clicked(self):
        if self.ui.summarizeradio.isChecked():
            self.summarize()
        elif self.ui.explainradio.isChecked():
            self.explain()

    def summarize(self):
        text = self.get_input()
        answer = get_prompt_answer(text, "summarize")
        self.ui.output.setPlainText(answer)
    def explain(self):
        text = self.get_input()
        answer = get_prompt_answer(text, "explain")
        self.ui.output.setPlainText(answer)
        # check if the user has clicked the button

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SumarEase()
    ui = Ui_SumarEase()
    window.show()
    sys.exit(app.exec_())
