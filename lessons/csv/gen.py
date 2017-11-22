import csv
import random


FIRST_NAMES = [
'Jess',
'Rudy',
'Vergie',
'Shemika',
'Myong',
'Willis',
'Kurt',
'Guillermo',
'Melvina',
'Gavin',
'Elizebeth',
'Kandace',
'Holley',
'Voncile',
'Catina',
'Gaylene',
'Lashonda',
'Betsy',
'Conrad',
'Senaida',
'Benjamin',
'Domenica',
'Young',
'Ignacio',
'Nickie',
'Rosena',
'Maryanne',
'Kieth',
'Earlene',
'Sonia',
'Eliseo',
'Barbie',
'Lanelle',
'Johanna',
'Irish',
'Nelda',
'Iona',
'Angelica',
'Reed',
'Ana',
'Florentina',
'Deb',
'Eleonore',
'Oliva',
'Edra',
'Christina',
'Gerald',
]

LAST_NAMES = [
'SMITH',
'JOHNSON',
'WILLIAMS',
'BROWN',
'JONES',
'MILLER',
'DAVIS',
'GARCIA',
'RODRIGUEZ',
'WILSON',
'MARTINEZ',
'ANDERSON',
'TAYLOR',
'THOMAS',
'HERNANDEZ',
'MOORE',
'MARTIN',
'JACKSON',
'THOMPSON',
'WHITE',
'LOPEZ',
'LEE',
'GONZALEZ',
'HARRIS',
'CLARK',
'LEWIS',
'ROBINSON',
'WALKER',
]

def main():
    with open('persons.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age'])

        for i in range(100):
            name = random.choice(FIRST_NAMES)
            name += ' ' + random.choice(LAST_NAMES).title()
            writer.writerow([name, random.randint(0, 100)])


if __name__ == '__main__':
    main()
