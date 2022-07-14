"""Models and helpers for media items."""
from __future__ import annotations

from dataclasses import dataclass, field, fields
from time import time
from typing import Any, Dict, List, Mapping, Optional, Set, Tuple, Union

from mashumaro import DataClassDictMixin

from music_assistant.helpers.json import json
from music_assistant.helpers.uri import create_uri
from music_assistant.helpers.util import create_sort_name, merge_lists
from music_assistant.models.enums import (
    AlbumType,
    ContentType,
    ImageType,
    LinkType,
    MediaQuality,
    MediaType,
    ProviderType,
)

MetadataTypes = Union[int, bool, str, List[str]]

JSON_KEYS = ("artists", "artist", "albums", "metadata", "provider_ids")


@dataclass(frozen=True)
class MediaItemProviderId(DataClassDictMixin):
    """Model for a MediaItem's provider id."""

    item_id: str
    prov_type: ProviderType
    prov_id: str
    available: bool = True
    quality: Optional[MediaQuality] = None
    details: Optional[str] = None
    url: Optional[str] = None

    def __hash__(self):
        """Return custom hash."""
        return hash((self.prov_id, self.item_id, self.quality))


@dataclass(frozen=True)
class MediaItemLink(DataClassDictMixin):
    """Model for a link."""

    type: LinkType
    url: str

    def __hash__(self):
        """Return custom hash."""
        return hash((self.type.value))


@dataclass(frozen=True)
class MediaItemImage(DataClassDictMixin):
    """Model for a image."""

    type: ImageType
    url: str
    is_file: bool = False  # indicator that image is local filepath instead of url

    def __hash__(self):
        """Return custom hash."""
        return hash((self.url))


@dataclass
class MediaItemMetadata(DataClassDictMixin):
    """Model for a MediaItem's metadata."""

    description: Optional[str] = None
    review: Optional[str] = None
    explicit: Optional[bool] = None
    images: Optional[List[MediaItemImage]] = None
    genres: Optional[Set[str]] = None
    mood: Optional[str] = None
    style: Optional[str] = None
    copyright: Optional[str] = None
    lyrics: Optional[str] = None
    ean: Optional[str] = None
    label: Optional[str] = None
    links: Optional[Set[MediaItemLink]] = None
    performers: Optional[Set[str]] = None
    preview: Optional[str] = None
    replaygain: Optional[float] = None
    popularity: Optional[int] = None
    # last_refresh: timestamp the (full) metadata was last collected
    last_refresh: Optional[int] = None
    # checksum: optional value to detect changes (e.g. playlists)
    checksum: Optional[str] = None

    def update(
        self,
        new_values: "MediaItemMetadata",
        allow_overwrite: bool = True,
    ) -> "MediaItemMetadata":
        """Update metadata (in-place) with new values."""
        for fld in fields(self):
            new_val = getattr(new_values, fld.name)
            if new_val is None:
                continue
            cur_val = getattr(self, fld.name)
            if isinstance(cur_val, list):
                new_val = merge_lists(cur_val, new_val)
                setattr(self, fld.name, new_val)
            elif isinstance(cur_val, set):
                new_val = cur_val.update(new_val)
                setattr(self, fld.name, new_val)
            elif cur_val is None or allow_overwrite:
                setattr(self, fld.name, new_val)
        return self


