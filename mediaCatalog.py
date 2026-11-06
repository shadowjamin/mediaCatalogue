class MediaError(Exception):
    """Custom exception for media-related errors."""
    
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj

class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

class TVSeries(Movie):
    """Child class representing an entire TV series."""
    
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)
        
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes
    
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'

class Album:
    """Parent class representing an album."""
    
    def __init__(self, title, year, musician, tracks):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not musician.strip():
            raise ValueError('Musician cannot be empty')
        if tracks <= 0:
            raise ValueError('Tracks must be positive')
        
        self.title = title
        self.year = year
        self.musician = musician
        self.tracks = tracks

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.tracks}, {self.musician}'

class Book:
    """Parent class representing a book."""
    
    def __init__(self, title, year, author, total_pages):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not author.strip():
            raise ValueError('Author cannot be empty')
        if total_pages <= 0:
            raise ValueError('Total pages must be positive')
        
        self.title = title
        self.year = year
        self.author = author
        self.total_pages = total_pages

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.total_pages}, {self.author}'


class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    
    def __init__(self):
        self.items = []
    
    def add(self, media_item):
        if not isinstance(media_item, (Movie, Album, Book)):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)
    
    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]
    
    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]

    def get_album(self):
        return [item for item in self.items if isinstance(item, Album)]

    def get_book(self):
        return [item for item in self.items if isinstance(item, Book)]
    
    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        
        movies = self.get_movies()
        series = self.get_tv_series()
        album = self.get_album()
        book = self.get_book()
        
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
        
        if len(series) > 0:
            result += '=== TV SERIES ===\n'
            for i, series in enumerate(series, 1):
                result += f'{i}. {series}\n'        
        
        if len(album) > 0:
            result += '=== ALBUMS ===\n'
            for i, album in enumerate(album, 1):
                result += f'{i}, {album}\n'

        if len(book) > 0:
            result += '=== BOOKS ===\n'
            for i, book in enumerate(book, 1):
                result += f'{i}. {book}\n'
        return result

catalogue = MediaCatalogue()

try:
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    catalogue.add(movie2)
    
    series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
    catalogue.add(series1)
    series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series2)

    album1 = Album('Icu', 2023, 'Citizen Soldier', 17)
    catalogue.add(album1)
    album2 = Album('Whatever', 2011, 'Hot Chelle Rae', 11)
    catalogue.add(album2)
    
    book1 = Book('Hitchikers Guide to the Galaxy', 1979, 'Douglas Adams', 224)
    catalogue.add(book1)
    book2 = Book('Cult of the Dead Cow', 2019, 'Joseph Menn', 272)
    catalogue.add(book2)

    print(catalogue)
except ValueError as e:
    print(f'Validation Error: {e}')
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')
