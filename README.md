# Biblioteksstyringssystem

Et simpelt kommandolinje-program skrevet i Python, der kan styre bøger og medlemmer i et bibliotek.

## Krav

- Python 3.6 eller nyere

Tjek din Python-version med:
```bash
python --version
```

## Sådan starter du programmet

1. Sørg for at alle filer ligger i samme mappe:
```
bibliotek/
├── book.py
├── member.py
├── library.py
└── main.py
```

2. Åbn en terminal, naviger til mappen og kør:
```bash
python main.py
```

## Funktioner

Når programmet kører, vises en menu med følgende muligheder:

- Tilføj, opdater eller fjern bøger
- Tilføj, opdater eller fjern medlemmer
- Udlån og aflever bøger
- Vis alle bøger eller medlemmer
- Søg efter bøger

Naviger i menuen med tal fra 1-12

## Bemærk

- Data **gemmes ikke** når programmet lukkes — alt nulstilles ved næste opstart.
- Bøger og medlemmer får automatisk tildelt et unikt ID.