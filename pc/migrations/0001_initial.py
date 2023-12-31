# Generated by Django 4.2.4 on 2023-08-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PC",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.PositiveIntegerField()),
                ("actions", models.TextField()),
                ("charisma", models.PositiveIntegerField()),
                ("constitution", models.PositiveIntegerField()),
                ("description", models.CharField(max_length=256)),
                ("dexterity", models.PositiveIntegerField()),
                ("height", models.DecimalField(decimal_places=2, max_digits=5)),
                ("intelligence", models.PositiveIntegerField()),
                ("location", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=100)),
                ("notes", models.TextField()),
                ("occupation", models.CharField(max_length=100)),
                (
                    "pc_class",
                    models.CharField(
                        choices=[
                            ("barbarian", "Barbarian"),
                            ("bard", "Bard"),
                            ("cleric", "Cleric"),
                            ("druid", "Druid"),
                            ("fighter", "Fighter"),
                            ("monk", "Monk"),
                            ("paladin", "Paladin"),
                            ("ranger", "Ranger"),
                            ("rogue", "Rogue"),
                            ("sorcerer", "Sorcerer"),
                            ("warlock", "Warlock"),
                            ("wizard", "Wizard"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "race",
                    models.CharField(
                        choices=[
                            ("dragonborn", "Dragonborn"),
                            ("dwarf", "Dwarf"),
                            ("elf", "Elf"),
                            ("gnome", "Gnome"),
                            ("half-elf", "Half-Elf"),
                            ("half-orc", "Half-Orc"),
                            ("halfling", "Halfling"),
                            ("human", "Human"),
                            ("tiefling", "Tiefling"),
                        ],
                        max_length=20,
                    ),
                ),
                ("strength", models.PositiveIntegerField()),
                ("wisdom", models.PositiveIntegerField()),
            ],
        ),
    ]
