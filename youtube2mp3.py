#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, X, N, Text, StringVar
from ttk import Frame, Button, Style, Label, Entry
import subprocess


class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):

        self.parent.title("Youtube2mp3")
        self.style = Style()
        self.style.theme_use("default")

        frame1 = Frame(self, relief=RAISED)
        frame1.pack(fill=X, expand=True)

        self.pack(fill=BOTH, expand=True)

        self.lbl1 = Label(frame1, text="Cole aqui a link da música:")
        self.lbl1.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.linkMusica = Entry(frame1)
        self.linkMusica.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self, relief=RAISED, borderwidth=1)
        frame2.pack(fill=BOTH, expand=True)

        self.textoLabelProcessamento = StringVar()
        self.textoLabelProcessamento.set("Testando")
        self.lblProcessamento = Label(frame2, textvariable=self.textoLabelProcessamento)
        self.lblProcessamento.pack(fill=BOTH, padx=5, pady=5)


        # self.txtProcessamento = Text(frame2)
        # self.txtProcessamento.pack(fill=BOTH, pady=5, padx=5, expand=True)

        self.closeButton = Button(self, text="Sair", command=self.quit)
        self.closeButton.pack(side=RIGHT, padx=5, pady=5)
        self.baixarButton = Button(self, text="Baixa Música", command=self.baixarMusica)
        self.baixarButton.pack(side=RIGHT)
        self.centerWindow()

    def centerWindow(self):
        w = 640
        h = 480

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def baixarMusica(self):
        link = self.linkMusica.get()
        comando = "youtube-dl %s" % link
        proc = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (rel, erro) = proc.communicate()
        if erro:
            self.textoLabelProcessamento.set(erro)
        else:
            if rel:
                self.textoLabelProcessamento.set("Musica baixada com sucesso")
        #self.textoLabelProcessamento.set(self.linkMusica.get())





def main():
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
