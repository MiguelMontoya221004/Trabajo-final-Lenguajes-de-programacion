import tkinter as tk
from PIL import Image, ImageTk

#Los archivos que faltan

emojis = {
    "()": "png/001-emoji.png",
    "xx": "png/023-cabeza-alienigena-1.png",
    "#$": "png/035-enojado-1.png",
    "!#": "png/048-fantasma.png",
    "&&": "png/003-feliz.png",
    "%%": "png/007-pensando.png",
    "==": "png/027-fresco.png",
    "__": "png/012-conmocionado-1.png",
    "//": "png/056-caca.png",
    "°°": "png/031-me-gusta-1.png",
    "??": "png/002-emoticonos.png",
    "!!¡": "png/009-triste.png",
    "++": "png/024-emoji-2.png",
    "^^": "png/030-payaso.png",
    "&&=": "png/013-preocuparse.png",
    "%%¿": "png/026-superhombre.png",
    "!!": "png/025-nerd.png",
    "::": "png/047-feliz-2.png",

}


def cargar_imagenes():
    for emoji, imagen in emojis.items():
        img = Image.open(imagen)
        img = img.resize((50, 50), Image.BILINEAR)
        emojis[emoji] = ImageTk.PhotoImage(img)


def contar_palabras(texto):
    word_count = 0

    while texto:
        found_emoji = False
        for emoji in emojis:
            if emoji in texto:
                indice = texto.find(emoji)
                frase = texto[:indice].strip()
                words = frase.split()
                word_count += len(words)
                texto = texto[indice + len(emoji):]
                found_emoji = True
                break

        if not found_emoji:
            words = texto.split()
            word_count += len(words)
            break

    return word_count


def analizador_lexicografico(texto):
    resultado_texto.config(state=tk.NORMAL)
    resultado_texto.delete("1.0", tk.END)

    word_count = contar_palabras(texto)
    emoji_count = 0

    while texto and emoji_count < 22:  # Máximo de 22 emojis
        found_emoji = False
        for emoji in emojis:
            start_index = texto.find(emoji)
            while start_index != -1 and emoji_count < 22:
                found_emoji = True
                frase = texto[:start_index].strip()
                words = frase.split()
                resultado_texto.insert(tk.END, f"{frase} ")
                resultado_texto.image_create(tk.END, image=emojis[emoji])
                resultado_texto.insert(tk.END, f" {emoji} ")
                texto = texto[start_index + len(emoji):]
                start_index = texto.find(emoji)
                emoji_count += 1

        if not found_emoji:
            words = texto.split()
            word_count += len(words)
            break

    resultado_texto.config(state=tk.DISABLED)
    etiqueta_palabras.config(text=f"Número de palabras: {word_count}")


root = tk.Tk()
root.title("Analizador de Emojis")

frame_imagen = tk.Frame(root)
frame_imagen.pack()

imagen = Image.open("logo_eafit_completo.png")
imagen = imagen.resize((100, 100))
imagen = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(frame_imagen, image=imagen)
label_imagen.pack()

frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

etiqueta = tk.Label(frame_entrada, text="Introduce el texto:")
etiqueta.pack()

entrada_texto = tk.Text(frame_entrada, width=50, height=10)
entrada_texto.pack()

boton_analizar = tk.Button(root, text="Mostrar Emojis",
                           command=lambda: analizador_lexicografico(entrada_texto.get("1.0", tk.END)))
boton_analizar.pack()

resultado_texto = tk.Text(root, width=60, height=15)
resultado_texto.pack()

frame_palabras = tk.Frame(root)
frame_palabras.pack()

etiqueta_palabras = tk.Label(frame_palabras, text="Número de palabras: 0")
etiqueta_palabras.pack()

cargar_imagenes()

root.mainloop()
