class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []

        self.playlists = []
    
    def __str__(self):
        return f'{self.nome}, {self.descricao}, {self.inscritos} {self.videos}'
    
    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

    def postar_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
            print('Video postado')
        else: 
            print('Esse video já foi postado')

    def adicionar_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
        else:
            print('Essa playlist já existe')

    def info_playlists(self):
        print(' Playlists: \n\n')
        for playlist in self.playlists:
            print(playlist.titulo)
            playlist.info_videos()



    
    
    
class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []
    @property
    def equipe(self):
                return self._equipe
            
    def adicionar_membro_equipe(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
            print(f'adicionado: {membro}')
        else: 
            print(f'O membro {membro} já foi adicionado na equipe')

    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
            print(f'{membro} removido')
        else:
            print(f'O {membro} não está na lista da equipe')



class Video:
    def __init__(self, titulo, descricao, data_publicacao= '01/01/2000'):
        self.titulo = titulo
        self.descricao = descricao

        self.visualizacoes = 0
        self.curtidas = 0
        self.dislikes = 0
        self.comentarios = []

        self.data_publicacao = data_publicacao

    #def __str__(self):
        #return f'{self.titulo},{self.descricao}, ' 

    def assistir_video(self):
        self.visualizacoes += 1

    def curtir(self):
        self.curtidas +=1

    def dislike(self):
        self.dislikes += 1

    def comentar(self,comentario):
        self.comentarios.append(comentario)

    def info(self):
        informacao = print(f"""Título do video: {self.titulo}
            Descrição: {self.descricao}
            {self.visualizacoes} - visualizações |
            {self.curtidas} - curtidas |
            {self.dislikes} - dislikes 
            data de publicação: {self.data_publicacao} \n""")
        return informacao

        
#video1 = Video('looney toons', 'desenho de criança')

#video1.info()




class Playlist:
    def __init__(self, titulo):
        self.titulo = titulo
        self.lista_videos = []

    def __str__(self):
        return f'titulo: {self.titulo} \n videos salvos na playlist: {self.lista_videos}'

    def adiciona_video_playlist(self, video):
        if video not in self.lista_videos:
            self.lista_videos.append(video)
            print(f'Video salvo com sucesso na Playlist {self.titulo}')
        else:
            print('Não foi encontrado esse video para salvar na playlist')

    def info_videos(self):
        for video in self.lista_videos:
            video.info()
    

    

            

              
    
fneto =  CanalEmpresarial('felipe neto', 'sou um cara maluco', 50000)
#fneto.adicionar_membro_equipe('Luana')
#fneto.adicionar_membro_equipe('Gabriel')
#fneto.adicionar_membro_equipe('Nahomi')
#fneto.remover_membro_equipe('Luana')
video_funny = Video('reagindo a memes', 'fiquei doido', '12/10/2025')
video_funny2 = Video('reagindo a memes 2', 'fiquei doidão', '15/10/2025')

video_cozinha = Video('faça um bolo comigo', 'melhor bolo do mundo', '06/08/2025')
video_cozinha2 = Video('cozinhe coxinha comigo', 'a tia da cantina tem inveja', '25/07/2025')

fneto.postar_video(video_funny)
fneto.postar_video(video_funny2)
fneto.postar_video(video_cozinha)
fneto.postar_video(video_cozinha2)

play_cozinha = Playlist('Cozinhemos juntos')
play_para_rir = Playlist('Para rir')

play_cozinha.adiciona_video_playlist(video_cozinha)
play_cozinha.adiciona_video_playlist(video_cozinha2)

play_para_rir.adiciona_video_playlist(video_funny)
play_para_rir.adiciona_video_playlist(video_funny2)

fneto.adicionar_playlist(play_para_rir)
fneto.adicionar_playlist(play_cozinha)

fneto.info_playlists()


#========================================================





class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade


livro1 = Livro('La bella', 'van gohg', 100)
livro2 = Livro('Hábitos atômicos', 'Freud', 300)




class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'{self._nome}, {self._idade}, {self._profissao}'
    
    def saudacao(self):
        print(f'{self._nome} diz: Olá, caso precise de um site pode me chamar!')
    

    @property
    def idade(self):
        return self._idade

    def aniversario(self):
        self._idade += 1
        print(f'{self._nome} fez {self._idade} anos!')


pessoa1 = Pessoa('nahomi', 20, 'desenvolvedora')

pessoa1.saudacao()

