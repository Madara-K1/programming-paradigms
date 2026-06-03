
## Snippet 2
**Label**: OOP

**Concept**: Composition

**Explanation**: This snippet shows composition because the `Library` class contains and manages playlist objects. This represents a "has-a" relationship, where a library has playlists as part of its internal structure.


## Snippet 3
**Label**: Pattern

**Concept**: Strategy

**Explanation**: This snippet uses the Strategy pattern because the sorting behaviour is delegated to a separate object stored in `self._sort`. This allows the playlist to change the sorting algorithm without changing the playlist class itself.


## Snippet 4
**Label**: Pattern

**Concept**: Observer

**Explanation**: This snippet uses the Observer pattern because callbacks can subscribe to an event and are executed when that event is published. This reduces coupling, since the event publisher does not need to know the concrete behaviour of each subscriber.
