from dataclasses import dataclass
from typing import List

from _recipe_utils import (
    Recipe,
    CoverOptions,
    onlyon_weekdays,
    default_conv_options,
    first_n_days_of_month,
    last_n_days_of_month,
)

# Define the categories display order, optional
categories_sort: List[str] = ["News"]

# Custom conversion options: if you're not overwriting all the format options,
# it's probably better to work off a copy of the default
custom_conversion_options = default_conv_options.copy()
custom_conversion_options.update(
    {"mobi": ["--output-profile=kindle", "--mobi-file-type=both"]}
)

# Define your custom recipes list here
# Example: https://github.com/ping/newsrack-fork-test/blob/custom/_recipes_custom.py


@dataclass
class CustomTitleDateFormatRecipe(Recipe):
    # Use a different title date format from default
    def __post_init__(self):
        self.title_date_format = "%Y-%m-%d"


recipes: List[Recipe] = [
    # Custom recipe example (recipes_custom/example.recipe.py)
    Recipe(
        recipe="france24",
        slug="example-01",
        src_ext="epub",
        category="News",
        target_ext=["epub"],
        cover_options=CoverOptions(
            text_colour="black",
            background_colour="white",
        ),  # generate black cover with white text
        tags=["custom-recipe"],
    ),

]
