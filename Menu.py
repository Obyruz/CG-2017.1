from Tkinter import *
import sys
import os
class menuTrabalhoCG:
    def __init__(self, master):
        self.master = master
        master.title("Trabalho de CG 2017.1")

        #altera o tamanho do menu
        master.geometry("450x450")

        self.label = Label(master, text="Selecione a textura e o poligono", font=("Fixedsys",16))
        self.label.pack()

        #frame para os poligonos
        self.poligonos = Frame(master)
        self.poligonos.pack(side=RIGHT)

        #botao que fecha o menu
        self.close_button = Button(master, text="Fechar", command=master.quit)
        self.close_button.pack(in_=self.poligonos,side=BOTTOM,expand = True)
        self.close_button.config(width = 5)

        #cria menu no topo da janela, com a label Ajuda
        self.principal = Menu(master)
        self.master.config(menu=self.principal)
        self.principal.add_command(label="Ajuda", command=self.Ajuda)

        #variavel que salva a textura escolhida
        self.textura = StringVar(master)

        #botao para a textura 1
        self.imagem1 = PhotoImage(file='nekomimi.gif')
        self.botao_textura1 = Radiobutton(text='textura1',value='nekomimi.jpg',variable=self.textura)
        self.botao_textura1.pack(anchor=W)
        self.botao_textura1.config(compound=BOTTOM,image=self.imagem1)

        #botao para a textura 2
        self.imagem2 = PhotoImage(file='nekomimi2.gif')
        self.botao_textura2 = Radiobutton(text='textura2',value='nekomimi2.jpg',variable=self.textura)
        self.botao_textura2.pack(anchor=W)
        self.botao_textura2.config(compound=BOTTOM,image=self.imagem2)

        #botao para a textura 3
        self.imagem3 = PhotoImage(file='nekomimi3.gif')
        self.botao_textura3 = Radiobutton(text='textura3',value='nekomimi3.png',variable=self.textura)
        self.botao_textura3.pack(anchor=W)
        self.botao_textura3.config(compound=BOTTOM,image=self.imagem3)

        #botao para a textura 4
        self.imagem4 = PhotoImage(file='nekomimi4.gif')
        self.botao_textura4 = Radiobutton(text='textura4',value='nekomimi4.jpg',variable=self.textura)
        self.botao_textura4.pack(anchor=W)
        self.botao_textura4.config(compound=BOTTOM,image=self.imagem4)

        #botao que seleciona o cubo
        self.botao_cubo = Button(master, text="Cubo", command=self.Cubo)
        self.botao_cubo.pack(in_=self.poligonos,expand = True)
        self.botao_cubo.config(height=3, width=10)

        #botao que seleciona o tetraedro
        self.botao_tetraedro = Button(master, text="Tetraedro", command=self.Tetraedro)
        self.botao_tetraedro.pack(in_=self.poligonos,expand = True)
        self.botao_tetraedro.config(height=3, width=10)

        #botao que seleciona o octaedro
        self.botao_octaedro = Button(master, text="Octaedro", command=self.Octaedro)
        self.botao_octaedro.pack(in_=self.poligonos,expand = True)
        self.botao_octaedro.config(height=3, width=10)

        #botao que seleciona o dodecaedro
        self.botao_dodecaedro = Button(master, text="Dodecaedro", command=self.Dodecaedro)
        self.botao_dodecaedro.pack(in_=self.poligonos,expand = True)
        self.botao_dodecaedro.config(height=3, width=10)

        #botao que seleciona o icosaedro
        self.botao_icosaedro = Button(master, text="Icosaedro", command=self.Icosaedro)
        self.botao_icosaedro.pack(in_=self.poligonos,expand = True)
        self.botao_icosaedro.config(height=3, width=10)

    def Ajuda(self):
        texto_ajuda = 'Para abrir uma figura, eh preciso selecionar uma textura antes \n' \
                      ' Os comandos do sao:                                                                    \n' \
                      '  - mouse : rotaciona a figura                                                     \n'\
                      '  - \'a\' : planifica o poligono com animacao                              \n' \
                      '  - \'d\' : planifica o poligono sem animacao                              \n' \
                      '  - \'s\' : aplica zoom in                                                                 \n' \
                      '  - \'w\' : aplica zoom out                                                             \n' \
                      '  - \'t\' : aplica a textura                                                             '

        self.pop_up = Toplevel()
        self.label = Label(self.pop_up, text = texto_ajuda, height=12, width=60,font=("Fixedsys",12))
        self.label.pack(expand=True)

    def Cubo(self):
        os.system('python Trabalho.py cube.ply '+self.textura.get())

    def Tetraedro(self):
        os.system('python Trabalho.py tetrahedron.ply '+self.textura.get())

    def Octaedro(self):
        os.system('python Trabalho.py octahedron.ply '+self.textura.get())

    def Dodecaedro(self):
        os.system('python Trabalho.py dodecahedron.ply '+self.textura.get())

    def Icosaedro(self):
        os.system('python Trabalho.py icosahedron.ply '+self.textura.get())

root = Tk()
my_gui = menuTrabalhoCG(root)
root.mainloop()
