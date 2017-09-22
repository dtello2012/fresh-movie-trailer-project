import fresh_tomatoes
import media

# Usung the Movie class from the media file we create a list of movies to be displayed
batman_v_superman = media.Movie('Batman v Superman',
                                'https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg',
                                'https://www.youtube.com/watch?v=0WWzgGyAH6Y')

logan = media.Movie('Logan',
                    'https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg',
                    'https://www.youtube.com/watch?v=XaE_9pfybL4')

avengers = media.Movie('Avengers',
                       'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg',
                       'https://www.youtube.com/watch?v=eOrNdBpGMv8')

suicide_squad = media.Movie('Suicide Squad',
                            'https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png',
                            'https://www.youtube.com/watch?v=mMb-RrhTxIE')

jurassic_park = media.Movie('Jurassic Park',
                            'https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg',
                            'https://www.youtube.com/watch?v=lc0UehYemQA')


jaws = media.Movie('Jaws',
                   'https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg',
                   'https://www.youtube.com/watch?v=U1fu_sA7XhE')

back_to_the_future = media.Movie('Back To The Future',
                                 'https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg',
                                 'https://www.youtube.com/watch?v=qvsgGtivCgs')

the_neverEnding_story = media.Movie('The NeverEnding Story',
                                    'https://upload.wikimedia.org/wikipedia/en/9/9b/Neverendingstoryposter.jpg',
                                    'https://www.youtube.com/watch?v=UeFni9dOv7c')

# Movies array containing the instaces of the Movie Class
movies = [ batman_v_superman, logan, avengers, suicide_squad, jurassic_park, jaws, back_to_the_future, the_neverEnding_story]

# movie website gets created using the fresh_tomatoes class by passing the array of movies
fresh_tomatoes.open_movies_page(movies)