@dataclass
class MediaItem(DataClassDictMixin):
    """Base representation of a media item."""

    item_id: str
    provider: ProviderType
    name: str
    provider_ids: Set[MediaItemProviderId] = field(default_factory=set)

    # optional fields below
    metadata: MediaItemMetadata = field(default_factory=MediaItemMetadata)
    in_library: bool = False
    media_type: MediaType = MediaType.UNKNOWN
    # sort_name and uri are auto generated, do not override unless really needed
    sort_name: Optional[str] = None
    uri: Optional[str] = None
    # timestamp is used to determine when the item was added to the library
    timestamp: int = 0

    def __post_init__(self):
        """Call after init."""
        if not self.uri:
            self.uri = create_uri(self.media_type, self.provider, self.item_id)
        if not self.sort_name:
            self.sort_name = create_sort_name(self.name)

    @classmethod
    def from_db_row(cls, db_row: Mapping):
        """Create MediaItem object from database row."""
        db_row = dict(db_row)
        db_row["provider"] = "database"
        for key in JSON_KEYS:
            if key in db_row and db_row[key] is not None:
                db_row[key] = json.loads(db_row[key])
        if "in_library" in db_row:
            db_row["in_library"] = bool(db_row["in_library"])
        if db_row.get("albums"):
            db_row["album"] = db_row["albums"][0]
            db_row["disc_number"] = db_row["albums"][0]["disc_number"]
            db_row["track_number"] = db_row["albums"][0]["track_number"]
        db_row["item_id"] = str(db_row["item_id"])
        return cls.from_dict(db_row)

    def to_db_row(self) -> dict:
        """Create dict from item suitable for db."""
        return {
            key: json.dumps(value) if key in JSON_KEYS else value
            for key, value in self.to_dict().items()
            if key
            not in [
                "item_id",
                "provider",
                "media_type",
                "uri",
                "album",
                "position",
                "track_number",
                "disc_number",
            ]
        }

    @property
    def available(self):
        """Return (calculated) availability."""
        return any(x.available for x in self.provider_ids)

    @property
    def image(self) -> str | None:
        """Return (first/random) image/thumb from metadata (if any)."""
        if self.metadata is None or self.metadata.images is None:
            return None
        return next(
            (x.url for x in self.metadata.images if x.type == ImageType.THUMB), None
        )

    def add_provider_id(self, prov_id: MediaItemProviderId) -> None:
        """Add provider ID, overwrite existing entry."""
        self.provider_ids = {
            x
            for x in self.provider_ids
            if not (x.item_id == prov_id.item_id and x.prov_id == prov_id.prov_id)
        }
        self.provider_ids.add(prov_id)

    @property
    def last_refresh(self) -> int:
        """Return timestamp the metadata was last refreshed (0 if full data never retrieved)."""
        return self.metadata.last_refresh or 0

    def __hash__(self):
        """Return custom hash."""
        return hash((self.media_type, self.provider, self.item_id))


@dataclass(frozen=True)
class ItemMapping(DataClassDictMixin):
    """Representation of a minimized item object."""

    media_type: MediaType
    item_id: str
    provider: ProviderType
    name: str
    sort_name: str
    uri: str
    version: str = ""

    @classmethod
    def from_item(cls, item: "MediaItem"):
        """Create ItemMapping object from regular item."""
        return cls.from_dict(item.to_dict())

    def __hash__(self):
        """Return custom hash."""
        return hash((self.media_type, self.provider, self.item_id))


@dataclass
class Artist(MediaItem):
    """Model for an artist."""

    media_type: MediaType = MediaType.ARTIST
    musicbrainz_id: Optional[str] = None

    def __hash__(self):
        """Return custom hash."""
        return hash((self.provider, self.item_id))


@dataclass
class Album(MediaItem):
    """Model for an album."""

    media_type: MediaType = MediaType.ALBUM
    version: str = ""
    year: Optional[int] = None
    artists: List[Union[Artist, ItemMapping]] = field(default_factory=list)
    album_type: AlbumType = AlbumType.UNKNOWN
    upc: Optional[str] = None
    musicbrainz_id: Optional[str] = None  # release group id

    @property
    def artist(self) -> Artist | ItemMapping | None:
        """Return (first) artist of album."""
        if self.artists:
            return self.artists[0]
        return None

    @artist.setter
    def artist(self, artist: Union[Artist, ItemMapping]) -> None:
        """Set (first/only) artist of album."""
        self.artists = [artist]

    def __hash__(self):
        """Return custom hash."""
        return hash((self.provider, self.item_id))


@dataclass(frozen=True)
class TrackAlbumMapping(ItemMapping):
    """Model for a track that is mapped to an album."""

    disc_number: Optional[int] = None
    track_number: Optional[int] = None


