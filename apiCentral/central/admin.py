from django.contrib import admin

from central.models import Log
# from central.models import AlarmeTipo
from central.models import Alarme
from central.models import PlacaExpansaoDigital
from central.models import EntradaDigital
from central.models import Ambiente
from central.models import Configuracoes
from central.models import SaidaDigital
from central.models import Sensor
from central.models import SensorGrandeza
from central.models import Leitura
from central.models import AlarmeAnalogico
from central.models import Mqtt

class LogAdmin(admin.ModelAdmin):
    def tempo_mod(self, obj):
       if(obj.tempo):
           return obj.tempo.strftime("%d %b %Y %H:%M:%S")

    readonly_fields = ('tipo','mensagem','tempo','sync',)
    list_display = ('tipo','mensagem','tempo_mod',)
    ordering = ('-tempo',)
    list_filter = ('tipo','tempo',)
    list_per_page = 50
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 0:
            return False
        else:
            return True

class AlarmeAdmin(admin.ModelAdmin):
    def tempoAtivacao_mod(self, obj):
       if(obj.tempoAtivacao):
           return obj.tempoAtivacao.strftime("%d %b %Y %H:%M:%S")

    def tempoInativacao_mod(self, obj):
       if(obj.tempoInativacao):
           return obj.tempoInativacao.strftime("%d %b %Y %H:%M:%S")

    readonly_fields = ('uid','codigoAlarme','ativo','mensagemAlarme','prioridadeAlarme','ambiente','tempoAtivacao',
                       'syncAtivacao','tempoInativacao',)
    list_display = ('mensagemAlarme','ativo','prioridadeAlarme','ambiente', 'tempoAtivacao_mod','tempoInativacao_mod',)
    list_filter = ('ativo','tempoAtivacao','ambiente','mensagemAlarme',)
    ordering = ('-ativo', '-tempoAtivacao',)
    list_per_page = EntradaDigital.objects.count() + AlarmeAnalogico.objects.count()
    
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 0:
            return False
        else:
            return True
 
class PlacaExpansaoDigitalAdmin(admin.ModelAdmin):
    list_display = ('descricao','idRede',)
    ordering = ('idRede',)
    list_per_page = 50

class EntradaDigitalAdmin(admin.ModelAdmin):
    list_display = ('nome','numero','placaExpansaoDigital','estado','ambiente','triggerAlarme',)
    readonly_fields = ('estado','codigoAlarme','sync',)
    ordering = ('placaExpansaoDigital', 'numero',)
    list_per_page = 50

class AmbienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uid','ativo',)
    ordering = ('nome',)
    readonly_fields = ('uid','createdAt', 'updatedAt',)

class ConfiguracoesAdmin(admin.ModelAdmin):
    list_display = ('uidCentral','maxAlarmes','portaSerial','taxa',)
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

# class GrandezaAdmin(admin.ModelAdmin):
#     readonly_fields = ('sync',)
#     list_display = ('nome','unidade','codigo',)
#     ordering = ('codigo',)

class SensorAdmin(admin.ModelAdmin):
    readonly_fields = ('sync','uid',)
    list_display = ('descricao', 'idRede','ambiente','intervaloAtualizacao','intervaloLeitura',)
    ordering = ('idRede',)

class SensorGrandezaAdmin(admin.ModelAdmin):
    readonly_fields = ('sync',)
    list_display = ('sensor', 'grandeza','curvaCalibracao','obs',)
    ordering = ('sensor',)
    list_filter = ('sensor','grandeza',)


class LeituraAdmin(admin.ModelAdmin):
    readonly_fields = ('valor','createdAt','sync','ambiente','grandeza','sensor',)
    list_display = ('sensor','valor','grandeza','createdAt','ambiente',)
    list_filter = ('createdAt','sensor','ambiente',)
    ordering = ('-createdAt','-sensor')
    list_per_page = 20
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 0:
            return False
        else:
            return True

class AlarmeAnalogicoAdmin(admin.ModelAdmin):
    list_display = ('mensagemAlarme','prioridadeAlarme','valorAlarmeOn', 'valorAlarmeOff','grandeza','ambiente',)
    readonly_fields = ('codigoAlarme',)
    ordering = ('ambiente','mensagemAlarme',)
    list_filter = ('ambiente','grandeza',)

class MqttAdmin(admin.ModelAdmin):
    list_display = ('descricao','servidor','status',)
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True   

admin.site.register(Log, LogAdmin)
admin.site.register(Alarme, AlarmeAdmin)
admin.site.register(PlacaExpansaoDigital, PlacaExpansaoDigitalAdmin)
admin.site.register(EntradaDigital, EntradaDigitalAdmin)
admin.site.register(Ambiente, AmbienteAdmin)
admin.site.register(Configuracoes, ConfiguracoesAdmin)
admin.site.register(SaidaDigital)
admin.site.register(Mqtt, MqttAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorGrandeza, SensorGrandezaAdmin)
admin.site.register(Leitura, LeituraAdmin)
admin.site.register(AlarmeAnalogico, AlarmeAnalogicoAdmin)
admin.site.site_header = 'Administração da Central'
admin.site.site_title = 'Central'
