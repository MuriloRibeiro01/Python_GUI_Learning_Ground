import tkinter as tk

COR_BACKGROUND = "#57537e" # Roxo escuro
COR_PRIMARIA = "#b5afdf" # Roxo claro
COR_SECUNDARIA = "#8681af" # Roxo médio
COR_BOTAO = "#2f1d85" # Roxo escuro para caramba

root = tk.Tk() # Cria uma janela principal para a GUI, usado só UMA VEZ no INÍCIO DO CÓDIGO
root.title("Eco de texto") # Obviamente é o texto da janela
root.geometry("400x250") # Um pouco maior para ver os estilos
root.configure(bg=COR_BACKGROUND) # Cor de fundo da janela (azul-escuro)

entrada = tk.Entry(root, width=40, bd=3, relief="sunken", font=("Arial", 12), bg=COR_PRIMARIA) # Cria uma caixa de texto de linha única onde o usuário pode digitar
# width: largura em caracteres
# bd: largura da borda
# relief: estilo da borda
# font: tipo e tamanho da fonte

entrada.pack(pady=15) # Empilha a entrada primeiro.

def processar_texto(texto_recebido): # Função criada para retornar o texto que o usuário digitou na caixa.

    return f"Você disse: {texto_recebido}"


def acao_do_botao(): # Função que orquestra a obtenção, processamento e exibição do texto da GUI.

    texto_recebido = entrada.get() # Ele PEGA a entrada da GUI

    resultado_do_processamento = processar_texto(texto_recebido) # CHAMA a função "cérebro" (processar_texto) com a entrada.

    rotulo.config(text=resultado_do_processamento) # ATUALIZA o rótulo com cores.


botao = tk.Button(root, text="Ecoar!", command=acao_do_botao,
                  bg=COR_BOTAO, fg="white", # Cores do botão em si
                  font=("Helvetica", 14, "bold"), # Fonte e estilo
                  padx=10, pady=5, # Preenchimento interno
                  bd=0, relief="flat" # Sem borda padrão, achatado para parecer mais moderno
                  ) # Cria um botão (obviamente)
# O commando é importante, ele é a função que será chamada quando o botão for clicado.

botao.pack(pady=5) # Empilha o botão em seguida.

rotulo = tk.Label(root, text="", font=("Courier New", 16),
                  fg=COR_PRIMARIA, bg=COR_BACKGROUND) # O label vai exibir textos e mensagens que o usuário não pode editar.

rotulo.pack() # Ele posiciona o rótulo por último.

root.mainloop()
