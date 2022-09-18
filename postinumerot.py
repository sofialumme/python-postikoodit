import json
from typing import Optional

def hae_postinumerot(postitmp: str) -> Optional[str]:

    with open('postcode_map_light.json', encoding = 'utf-8') as postinumerot_json:
        postinumerot = json.loads(postinumerot_json.read())

    postinumerot_lista = []

    postitmp = postitmp.upper().replace(' ', '')

    for numero, paikka in postinumerot.items():
        postinumerot[numero] = postinumerot[numero].replace(' ', '')

        if postinumerot[numero] == postitmp:
            postinumerot_lista.append(numero)

    postinumerot_lista.sort()

    if len(postinumerot_lista) > 0:
        return postinumerot_lista


if __name__ == '__main__':

    postitoimipaikka = input('Kirjoita postitoimipaikka: ')

    postinumerolista = hae_postinumerot(postitoimipaikka)

    if postinumerolista:
        print('Postinumerot: ' + ', '.join(postinumerolista))

    else:
        print('Tuntematon postitoimipaikka')
        