from django.db import models

# Create your models here.
# Django ORM
class Player(models.Model):
    name = models.CharField(max_length=50, verbose_name='Jogadores')
    initial_price = models.FloatField(verbose_name='Preco Inicial')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

class MyTeam(models.Model):
    players = models.ManyToManyField(Player)

    def __str__(self):
        return [player.name for player in self.players.all()].__str__()

    class Meta:
        verbose_name = 'Meu Time'
        verbose_name_plural = 'Meus Times'
    

class Match(models.Model):
    match_date = models.DateTimeField(verbose_name='Data do Jogo')
    team_a = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name='team_a_matches',
        verbose_name='Time A'
        ) # CASCADE se quisessemos deletar ao inves de proteger 
    team_a_goal = models.IntegerField(default=0, verbose_name='Gols do Time A')
    team_b = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name='team_b_matches',
        verbose_name='Time B'
        )
    team_b_goal = models.IntegerField(default=0, verbose_name='Gols do Time B')

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

    def __str__(self):
        return f'{self.team_a} x {self.team_b}'
