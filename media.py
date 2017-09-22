import webbrowser

class Movie():
    """
    This class provides a way to create movie related information for the final project
    The following have to be provided
    - Name of the movie
    - Box art / poster url
    - youtube url

    """
    
    
    def __init__(self, movie_title, poster_image, trailer_youtube):
        # Sets instance variables to the values provided
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
