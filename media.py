import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = movie.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poaster.jpg",
                     "http://www.youtube.com/watc?v=-9ceBgWV8io")

#print(avatar.storyline)

#avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)