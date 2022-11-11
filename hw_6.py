DOCUMENTS = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

DIRECTORIES = { # Перечень полок, на которых находятся документы хранится в следующем виде:
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

'''основные функции'''

def people(): # p – people – команда, которая спросит номер документа и выведет имя владельца
    doc_number = input('Введите номер документа: ')
    for document in DOCUMENTS:
        if document['number'] == doc_number:
            return f'''Владелец: {document['name']}'''
    return f'Документа с таким номером в каталоге нет'

def shelf(): # команда, кот спросит номер документа и выведет номер полки, на которой он находится
    doc_number = input('Введите номер документа: ')
    for document in DIRECTORIES.items():
        if doc_number in document[1]:
            return f'Документ находится на полке № {document[0]}'
    return f'Документа с таким номером в каталоге нет'

def list_(): # команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    list_doc = []
    for document in DOCUMENTS:
        text_doc = ('').join(f'''{document['type']} "{document['number']}" "{document['name']}"''')
        list_doc.append(text_doc)
    return (',').join(list_doc)

def add(): # команда, которая добавит
    # новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
    while True:
        command = input('Укажите через запятую: номер полки для хранения, тип документа, номер документа, ФИО владельца')
        doc_location = command.split(', ')[0]
        if doc_location in DIRECTORIES.keys():
            new_doc = {}
            doc_type = command.split(', ')[1]
            new_doc['type'] = doc_type
            doc_number = command.split(', ')[2]
            new_doc['number'] = doc_number
            doc_owner = command.split(', ')[3]
            new_doc['name'] = doc_owner
            DOCUMENTS.append(new_doc)
            DIRECTORIES[doc_location].append(doc_number)
            return f'Документ номер {doc_number} успешно добавлен на полку {doc_location}!'
        else:
            return f'Такой полки не существует'

def delete_doc(): # команда, которая спросит номер документа и удалит его
    doc_number = input('Введите номер документа: ')
    for document in DOCUMENTS:
        if doc_number in document.values():
            DOCUMENTS.remove(document)

    for shelf in DIRECTORIES.values():
        if doc_number in shelf:
            shelf.remove(doc_number)
            return f'Вы удалили документ "{doc_number}" из каталога и полки архива'
    return 'Документа с таким номером в каталоге нет'


# print(people())
# print(shelf())
# print(add())
# print(delete_doc())
print(list_())