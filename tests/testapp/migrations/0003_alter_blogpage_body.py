# Generated by Django 5.0.9 on 2024-09-20 07:17

import wagtail.fields

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0002_create_homepage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("heading", 0),
                    ("paragraph", 1),
                    ("image", 2),
                    ("decimal", 3),
                    ("date", 4),
                    ("datetime", 5),
                    ("gallery", 8),
                    ("video", 10),
                    ("objectives", 12),
                    ("carousel", 13),
                    ("callout", 14),
                    ("text_and_buttons", 20),
                    ("page", 21),
                    ("text_with_callable", 24),
                    ("block_with_name", 25),
                    ("advert", 26),
                    ("person", 27),
                    ("additional_interface_block", 28),
                ],
                block_lookup={
                    0: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"form_classname": "full title"},
                    ),
                    1: ("wagtail.blocks.RichTextBlock", (), {}),
                    2: ("wagtail.images.blocks.ImageChooserBlock", (), {}),
                    3: ("wagtail.blocks.DecimalBlock", (), {}),
                    4: ("wagtail.blocks.DateBlock", (), {}),
                    5: ("wagtail.blocks.DateTimeBlock", (), {}),
                    6: (
                        "wagtail.blocks.StructBlock",
                        [[("caption", 0), ("image", 2)]],
                        {},
                    ),
                    7: ("wagtail.blocks.StreamBlock", [[("image", 6)]], {}),
                    8: (
                        "wagtail.blocks.StructBlock",
                        [[("title", 0), ("images", 7)]],
                        {},
                    ),
                    9: ("wagtail.embeds.blocks.EmbedBlock", (), {"required": False}),
                    10: ("wagtail.blocks.StructBlock", [[("youtube_link", 9)]], {}),
                    11: ("wagtail.blocks.CharBlock", (), {}),
                    12: ("wagtail.blocks.ListBlock", (11,), {}),
                    13: (
                        "wagtail.blocks.StreamBlock",
                        [[("text", 0), ("image", 2), ("markup", 1)]],
                        {},
                    ),
                    14: (
                        "wagtail.blocks.StructBlock",
                        [[("text", 1), ("image", 2)]],
                        {},
                    ),
                    15: ("wagtail.blocks.TextBlock", (), {}),
                    16: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"label": "Text", "max_length": 50, "required": True},
                    ),
                    17: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"label": "Link", "max_length": 255, "required": True},
                    ),
                    18: (
                        "wagtail.blocks.StructBlock",
                        [[("button_text", 16), ("button_link", 17)]],
                        {},
                    ),
                    19: ("wagtail.blocks.ListBlock", (18,), {}),
                    20: (
                        "wagtail.blocks.StructBlock",
                        [[("text", 15), ("buttons", 19), ("mainbutton", 18)]],
                        {},
                    ),
                    21: ("wagtail.blocks.PageChooserBlock", (), {}),
                    22: ("wagtail.blocks.IntegerBlock", (), {}),
                    23: ("wagtail.blocks.FloatBlock", (), {}),
                    24: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("text", 11),
                                ("integer", 22),
                                ("decimal", 23),
                                ("page", 21),
                            ]
                        ],
                        {},
                    ),
                    25: ("wagtail.blocks.StructBlock", [[("name", 15)]], {}),
                    26: (
                        "wagtail.snippets.blocks.SnippetChooserBlock",
                        ("testapp.Advert",),
                        {},
                    ),
                    27: (
                        "wagtail.snippets.blocks.SnippetChooserBlock",
                        ("testapp.Person",),
                        {},
                    ),
                    28: ("wagtail.blocks.StructBlock", [[("additional_text", 15)]], {}),
                },
            ),
        ),
    ]
