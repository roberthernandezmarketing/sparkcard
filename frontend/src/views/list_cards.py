#
# list_cards.py
#
import flet as ft
import requests

API_URL = "https://sparkcard-api.onrender.com/api/v1/cards/"

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_50
    page.title = "Listado de Cards"
    page.scroll = ft.ScrollMode.AUTO

    cards_column = ft.Column()

    # Mostrar cargando
    loading_text = ft.Text("Cargando Fichas...", size=16, weight="bold")
    page.add(loading_text)
    page.update()

    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        cards = response.json()

        # Clear loading message
        page.controls.clear()

        # Mostrar cada card
        for card in cards:
            card_view = ft.Container(
                content=
                ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(f"Area:      {card["card_area_id"]}", size=12),
                            ft.Text(f"Subarea:   {card["card_subarea_id"]}", size=12),
                            ft.Text(f"Topico:    {card["card_topic_id"]}", size=12),
                            ft.Text(f"Subtopico: {card["card_subtopic_id"]}", size=12),
                            ft.Text(f"Dificultad: {card.get('card_diff_level_id', 'N/A')}", size=12, weight="bold"),
                        ],
                        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),

                    ft.Text(card["card_question_concept"], size=18, weight="bold"),
                    ft.Text(card["card_explanation"], size=14, italic=True),
                ]),
                padding=10,
                border=ft.border.all(2, ft.Colors.GREY),
                border_radius=10,
                bgcolor=ft.Colors.WHITE,
                margin=10
            )
            cards_column.controls.append(card_view)

        page.add(cards_column)

    except requests.RequestException as e:
        page.controls.clear()
        page.add(ft.Text(f"Error al cargar las cards: {e}", color=ft.colors.RED))

    page.update()

ft.app(target=main)
