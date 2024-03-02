from dataclasses import dataclass
from typing import List

from _recipe_utils import (
    CoverOptions,
    Recipe,
    first_n_days_of_month,
    last_n_days_of_month,
    onlyat_hours,
    onlyon_days,
    onlyon_weekdays,)

# Define the categories display order, optional
categories_sort: List[str] = ["News", "Magazines", "Online Magazines", "Arts & Culture"]

# Custom conversion options: if you're not overwriting axll the format options,
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
Recipe(
        recipe="economist",
        slug="economist",
        src_ext="mobi",
        target_ext=["epub"],
        overwrite_cover=False,
        category="Magazines",
        tags=["business"],
        enable_on=onlyon_weekdays([4]),
        timeout=360,
    ),
    # Not reading this
    # Recipe(
    #     recipe="forbes-editors-picks",
    #     slug="forbes-editors-picks",
    #     src_ext="mobi",
    #     target_ext=["epub"],
    #     timeout=360,  # will glitch often and take a really long time
    #     retry_attempts=1,
    #     category="Online Magazines",
    #     tags=["business"],
    #     enable_on=onlyon_weekdays([0, 1, 2, 3, 4], -4)
    #     and onlyat_hours(list(range(8, 20)), -4),
    #     cover_options=CoverOptions(
    #         logo_path_or_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Forbes_logo.svg/1024px-Forbes_logo.svg.png"
    #     ),
    # ),
    Recipe(
        recipe="guardian",
        slug="guardian",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        cover_options=CoverOptions(
            logo_path_or_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/The_Guardian.svg/1024px-The_Guardian.svg.png"
        ),
    ),
    Recipe(
        recipe="harvard-intl-review",
        slug="harvard-intl-review",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        enable_on=onlyat_hours(list(range(11, 15))),
        cover_options=CoverOptions(
            logo_path_or_url="https://hir.harvard.edu/content/images/2020/12/HIRlogo_crimson-4.png"
        ),
    ),
    Recipe(
        recipe="london-review",
        slug="lrb",
        src_ext="mobi",
        target_ext=["epub"],
        overwrite_cover=False,
        category="Arts & Culture",
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4]),
    ),
    Recipe(
        recipe="mit-press-reader",
        slug="mit-press-reader",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4], -4),
        cover_options=CoverOptions(
            text_colour="#444444",
            logo_path_or_url="https://dhjhkxawhe8q4.cloudfront.net/mit-press/wp-content/uploads/2022/03/25123303/mitp-reader-logo_0-scaled.jpg",
        ),
    ),
    Recipe(
        recipe="mit-tech-review",
        slug="mit-tech-review-feed",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4, 5], -4),
        tags=["technology"],
        cover_options=CoverOptions(
            text_colour="#444444",
            logo_path_or_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/MIT_Technology_Review_modern_logo.svg/1024px-MIT_Technology_Review_modern_logo.svg.png",
        ),
    ),
    Recipe(
        recipe="mit-tech-review-magazine",
        slug="mit-tech-review-magazine",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        overwrite_cover=False,
        enable_on=first_n_days_of_month(7, -5) or last_n_days_of_month(7, -5),
        tags=["technology"],
    ),
    Recipe(
        recipe="nature",
        slug="nature",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        overwrite_cover=False,
        enable_on=onlyon_weekdays([2, 3, 4], 0),
        tags=["science"],
    ),
    Recipe(
        recipe="new-republic-magazine",
        slug="new-republic-magazine",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        overwrite_cover=False,
        enable_on=(first_n_days_of_month(4) or last_n_days_of_month(10))
        and onlyat_hours(list(range(8, 16))),
    ),
    Recipe(
        recipe="newyorker",
        slug="newyorker",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        overwrite_cover=False,
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4], -5),
        tags=["editorial", "commentary"],
    ),
    # don't let NYT recipes overlap to avoid throttling
    Recipe(
        recipe="nytimes-global",
        slug="nytimes-global",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        timeout=900,
        retry_attempts=0,
        enable_on=onlyat_hours(
            list(range(0, 8)) + list(range(12, 18)) + list(range(22, 24))
        ),
        cover_options=CoverOptions(
            logo_path_or_url="https://static01.nyt.com/newsgraphics/2015/12/23/masthead-2016/8118277965bda8228105578895f2f4a7aeb22ce2/nyt-logo.png"
        ),
    ),
    Recipe(
        recipe="nytimes-paper",
        slug="nytimes-print",
        src_ext="mobi",
        target_ext=["epub"],
        category="News",
        timeout=1320,
        retry_attempts=0,
        enable_on=onlyat_hours(list(range(8, 12))),
        cover_options=CoverOptions(
            logo_path_or_url="https://static01.nyt.com/newsgraphics/2015/12/23/masthead-2016/8118277965bda8228105578895f2f4a7aeb22ce2/nyt-logo.png"
        ),
    ),
    Recipe(
        recipe="nytimes-books",
        slug="nytimes-books",
        src_ext="mobi",
        target_ext=["epub"],
        category="Arts & Culture",
        timeout=300,
        retry_attempts=0,
        enable_on=onlyat_hours(list(range(18, 22))),
        cover_options=CoverOptions(
            logo_path_or_url="https://static01.nyt.com/newsgraphics/2015/12/23/masthead-2016/8118277965bda8228105578895f2f4a7aeb22ce2/nyt-logo.png"
        ),
        tags=["literature", "books"],
    ),
    Recipe(
        recipe="nytimes-magazine",
        slug="nytimes-magazine",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        overwrite_cover=False,
        enable_on=onlyon_weekdays([5]) and onlyat_hours(list(range(18, 22))),
    ),
    Recipe(
        recipe="paris-review-blog",
        slug="paris-review-blog",
        src_ext="mobi",
        target_ext=["epub"],
        category="Arts & Culture",
        enable_on=onlyat_hours(list(range(12, 18)), -5),
        cover_options=CoverOptions(
            logo_path_or_url="https://www.theparisreview.org/il/7d2a53fbaa/medium/Hadada-Circle-holding.png"
        ),
    ),
    Recipe(
        recipe="politico-magazine",
        slug="politico-magazine",
        src_ext="mobi",
        target_ext=["epub"],
        category="Online Magazines",
        enable_on=onlyon_weekdays([0, 1, 2, 3, 4, 5], -5),
        cover_options=CoverOptions(
            logo_path_or_url="https://www.politico.com/dims4/default/bbb0fd2/2147483647/resize/1160x%3E/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2F0e%2F5b%2F3cf3e0f04ca58370112ab667c255%2Fpolitico-logo.png"
        ),
    ),
    Recipe(
        recipe="scientific-american",
        slug="scientific-american",
        src_ext="mobi",
        target_ext=["epub"],
        category="Magazines",
        overwrite_cover=False,
        enable_on=onlyon_days(list(range(15, 31)), -5),  # middle of the month?
        tags=["science"],
    ),
    Recipe(
        recipe="time-magazine",
        slug="time-magazine",
        src_ext="mobi",
        target_ext=["epub"],
        overwrite_cover=False,
        category="Magazines",
        enable_on=onlyon_weekdays([3, 4, 5, 6], -4),
    ),
    Recipe(
        recipe="wired",
        slug="wired",
        src_ext="mobi",
        target_ext=["epub"],
        overwrite_cover=True,
        category="Online Magazines",
        tags=["technology"],
        enable_on=(first_n_days_of_month(7) or last_n_days_of_month(7))
        and onlyat_hours(list(range(10, 18))),
        cover_options=CoverOptions(
            logo_path_or_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Wired_logo.svg/1024px-Wired_logo.svg.png"
        ),
    ),
]
