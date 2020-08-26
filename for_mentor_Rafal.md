Załączam Ci 2 pliki:
main_prop.py
użyłam w klasie BAZOWEJ oraz Biznesowej (zamiast phone tu było bus_phone)
@property
def contact_phone(self):
        return self.phone

Nieważne jednak czy wywołuję metodę przez BaseContact czy przez BusinessContact - metoda contact zawsze bierze wartość z property z klasy biznesowej - i tutaj moje pytanie.
Czy nie jest tak dlatego, że on rozpoznaje obiekt jako wizytówkę biznesową więc stosuje metodę property dla danej klasy?
Czy raczej przez wywołanie metody Base lub Business powinien stosować property dla danego wywowłania?

Raczej mam wrażenie, że właśnie to pierwsze podejście jest poprawne i dlatego w ten sposób nie mogę dostać się do prywatnego numeru telefonu mimo, że on istnieje.

Jeśli tak jest, to zmieniłam podejście i napisałam krótką metodę, która określa czy chcemy dostać się do prywatnego czy służbowego numeru. Znajduje się ona w klasie rodzica i po wywołaniu metody contact pyta czy chcemy numer prywatny, czy służbowy. (main.py)