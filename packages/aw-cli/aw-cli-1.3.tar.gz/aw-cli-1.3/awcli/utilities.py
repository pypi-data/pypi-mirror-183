import os
import requests
from time import sleep
from bs4 import BeautifulSoup


class Anime:
    """
    Classe che rappresenta un anime.

    Attributes:
        name (str): il nome dell'anime.
        url (str): l'URL della pagina dell'anime su AnimeWorld.
        ep (int): il numero di episodi dell'anime.
    """ 

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url

    def load_episodes(self) -> None:
        """
        Cerca gli URL degli episodi dell'anime e salva il numero di episodi trovati.
        """
        self.url_episodi = episodes(self.url)
        self.ep = len(self.url_episodi)

    def get_episodio(self, ep: int) -> str:
        """
        Restituisce il link dell'episodio specificato.

        Args:
            ep (int): il numero dell'episodio.

        Returns:
            str: il link dell'episodio.
        """

        ep -= 1
        if ep in range(self.ep):
            return download(self.url_episodi[ep])
        
    def ep_name(self, ep: int) -> str:
        """
        Restituisce il nome dell'episodio specificato.

        Args:
            ep (int): il numero dell'episodio.

        Returns:
            str: il nome dell'episodio.
        """
        return f"{self.name} Ep. {ep}"

_url = "https://www.animeworld.tv"

def my_print(text: str, format: int = 1, color: str = "bianco", bg_color: str = "nero", cls: bool = False, end: str = "\n"):
    """
    Stampa il testo con il formata, colore e lo sfondo specificato.

    Args:
        text (str): il testo da stampare
        format (int, optional): il formato della stampa. Valore predefinito: 1.
        color (str, optional): il colore del testo. Valore predefinito: "bianco".
        bg_color (str, optional): il colore dello sfondo. Valore predefinito: "nero".
        cls (bool, optional): se impostato a True, pulisce lo schermo prima di stampare il testo. Valore predefinito: False.
        end (str, optional): il carattere di fine linea da utilizzare. Valore predefinito: "\n".
    """
    COLORS = {'nero': 0,'rosso': 1,'verde': 2,'giallo': 3,'blu': 4,'magenta': 5,'azzurro': 6,'bianco': 7}
    if cls:
        os.system('cls' if os.name == 'nt' else 'clear')

    print(f"\033[{format};3{COLORS[color]};4{COLORS[bg_color]}m{text}\033[1;37;40m", end=end)

def my_input(text: str, format = lambda i: i, error: str = "Seleziona una risposta valida!", cls = False):
    """
    Funzione personalizzata d'input che restituisce un input formattato sse format(input) != None

    Args:
        text (str): testo da stampare
        format (callable, optional): funzione che formatta l'input se possibile altrimenti restituisce None. Valore predefinito: funzione identità.
        error (str, optional): messaggio di errore in caso di formato errato. Valore predefinito: "Seleziona una risposta valida!".
        cls (bool, optional): se impostato a True esegue la clearscreen dopo 1 secondo. Valore predefinito: False.

    Returns:
        Input formattato dalla funzione format, se fornita. Altrimenti, restituisce l'input immutato.
    """
    while True:
        my_print(f"{text}\n>", end=" ", color="magenta")
        if (i := format(input())) is not None:
            break

        my_print(error, color="rosso")
        if cls:
            sleep(1)
            my_print("",end="", cls=True)
    return i

def search(input: str) -> list[Anime]:
    """
    Ricerca l'anime selezionato su AnimeWorld.

    Args:
        input (str): la stringa di ricerca da effettuare

    Returns:
        list[Anime]: la lista degli anime trovati
    """
    # cerco l'anime su animeworld
    my_print("Ricerco...", color="giallo")
    url_ricerca = _url + "/search?keyword=" + input.replace(" ", "+")
    bs = BeautifulSoup(requests.get(url_ricerca).text, "lxml")

    animes = list[Anime]()
    # prendo i link degli anime relativi alla ricerca
    for div in bs.find(class_='film-list').find_all(class_='inner'):
        url = _url + div.a.get('href')
        
        for a in div.find_all(class_='name'):
            name =a.text

        animes.append(Anime(name, url))

    return animes

def latest(filter = "a") -> list[Anime]:
    """
    Restituisce le ultime uscite anime su AnimeWorld.

    Args:
        filter (str, optional): può essere "d" o "s" per filtrare i risultati per versione dubbed o subbed. Valore predefinito: "a" (nessun filtro).

    Returns:
        list[Anime]: la lista degli anime trovati
    """
    bs = BeautifulSoup(requests.get(_url).text, "lxml")

    match filter:
        case 's': data_name = "sub"
        case 'd': data_name = "dub"
        case  _ : data_name = "all"
    
    animes = list[Anime]()

    div = bs.find("div", {"data-name": data_name})
    for div in div.find_all(class_='inner'):
        url = _url + div.a.get('href')
        
        for a in div.find_all(class_='name'):
            name = a.text
        for div in div.find_all(class_='ep'):
            name += " [" + div.text + "]"
        
        animes.append(Anime(name, url))

    return animes

def download(url_ep: str) -> str:
    """
    Cerca il link di download alternativo nella pagina selezionata.

    Args:
        url_ep (str): indica la pagina dell'episodio

    Returns:
        str: il link di download
    """
    bs = BeautifulSoup(requests.get(url_ep).text, "lxml")

    links = bs.find(id="download").find_all("a")
    return links[1].get('href')

def episodes(url_ep: str) -> list[str]:
    """
    Cerca i link degli episodi dell'anime nella pagina selezionata.

    Args:
        url_ep (str): indica la pagina dell'episodio

    Returns:
        list[str]: la lista con gli URL dei vari episodi trovati
    """

    # prendo l'html dalla pagina web di AW
    bs = BeautifulSoup(requests.get(url_ep).text, "lxml")

    url_episodi = list[str]()
    # cerco gli url di tutti gli episodi
    for div in bs.find_all(class_='server active'):
        for li in div.find_all(class_="episode"):
            temp = "https://www.animeworld.tv" + (li.a.get('href'))
            url_episodi.append(temp)
    return url_episodi