@dataclass
class Track(MediaItem):
    """Model for a track."""

    media_type: MediaType = MediaType.TRACK
    duration: int = 0
    version: str = ""
    isrc: Optional[str] = None
    musicbrainz_id: Optional[str] = None  # Recording ID
    artists: List[Union[Artist, ItemMapping]] = field(default_factory=list)
    # album track only
    album: Union[Album, ItemMapping, None] = None
    albums: List[TrackAlbumMapping] = field(default_factory=list)
    disc_number: Optional[int] = None
    track_number: Optional[int] = None
    # playlist track only
    position: Optional[int] = None

    def __hash__(self):
        """Return custom hash."""
        return hash((self.provider, self.item_id))

    @property
    def image(self) -> str | None:
        """Return (first/random) image/thumb from metadata (if any)."""
        if image := super().image:
            return image
        # fallback to album image
        if self.album:
            return self.album.image
        return None

    @property
    def isrcs(self) -> Tuple[str]:
        """Split multiple values in isrc field."""
        # sometimes the isrc contains multiple values, splitted by semicolon
        if not self.isrc:
            return tuple()
        return tuple(self.isrc.split(";"))


@dataclass
class Playlist(MediaItem):
    """Model for a playlist."""

    media_type: MediaType = MediaType.PLAYLIST
    owner: str = ""
    is_editable: bool = False

    def __hash__(self):
        """Return custom hash."""
        return hash((self.provider, self.item_id))


@dataclass
class Radio(MediaItem):
    """Model for a radio station."""

    media_type: MediaType = MediaType.RADIO
    duration: int = 172800

    def to_db_row(self) -> dict:
        """Create dict from item suitable for db."""
        val = super().to_db_row()
        val.pop("duration", None)
        return val

    def __hash__(self):
        """Return custom hash."""
        return hash((self.provider, self.item_id))


@dataclass
class BrowseFolder(MediaItem):
    """Representation of a Folder used in Browse (which contains media items)."""

    media_type: MediaType = MediaType.FOLDER
    # label: a labelid that needs to be translated by the frontend
    label: str = ""
    # items (max 25) to provide in recommendation listings
    items: Optional[List[MediaItemType]] = None


MediaItemType = Union[Artist, Album, Track, Radio, Playlist, BrowseFolder]


def media_from_dict(media_item: dict) -> MediaItemType:
    """Return MediaItem from dict."""
    if media_item["media_type"] == "artist":
        return Artist.from_dict(media_item)
    if media_item["media_type"] == "album":
        return Album.from_dict(media_item)
    if media_item["media_type"] == "track":
        return Track.from_dict(media_item)
    if media_item["media_type"] == "playlist":
        return Playlist.from_dict(media_item)
    if media_item["media_type"] == "radio":
        return Radio.from_dict(media_item)
    return MediaItem.from_dict(media_item)


@dataclass
class StreamDetails(DataClassDictMixin):
    """Model for streamdetails."""

    # NOTE: the actual provider/itemid of the streamdetails may differ
    # from the connected media_item due to track linking etc.
    # the streamdetails are only used to provide details about the content
    # that is going to be streamed.

    # mandatory fields
    provider: ProviderType
    item_id: str
    content_type: ContentType
    media_type: MediaType = MediaType.TRACK
    sample_rate: int = 44100
    bit_depth: int = 16
    channels: int = 2
    # stream_title: radio streams can optionally set this field
    stream_title: Optional[str] = None
    # duration of the item to stream, copied from media_item if omitted
    duration: Optional[int] = None
    # total size in bytes of the item, calculated at eof when omitted
    size: Optional[int] = None
    # expires: timestamp this streamdetails expire
    expires: float = time() + 3600
    # data: provider specific data (not exposed externally)
    data: Optional[Any] = None
    # if the url/file is supported by ffmpeg directly, use direct stream
    direct: Optional[str] = None
    # callback: optional callback function (or coroutine) to call when the stream completes.
    # needed for streaming provivders to report what is playing
    # receives the streamdetails as only argument from which to grab
    # details such as seconds_streamed.
    callback: Any = None

    # the fields below will be set/controlled by the streamcontroller
    queue_id: Optional[str] = None
    seconds_streamed: int = 0
    seconds_skipped: int = 0
    gain_correct: Optional[float] = None
    loudness: Optional[float] = None

    def __post_serialize__(self, d: Dict[Any, Any]) -> Dict[Any, Any]:
        """Exclude internal fields from dict."""
        d.pop("data")
        d.pop("direct")
        d.pop("expires")
        d.pop("queue_id")
        d.pop("callback")
        return d

    def __str__(self):
        """Return pretty printable string of object."""
        return self.uri

    @property
    def uri(self) -> str:
        """Return uri representation of item."""
        return f"{self.provider.value}://{self.media_type.value}/{self.item_id}"
