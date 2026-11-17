## v1.4.0-ru3 (2026-11-17)

- Полная русская локализация генератора имен боссов в байт-коде (`BossNameUtil.pretty`): теперь процедурные боссы отображают имена всех мобов (Зомби, Скелет, Слизень, Разбойник, Ведьма, Визер-скелет, Эндермен, Шалкер и др.) полностью на русском языке.
- Патч `MummifiedLeaderVariant`: замена жестко прописанного в байт-коде имени «Mummified Leader» на «Мумифицированный лидер».
- Патч `WarsteedRuntimeListener`: замена жестко прописанного имени скакуна «Warsteed» на «Боевой конь» и строки перезарядки.
- Полный перевод оставшихся описаний перков и строк actionbar в `lang/ru_ru.yml`.

# Changelog

## 1.4.0-ru2 (2026-11-17)

Boss spawn rarity fix and full item localization.

- Bytecode patch in `BossService` (`lambda$announceSpawn$12`): replaces raw Java enum names (`COMMON`, `UNCOMMON`, `RARE`, `EPIC`, `MYTHIC`) in boss spawn Actionbar with localized Russian strings («Обычный», «Необычный», «Редкий», «Эпический», «Мифический»).
- Full Russian translation of `names.yml`: all 750 equipment names, prefixes, suffixes, and mob variants.
- Completed missing perk and gem strings in `lang/ru_ru.yml`.
- Updated pre-built binary package `Theosis-1.4-RU.jar` attached in GitHub Releases.

## 1.0.0 (2026-11-11)

First public release of the Russian localization package.

- Clean, standalone Russian localization and configuration files for Theosis v1.4.
- Verified compatibility, zero style/spelling warnings.
- Pre-built binary package attached in GitHub Releases.
