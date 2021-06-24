from mysql.connector import connect
from requests import request



def insert_into_mask():
  fields = (
    'nome','sexo','email','cpf','rg','celular','cep','endereco',
    'numero','bairro','cidade','estado','peso','tipo_sanguineo','data_nasc'
  )

  masks = (
    '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'
  )

  return f"insert into `people` ({','.join(fields)}) values ({','.join(masks)})"


def person_tuple(person):
  return (
    person['nome'],person['sexo'],person['email'],
    person['cpf'].replace('.', '').replace('-', ''),
    person['rg'],person['celular'],person['cep'],person['endereco'],
    person['numero'],person['bairro'],person['cidade'],person['estado'],
    person['peso'],person['tipo_sanguineo'],
    '-'.join(person['data_nasc'].split('/')[::-1])
  )


def get_people():
  for _try in range(0,5):
    try:
      config = {
        'method': 'POST',
        'url': 'https://www.4devs.com.br/ferramentas_online.php',
        'headers': {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        'data': 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&txt_qtde=30',
        'timeout': 120
      }

      req = request(**config)

      return req.json()
    except Exception as e:
      print(str(e))


def main():
  try:
    conexao = connect(**{
      'host': 'localhost',
      'port': 3306,
      'user': 'root',
      'passwd': '3lqanijSBkqj76ovJqASRmkr9MAp9zfhdHQ8f92Iv4CmkPxPjZ',
      'database': 'test_1'
    })

    cursor = conexao.cursor()


    total_people = 0

    while total_people < 100_000:
      people = get_people()

      people_tuples = []

      for person in people:
        people_tuples.append(person_tuple(person))

      cursor.executemany(insert_into_mask(), people_tuples)

      conexao.commit()

      total_people += len(people)

      print(f"People processed = {total_people}")


    print('Success execution')
  except Exception as e:
    print(str(e))


main()
