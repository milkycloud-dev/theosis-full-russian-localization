<h1 align="center">Theosis: Full Russian Localization</h1>

<p align="center">
  Polished Russian localization package for Theosis RPG plugin v1.4 (default locale, full perk strings, rarities, names).<br>
  Полный пакет русской локализации для RPG плагина Theosis v1.4 (русский язык по умолчанию, перки, редкости, имена).
</p>

<p align="center">
  <sub>Target: Theosis v1.4 · License: MIT · Encoding: UTF-8</sub>
</p>

<p align="center">
  <a href="#english">English</a> | <a href="#русский">Русский</a>
</p>

---

<a id="english"></a>

## English

### Overview

This repository provides clean, standalone Russian localization files for **Theosis v1.4**.
It contains only configuration and text files to respect original author licensing and copyright requirements.

### Files

- `config.yml`: Configured with `default_locale: "ru_ru"`.
- `lang/ru_ru.yml`: Cleaned Russian localization file with all 2,357 keys (including `storm_javelin`).
- `rarities.yml`: Localized item rarity prefixes.
- `names.yml`: Localized RPG item and boss names.

### Installation

1. Copy `lang/ru_ru.yml` into `plugins/Theosis/lang/ru_ru.yml`.
2. In `plugins/Theosis/config.yml` set `default_locale: "ru_ru"`.
3. Restart your server.

### License

MIT License. Created by milkycloud-dev (2026).

---

<a id="русский"></a>

## Русский

### Описание

Репозиторий содержит чистые файлы русской локализации для **Theosis v1.4**.
В состав включены исключительно файлы конфигурации и переводов, без бинарных сборок, с соблюдением требований лицензий авторов.

### Файлы

- `config.yml`: Конфигурация с русским языком по умолчанию (`default_locale: "ru_ru"`).
- `lang/ru_ru.yml`: Вычитанный файл локализации на 2357 ключей (включая перк `storm_javelin`).
- `rarities.yml`: Переведенные префиксы редкостей предметов.
- `names.yml`: Сгенерированные имена предметов и боссов на русском языке.

### Установка

1. Скопируйте файл `lang/ru_ru.yml` в папку `plugins/Theosis/lang/ru_ru.yml`.
2. В файле `plugins/Theosis/config.yml` укажите `default_locale: "ru_ru"`.
3. Перезапустите сервер.

### Лицензия

MIT License. Создано milkycloud-dev (2026).
