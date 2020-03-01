from collections import Counter


def charMaisComum(string):
    chars = [0] * 256  # caracteres no ascii
    max = -1
    ch = ''
    for i in string:
        chars[ord(i)] += 1

    for i in string:
        if max < chars[ord(i)]:
            max = chars[ord(i)]
            ch = i
    return ch


def criptar(mensagem, chave, alfabeto_ini, tamAlfabeto):
    int_chave = [ord(i)-alfabeto_ini for i in chave]
    int_mensagem = [ord(i)-alfabeto_ini for i in mensagem]
    txtCriptografado = ''
    for i in range(len(int_mensagem)):
        value = (int_mensagem[i] + int_chave[i % len(chave)]) % tamAlfabeto
        txtCriptografado += chr(value + alfabeto_ini)
    return txtCriptografado


def decriptar(txtCriptografado, chave, alfabeto_ini, tamAlfabeto):
    int_chave = [ord(i) for i in chave]
    int_txtCriptografado = [ord(i) for i in txtCriptografado]
    mensagem = ''
    for i in range(len(int_txtCriptografado)):
        value = (int_txtCriptografado[i] -
                 int_chave[i % len(chave)]) % tamAlfabeto
        mensagem += chr(value + alfabeto_ini)
    return mensagem


def quebraCifra(texto, tamChave):
    blocos = [[], [], [], []]

    for n in range(tamChave):
        # divide o texto em N arrays sendo N o tamanho da chave
        blocos[n] = texto[n::4]

    chave = ''
    for bloco in blocos:
        chave += charMaisComum(bloco)
    return chave


f = open("texto_cripto_chave04.txt")
texto = f.read()

chave = quebraCifra(texto, 4)

res = (decriptar(texto, chave, 32, 91))
print(res)
#print(criptar(res,chave,ord(' '),91))
