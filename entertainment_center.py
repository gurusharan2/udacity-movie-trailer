import media
import fresh_tomatoes
# below are the favourite movies
furious_7 = media.Movie("Furious 7", "American action film directed by James Wan and written by Chris Morgan. It is the seventh installment in The Fast and the Furious franchise",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg", "https://www.youtube.com/watch?v=Skpu5HaVkOc")

the_avengers = media.Movie("The Avengers", "The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero team of the same name",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", "https://www.youtube.com/watch?v=eOrNdBpGMv8")

Ironman_1 = media.Movie("IRONMAN 1", "Iron Man is a 2008 American superhero film based on the Marvel Comics character of the same name, produced by Marvel Studios and distributed by Paramount Pictures",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", "https://www.youtube.com/watch?v=8hYlB38asDY")
Ironman_2 = media.Movie("IRONMAN 2", "Iron Man 2 is a 2010 American superhero film based on the Marvel Comics character Iron Man, produced by Marvel Studios and distributed by Paramount Pictures.1 It is the sequel to 2008's Iron Man",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg", "https://www.youtube.com/watch?v=wKtcmiifycU")
Ironman_3 = media.Movie("Ironman 3", "Iron Man 3 (stylized onscreen as Iron Man Three) is a 2013 American[4] superhero film based on the Marvel Comics character Iron Man, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.1 It is the sequel to 2008's Iron Man and 2010's Iron Man 2",
                        "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg", "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
avengers_age_of_the_ultron = media.Movie("Avengers:Age of the ultron", "Avengers: Age of Ultron is a 2015 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. It is the sequel to 2012's The Avengers and the eleventh film in the Marvel Cinematic Universe (MCU)",
                                         "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg", "https://www.youtube.com/watch?v=tmeOjFno6Do")
# array movies contain the movies
movies = [furious_7, the_avengers, Ironman_1,
          Ironman_2, Ironman_3, avengers_age_of_the_ultron]
fresh_tomatoes.open_movies_page(movies)
