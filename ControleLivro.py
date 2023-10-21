""" Neste exemplo, a classe Livro é definida com os atributos titulo, autor e num_paginas. O método __init__ é usado
para inicializar esses atributos quando um objeto da classe é criado.

O método calcular_media_caracteres_por_pagina recebe um texto como parâmetro e calcula a média de caracteres por
página. Ele conta o total de caracteres no texto e divide pelo número de páginas do livro.

No exemplo de uso, um objeto livro é criado com título "Python for Beginners", autor "John Smith" e 200 páginas. Um
texto é fornecido como exemplo. O método calcular_media_caracteres_por_pagina é chamado com o texto como argumento,
e o resultado é impresso na tela como "Média de caracteres por página: 0.75". Isso significa que, em média,
cada página do livro contém 0.75 caracteres do texto fornecido."""


class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def calcular_media_caracteres_por_pagina(self, texto):
        total_caracteres = len(texto)
        media_caracteres_por_pagina = total_caracteres / self.num_paginas

        return media_caracteres_por_pagina


if __name__ == '__main__':
    # Exemplo de uso
    livro = Livro("Python for Beginners", "John Smith", 200)
    texto = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquam lacinia, "
             "nunc nisl ultrices nunc, nec aliquet nisl nisl id nunc.")
    media_caracteres_por_pagina = livro.calcular_media_caracteres_por_pagina(texto)
    print("Média de caracteres por página:", media_caracteres_por_pagina)
