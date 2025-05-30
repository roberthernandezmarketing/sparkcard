#
# list_cards.py
#
import flet as ft
import requests

API_URL = "https://sparkcard-api.onrender.com/api/v1/cards/"

def main(page: ft.Page):
    page.title = "Listado de Cards"
    page.scroll = ft.ScrollMode.AUTO

    cards_column = ft.Column()

    # Mostrar cargando
    loading_text = ft.Text("Cargando cards...", size=16, weight="bold")
    page.add(loading_text)
    page.update()

    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        cards = response.json()

        # Limpiar loading
        page.controls.clear()

        # Mostrar cada card
        for card in cards:
            card_view = ft.Container(
                content=ft.Column([
                    ft.Text(card["question"], size=18, weight="bold"),
                    ft.Text(card["answer"], size=14, italic=True),
                    ft.Text(f"Dificultad: {card.get('diff_level_name', 'N/A')}", size=12),
                ]),
                padding=10,
                border=ft.border.all(1, ft.colors.GREY),
                border_radius=8,
                bgcolor=ft.colors.WHITE,
                margin=10
            )
            cards_column.controls.append(card_view)

        page.add(cards_column)

    except requests.RequestException as e:
        page.controls.clear()
        page.add(ft.Text(f"Error al cargar las cards: {e}", color=ft.colors.RED))

    page.update()

ft.app(target=main)
