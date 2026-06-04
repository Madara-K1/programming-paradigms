from abc import ABC, abstractmethod


MEDIA_DATA = [
    {"type": "song", "title": "Bohemian Rhapsody", "creator": "Queen", "duration": 354, "genre": "Rock"},
    {"type": "song", "title": "Blinding Lights", "creator": "The Weeknd", "duration": 200, "genre": "Pop"},
    {"type": "podcast", "title": "Lex Fridman #400", "creator": "Lex Fridman", "duration": 7200, "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code", "creator": "Robert Martin", "duration": 25200, "chapters": 17},
]


class MediaItem(ABC):
    def __init__(self, title, creator, duration):
        if title.strip() == "":
            raise ValueError("Title cannot be empty")

        if creator.strip() == "":
            raise ValueError("Creator cannot be empty")

        if duration <= 0:
            raise ValueError("Duration must be greater than zero")

        self._title = title
        self._creator = creator
        self._duration = duration

    @property
    def title(self):
        return self._title

    @property
    def creator(self):
        return self._creator

    @property
    def duration(self):
        return self._duration

    @abstractmethod
    def describe(self):
        pass


class Song(MediaItem):
    def __init__(self, title, creator, duration, genre):
        super().__init__(title, creator, duration)
        self.genre = genre

    def describe(self):
        return f"Song: {self.title} by {self.creator} [{self.genre}] ({self.duration}s)"


class Podcast(MediaItem):
    def __init__(self, title, creator, duration, episode_number):
        super().__init__(title, creator, duration)
        self.episode_number = episode_number

    def describe(self):
        return f"Podcast: {self.title} by {self.creator} [Episode {self.episode_number}] ({self.duration}s)"


class Audiobook(MediaItem):
    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self.chapters = chapters

    def describe(self):
        return f"Audiobook: {self.title} by {self.creator} [{self.chapters} chapters] ({self.duration}s)"


class Playlist:
    def __init__(self, name, event_bus=None):
        self.name = name
        self._items = []
        self._event_bus = event_bus
        self._sort_strategy = None

    def add_item(self, item):
        if not isinstance(item, MediaItem):
            raise TypeError("Playlist only accepts MediaItem objects")

        self._items.append(item)

        if self._event_bus is not None:
            self._event_bus.publish("item_added", {"title": item.title})

    def total_duration(self):
        total = 0

        for item in self._items:
            total = total + item.duration

        return total

    def __len__(self):
        return len(self._items)

    def set_sort_strategy(self, strategy):
        self._sort_strategy = strategy

    def items_sorted(self):
        if self._sort_strategy is None:
            return list(self._items)

        return self._sort_strategy.sort(self._items)

    @property
    def items(self):
        return list(self._items)


class Library:
    def __init__(self, name):
        self.name = name
        self._playlists = {}

    def add_playlist(self, playlist):
        self._playlists[playlist.name] = playlist

    def statistics(self):
        total_items = 0
        total_duration = 0

        for playlist in self._playlists.values():
            total_items = total_items + len(playlist)
            total_duration = total_duration + playlist.total_duration()

        return {
            "total_items": total_items,
            "total_duration": total_duration
        }


class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        if event not in self._subscribers:
            self._subscribers[event] = []

        self._subscribers[event].append(callback)

    def publish(self, event, payload):
        callbacks = self._subscribers.get(event, [])

        for callback in callbacks:
            callback(payload)


class SortByTitle:
    def sort(self, items):
        return sorted(items, key=lambda item: item.title.lower())


class SortByDuration:
    def sort(self, items):
        return sorted(items, key=lambda item: item.duration)


class CatalogExporter:
    def export(self, rows):
        return self.format_header() + self.format_rows(rows)

    def format_header(self):
        raise NotImplementedError("Subclasses must implement format_header")

    def format_rows(self, rows):
        raise NotImplementedError("Subclasses must implement format_rows")


class CsvCatalogExporter(CatalogExporter):
    def format_header(self):
        return "type,title,duration\n"

    def format_rows(self, rows):
        lines = []

        for row in rows:
            line = f"{row['type']},{row['title']},{row['duration']}"
            lines.append(line)

        return "\n".join(lines)


def load_items(data):
    items = []

    for record in data:
        item_type = record["type"]

        if item_type == "song":
            item = Song(
                record["title"],
                record["creator"],
                record["duration"],
                record["genre"]
            )

        elif item_type == "podcast":
            item = Podcast(
                record["title"],
                record["creator"],
                record["duration"],
                record["episode_number"]
            )

        elif item_type == "audiobook":
            item = Audiobook(
                record["title"],
                record["creator"],
                record["duration"],
                record["chapters"]
            )

        else:
            raise ValueError("Unknown media type: " + item_type)

        items.append(item)

    return items


def run_media_hub():
    items = load_items(MEDIA_DATA)

    event_bus = EventBus()
    log = []

    event_bus.subscribe(
        "item_added",
        lambda payload: log.append(f"added:{payload['title']}")
    )

    playlist = Playlist("Main playlist", event_bus)

    for item in items:
        playlist.add_item(item)

    library = Library("My media library")
    library.add_playlist(playlist)

    for item in items:
        print(item.describe())

    print(library.statistics())
    print(log)

    playlist.set_sort_strategy(SortByTitle())
    sorted_items = playlist.items_sorted()

    sorted_titles = []

    for item in sorted_items:
        sorted_titles.append(item.title)

    print("Sorted: " + " | ".join(sorted_titles))

    rows = []

    for item in playlist.items:
        rows.append({
            "type": type(item).__name__,
            "title": item.title,
            "duration": item.duration
        })

    exporter = CsvCatalogExporter()
    print(exporter.export(rows))


if __name__ == "__main__":
    run_media_hub()
