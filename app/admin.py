from django.contrib import admin

# Register your models here.
from .models import Player, Team, MyTeam, Match

class PlayerAdmin(admin.ModelAdmin):
    list_per_page: int = 15
    model: Player

class MatchAdmin(admin.ModelAdmin):
    list_display =  ('match_date', 'show_match')
    list_filter = ('match_date',  'team_a', 'team_b')
    search_fields = ('team_a__name', 'team_b__name') # lookups no django

    def show_match(self, obj: Match):
        return f'{obj.team_a} {obj.team_a_goal} x {obj.team_b_goal} {obj.team_b}'

    show_match.short_description = 'Jogo'

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)
admin.site.register(MyTeam)
admin.site.register(Match, MatchAdmin)