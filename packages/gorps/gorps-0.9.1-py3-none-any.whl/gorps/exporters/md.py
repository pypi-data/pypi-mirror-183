"""Markdown export"""

from typing import IO
from collections.abc import Iterable

from ..model import Recipe, Ingredient, IngredientGroup
from .base import TextExporterBase
from .templating import format_ingredient


class Exporter(TextExporterBase):
    name = "markdown"
    ext = "md"

    def export_stream(self, recipes: Iterable[Recipe], stream: IO[str]) -> None:
        for recipe in recipes:
            stream.write(f"# {recipe.title}\n\n")
            for ingredient in recipe.ingredients:
                if isinstance(ingredient, Ingredient):
                    write_ingredient(ingredient, stream)
                elif isinstance(ingredient, IngredientGroup):
                    stream.write(f"\n### {ingredient.name}\n\n")
                    for sub_ingredient in ingredient.ingredients:
                        write_ingredient(sub_ingredient, stream)
            stream.write(f"\n{recipe.instruction}\n")


def write_ingredient(ingredient: Ingredient, stream: IO[str]) -> None:
    stream.write(f"* {format_ingredient(ingredient)}\n")
