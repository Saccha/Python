from datetime import date, time, datetime

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H/%M/%S'))
    print(data_atual.strftime('%c'))#Calendário
    print(data_atual.minute)
    print(data_atual.weekday())
    print(data_atual.month)
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2020, 11, 29, 17, 9, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%y')
    print(type(data_convertida))


def trabalhando_com_date():

    data_atual = date.today()
    print(data_atual.strftime('%d-%m-%Y'))#Data atual
    print(data_atual.strftime('%A %B %Y'))#Semana,Mês e Ano, respectivamente atual

    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = (horario.strftime('%H:%M:%S'))#Hora,minuto e segundo,respectivamente
    print(type(horario_str))

if (__name__) == ('__main__'):
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
