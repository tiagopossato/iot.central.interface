import datetime
import time
from threading import Thread

from central.placaBase.configuracao import config
from central.models import AlarmeTipo, Alarme, Ambiente
from central.log import log

"""
Cria um novo tipo de alarme
"""
def newAlarmeTipo(_codigo, _mensagem, _prioridade):
    try:
        at = AlarmeTipo(codigo=_codigo, mensagem=_mensagem, prioridade=_prioridade)
        at.save()
    except Exception as e:
        log('ALM01',str(e))

class alarmTrigger():
    # def __init__(self):
        # self.sincronizador = SincronizaAlarmes()
        # self.sincronizador.start()

    def on(_alarmeTipo_id, _ambiente):
        try:
            #verifica se o codigo do alarme já está ativo
            alm = Alarme.objects.\
                filter(alarmeTipo_id = _alarmeTipo_id, ativo = True)\
                .order_by('id').all()
        except Exception as e:
            log('ALM02.0',str(e))
            return False
        
        try:
            if(len(alm)==1):
                #O alarme já está ativo
                log('ALM02.1','O alarme '+ str(_alarmeTipo_id) + ' já está ativo')
                return True
            if(len(alm)>1):
                log('ALM02.2','Erro, existe mais de um alarme do tipo: '\
                + str(_alarmeTipo_id) + ' ativo, inativando os mais velhos')
                for x in range(len(alm)-1):
                    alm[x].tempoInativacao=int(time.time())
                    alm[x].ativo = False
                    alm[x].syncInativacao = False
                    alm[x].save()
                    # if(self.sincronizador.isAlive() == False):
                    #     self.sincronizador.run()
                return True
        except Exception as e:
            log('ALM02.3',str(e))
            return False

        #Caso nenhum problema aconteceu, insere um novo alarme na tabela
        try:
            a = Alarme(alarmeTipo_id=_alarmeTipo_id, \
                ativo=True, syncAtivacao=False, \
                ambiente_id=_ambiente,\
                tempoAtivacao=datetime.datetime.fromtimestamp(time.time()))
            a.save()

            # if(self.sincronizador.isAlive() == False):
            #     self.sincronizador.run()
            return True
        except Exception as e:
            log('ALM02.4',str(e))
            return False

    def off(_alarmeTipo_id):
        try:
            #verifica se o codigo do alarme está ativo
            alm = Alarme.objects.\
                filter(alarmeTipo_id = _alarmeTipo_id, ativo = True)\
                .order_by('id').all()
            #O alarme já está ativo, desativa
            try:
                if(len(alm)>1):
                    log('ALM03.0','Erro, existe mais de um alarme do tipo: '\
                    + str(_alarmeTipo_id) + ' ativo, inativando todos')
                if(len(alm)==0):
                    log('ALM03.1','Não existe alarme do tipo: '\
                    + str(_alarmeTipo_id) + ' ativo!')
                    return False
                for x in range(len(alm)):
                    #Altera alarme na tabela
                    alm[x].tempoInativacao=datetime.datetime.fromtimestamp(time.time())
                    alm[x].ativo = False
                    alm[x].syncInativacao = False
                    alm[x].save()
                    # if(self.sincronizador.isAlive() == False):
                    #     self.sincronizador.run()
                return True
            except Exception as e:
                log('ALM03.2',str(e))
                return False
        except Exception as e:
            log('ALM03.3',str(e))
            return False