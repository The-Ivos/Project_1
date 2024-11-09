"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jaroslav Cap
email: jarda.cap@seznam.cz
discord: jarda_75069
"""

import task_template

registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'}

# Oddelovac radku pro ucely vystupu
output_sep = 40 * '-'
column_sep = '|'
tr_terminating = 'terminating the program..'

username = input('username: ')
password = input('password: ')
print(output_sep)

# Testujeme NEplatne prihlasovaci udaje, abychom se s nimi vyporadali
# už na zacatku kodu a ne az nekde na konci mimo kontext
if not registered_users.get(username, '') == password:
    # Prihlasovaci udaje neodpovidaji ulozenemu obsahu
    print(f'unregistered user,',tr_terminating)
else:
    text_count = len(task_template.TEXTS);

    print(f'Welcome to the app, {username}')
    print(f'We have {text_count} texts to be analyzed.')
    print(output_sep)

    text_index =  input(f'Enter a number btw. 1 and {text_count} to select: ')
    if not text_index.isdigit():
        print(f'The input value \'{text_index}\' is not a decimal,', tr_terminating)
    else:
        text_index = int(text_index)
        if not (1 <= text_index <= len(task_template.TEXTS)):
            print(f'The input value is out of range,', tr_terminating)
        else:
            # Celkovy pocet slov
            total_word_count = 0

            # Delka nejdelsiho slova
            longest_word_length = 0
            # Dictionary pro roztrideni slov podle sledovanych vlastnosti (uppercase,..)
            word_stats = {}
            # Dictionary pro roztrideni slov podle delky
            words_len = {}
            # Nejvyssi pocet slov nejake delky
            max_occurence = 0

            for word in task_template.TEXTS[text_index - 1].split():
                # Orizneme interpunkcni znamenka na zacatku a konci, byla by lepsi konstanta
                # ale tohle ucel splni
                word = word.strip(',.!?')
                total_word_count += 1

                # Zaindexovani dane delky slova
                current_word_len = len(word)
                longest_word_length = max(current_word_len, longest_word_length)
                words_len[current_word_len]= words_len.get(current_word_len, 0) + 1;
                max_occurence = max(max_occurence, words_len[current_word_len])

                if word.isalpha():
                    # Kontrolujeme pouze slova bez jakychkoliv cisel, jinak je
                    # nepovazujeme ani za lowercase, uppercase
                    if word[0].isupper():
                        word_stats['titlecase'] = word_stats.get('titlecase', 0) + 1
                    if word.isupper():
                        word_stats['uppercase'] = word_stats.get('uppercase', 0) + 1
                    elif word.islower():
                        word_stats['lowercase'] = word_stats.get('lowercase', 0) + 1
                elif word.isnumeric():
                    word_stats['numeric'] = word_stats.get('numeric', 0) + 1
                    word_stats['sum'] = word_stats.get('sum', 0) + int(word)

            print(output_sep)
            print('There are', total_word_count, 'words in the selected text.')
            print('There are', word_stats.get('titlecase', 0), 'titlecase words.')
            print('There are', word_stats.get('uppercase', 0), 'uppercase words.')
            print('There are', word_stats.get('lowercase', 0), 'lowercase words.')
            print('There are', word_stats.get('numeric', 0), 'numeric strings.')
            print('The sum of all the numbers', word_stats.get('sum', 0))
            print(output_sep)

            # Spocitame sirku prvniho sloupce
            len_column_header = 'LEN'
            # Delku nejdelsiho slova prevedeme na pocet cifer a vybereme bud tu, nebo sirku nadpisu (delsi variantu)
            len_column_size = max(len(str(longest_word_length)), len(len_column_header))

            # Druhy sloupec
            occurences_column_header = 'OCCURENCES'
            # Bud pocet znaku, nebo delka nadpisu prostredniho sloupce
            occurences_column_size = max(max_occurence, len(occurences_column_header))

            # Zahlavi zarovnavame na stred, tak zajistime, aby pocet mezer okolo nadpisu
            # byl vzdy soumerny (sudy) a zahlavi tedy dobre vypadalo
            if occurences_column_size % 2:
                occurences_column_size += 1

            # Print zahlavi tabulky
            print(column_sep.join([
              # 'LEN' zarovnane vpravo
              str(len_column_header.ljust(len_column_size)),

              # 'OCCURENCES' zarovnane na stred
              occurences_column_header.center(occurences_column_size),

              # 'NR' - zarovnani neresime
              'NR.']))

            print(output_sep)


            # Vypiseme vsechny mozne delky az do aktualni zjistene a to i ty, pro ktere
            # jsme nenasli zadny vyskyt
            for index in range(1, longest_word_length + 1):
                # Pocet vyskytu iterovane delky slova
                current_occurence = words_len.get(index, 0)

                print(column_sep.join([
                  # Aktualni vypisovana delka zarovnana na sirku prvniho sloupce
                  str(index).rjust(len_column_size),

                  # Pocet vyskytu dane delky slova, reprezentovany poctem hvezdicek
                  ('*' * current_occurence).ljust(occurences_column_size),

                  # Aktualni vypisovana delka - zarovnana na sirku prvniho sloupce
                  str(current_occurence)]))