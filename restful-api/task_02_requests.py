#!/usr/bin/python3
"""Consuming and processing data from an API using Python
"""


import json
import requests
import csv


url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])
    else:
        print(f"Error: {response.status_code}")


def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        posts_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Escribir los datos en un archivo CSV
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Escribir la cabecera
            writer.writerows(posts_data)  # Escribir las filas de datos

    else:
        print(f"Error: {response.status_code}")
