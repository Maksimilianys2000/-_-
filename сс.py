import requests
from bs4 import BeautifulSoup
import sqlite3


conn = sqlite3.connect('search.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS websites (
        id INTEGER PRIMARY KEY,
        url TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_results (
        id INTEGER PRIMARY KEY,
        keyword TEXT,
        website_id INTEGER,
        FOREIGN KEY (website_id) REFERENCES websites (id)
    )
''')

conn.commit()


def add_website(url):
    cursor.execute('INSERT OR IGNORE INTO websites (url) VALUES (?)', (url,))
    conn.commit()


def search_and_store(keyword):
    websites = cursor.execute('SELECT * FROM websites').fetchall()

    results = []

    for website in websites:
        url = website[1]
        response = requests.get(url)
        if response.status_code == 200:
            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')
            text = soup.get_text()
            count = text.lower().count(keyword.lower())

            cursor.execute('INSERT INTO search_results (keyword, website_id) VALUES (?, ?)', (keyword, website[0]))
            conn.commit()

            results.append((url, count))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def clear_db():
    cursor.execute('DELETE FROM websites')
    cursor.execute('DELETE FROM search_results')
    conn.commit()


if __name__ == '__main__':
    while True:
        print("Выберите действие:")
        print("1. Добавить веб-сайт")
        print("2. Очистить базу данных")
        print("3. Выполнить поиск")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            url = input("Введите URL веб-сайта: ")
            add_website(url)
        elif choice == '2':
            clear_db()
            print("База данных очищена.")
        elif choice == '3':
            keyword = input("Введите ключевое слово для поиска: ")
            results = search_and_store(keyword)
            for i, result in enumerate(results, start=1):
                print(f"{i}. URL: {result[0]}, Количество вхождений: {result[1]}")
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")
