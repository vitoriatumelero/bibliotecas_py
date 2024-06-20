from PIL import Image, ImageFilter, ImageColor



imagem = Image.open("gato.webp")
imagem_filtrada = imagem.filter(ImageFilter.SHARPEN)

# Convertendo para escala de cinza
imagem_pb = imagem.convert('L')

imagem_pb.save('imagem_preto_branco.jpg')


largura, altura =imagem.size
print (f"Largura: {largura} pixels, Altura: {altura} pixels")



im1= Image.open("flor_de_lotus.png")
im2= Image.open("girassol.png")



def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

new_image=merge(im1, im2)
new_image.show()
