# Assignment 2 - Media Library Hub

## Project overview

This project is a small Media Library Hub written in Python. It manages different types of media items, including songs, podcasts, and audiobooks. Each item has common information such as a title, creator, and duration, while each media type also has its own specific data.

The program creates media objects from a dataset, adds them to a playlist, stores the playlist inside a library, calculates statistics, sorts the items, records events, and exports a simple CSV catalog.

## How to run

The program can be executed from the command line with:

```bash
python media_library.py
```

## OOP example

The main OOP example is the `MediaItem` abstract class. It defines the common attributes and the abstract `describe()` method. The classes `Song`, `Podcast`, and `Audiobook` inherit from `MediaItem` and provide their own implementation of `describe()`. This shows inheritance and polymorphism because the same method produces different results depending on the object type.

The project also uses composition. A `Playlist` contains media items, and a `Library` contains playlists.

## Design pattern example

One design pattern used in the project is Strategy. The playlist can use different sorting strategies, such as `SortByTitle` or `SortByDuration`, without changing the playlist class.

The project also includes Observer through the `EventBus`, Factory Method in `load_items()`, Template Method in the exporter classes, and Facade in `run_media_hub()`.

## Example output

```text
Song: Bohemian Rhapsody by Queen [Rock] (354s)
Song: Blinding Lights by The Weeknd [Pop] (200s)
Podcast: Lex Fridman #400 by Lex Fridman [Episode 400] (7200s)
Audiobook: Clean Code by Robert Martin [17 chapters] (25200s)

{'total_items': 4, 'total_duration': 32954}

Sorted: Blinding Lights | Bohemian Rhapsody | Clean Code | Lex Fridman #400
```
