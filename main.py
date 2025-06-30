import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/users'


def get_user(user_id, base_url=BASE_URL):
    url = f'{base_url}/{user_id}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Найден пользователь: {response.json()}')
        return response.json()
    else:
        print(f'❌ Ошибка: {response.status_code}')
        return None


def create_user(data, base_url=BASE_URL):
    response = requests.post(base_url, json=data)

    if response.status_code == 201:
        print(f'Пользователь успешно создан!')
        return response.json()
    else:
        print(f'❌ Ошибка: {response.status_code}')
        return None


def update_user(user_id, data, base_url=BASE_URL):
    url = f'{base_url}/{user_id}'
    response = requests.patch(url, json=data)
    if response.status_code == 200:
        print(f'Пользователь успешно изменен!')
        return response.json()
    else:
        print(f'❌ Ошибка: {response.status_code}')
        return None


def delete_user(user_id, base_url=BASE_URL):
    url = f'{base_url}/{user_id}'
    response = requests.delete(url)

    if response.status_code in (200, 204):
        print('Пользователь успешно удален!')
        return True
    else:
        print(f'Ошибка: {response.status_code}')
        return False


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Получить пользователя")
        print("2. Создать пользователя")
        print("3. Обновить пользователя")
        print("4. Удалить пользователя")
        print("0. Выйти")

        choice = input('Введите номер действия: ')
        if choice == '1':
            user_id = input('Введите ID пользователя: ')
            get_user(user_id)

        elif choice == '2':
            name = input('Введите имя: ')
            user_name = input('Введите имя пользователя: ')
            email = input('Введите email пользователя: ')

            data = {
                'name': name,
                'username': user_name,
                'email': email
            }
            create_user(data)

        elif choice == '3':
            user_id = input('Введите ID пользователя для обновления данных:')
            name = input("Новое имя (оставьте пустым, если не менять): ")
            email = input("Новый email (оставьте пустым, если не менять): ")

            updated_data = {}
            if name:
                updated_data['name'] = name
            if email:
                updated_data['email'] = email

            if not updated_data:
                print("Нет данных для обновления.")
                continue

            update_user(user_id, updated_data)

        elif choice == '4':
            user_id = input('Введите ID пользователя для удаления данных:')
            delete_user(user_id)

        elif choice == '0':
            print('Выход из программы.')
            break

        else:
            print('Неизвестная программа.')
            continue


if __name__ == '__main__':
    main()
