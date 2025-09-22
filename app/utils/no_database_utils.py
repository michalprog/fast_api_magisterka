import random
from typing import List
from app.models.post_person import PostPerson

# Stałe pomocnicze
NAMES = ["Adam", "Ewa", "Kamil", "Zosia", "Marek", "Julia"]
SURNAMES = ["Krawczyk", "Mazur", "Baran", "Pawlak", "Król", "Sikora"]

LOREM_IPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus urna lacus, aliquam vel quam eu, ultricies rutrum risus. Donec id sapien tempus, finibus lectus ac, pretium nisi. Sed lorem ligula, sagittis vitae turpis vitae, lobortis mattis nulla. Cras molestie ut ante id pulvinar. Curabitur auctor commodo sem, id tincidunt lorem eleifend ac. Proin pellentesque sapien libero, eu lobortis velit feugiat blandit. Ut molestie in velit nec tristique.

Phasellus et libero metus. Pellentesque in accumsan eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent vehicula turpis sed magna aliquam aliquam. Aenean nulla risus, pretium ultricies vulputate eget, varius at tellus. Nulla quis tincidunt quam. Nulla mauris nibh, semper aliquam nulla at, blandit cursus odio.

Aliquam nisi dui, lacinia a orci a, tristique dapibus nisi. Vestibulum nec blandit dolor, ut scelerisque tellus. Mauris mollis enim ac tristique ornare. Nullam nec nisi a mauris consequat semper vitae egestas lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris id dui nec nisl facilisis rhoncus. Vestibulum pulvinar accumsan nunc, ut placerat felis laoreet vel. Integer fermentum lacinia leo sed sagittis.

Fusce porta risus sit amet elit vulputate, eget suscipit ipsum luctus. Quisque elementum vel lectus placerat dapibus. Duis eu scelerisque felis, eu auctor velit. Donec interdum blandit tortor eu fermentum. Suspendisse maximus nunc lectus, a venenatis enim malesuada in. Sed imperdiet varius ex in lobortis. Mauris bibendum et arcu et tincidunt.

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam rutrum mollis libero sed mattis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed gravida aliquet pretium. Suspendisse in urna vehicula, mattis risus non, maximus risus. Integer accumsan tortor non tempus placerat. Morbi sed leo a arcu pellentesque sollicitudin quis sed ipsum. Mauris semper massa ac auctor dapibus. Vestibulum elementum pulvinar posuere.
"""

def transform_persons(persons: List[PostPerson]) -> List[PostPerson]:
    """
    Dla każdej osoby:
      - losuje nowe imię i nazwisko
      - zwiększa pensję o 500–1500
      - dopisuje Lorem Ipsum do opisu
    """
    updated_list: List[PostPerson] = []
    for p in persons:
        updated = PostPerson(
            id=p.id,
            name=random.choice(NAMES),
            surname=random.choice(SURNAMES),
            salary=p.salary + random.randint(500, 1500),
            description=(p.description or "") + "\n\n" + LOREM_IPSUM,
            role=p.role,
            active=p.active,
        )
        updated_list.append(updated)
    return updated_list
