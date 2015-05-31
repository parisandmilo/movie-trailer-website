__author__ = 'dklhy'

import fresh_tomatoes
import media


limitless = media.Movie("Limitless","A new drug that makes you feel limitless comes on the market", "when his girlfriend tries the drugs but chooses not to keep using them", "Bradley Cooper", "http://upload.wikimedia.org/wikipedia/en/1/17/Limitless_Poster.jpg", "https://www.youtube.com/watch?v=jOLqNOfzus4")

jeux_denfants = media.Movie("Jeux D'Enfants", "A twisted French love story about playing games in relationships", "when they open the music box and are in the 'elderly home' together", "Marion Cotillard, Guillame Canet", "http://upload.wikimedia.org/wikipedia/en/e/e7/Love_Me_If_You_Dare_movie.jpg","https://www.youtube.com/watch?v=AeNXmKvuzKI")

fermats_room = media.Movie("La Habitaci&oacute;n de Fermat", "Maths people in a closing room, thriller", "when the crazy guy reveals himself", "Not that I know of", "http://upload.wikimedia.org/wikipedia/en/8/80/FermatsRoom.png","https://www.youtube.com/watch?v=tR8H6hLhQBw")

a_team = media.Movie("The A Team", "I love it when a plan comes together.", "the end bit of course", "Liam Neeson, Bradley Cooper, cool crazy guy, cool anti-violence guy","http://upload.wikimedia.org/wikipedia/en/e/e8/A_team_poster_10.jpg","https://www.youtube.com/watch?v=z93AADd2Dpo")

taken = media.Movie("Taken", "Liam Neeson does cool shit and it's really cool", "liam neeson", "Liam Neeson, hot wife that dies in Taken 3", "http://upload.wikimedia.org/wikipedia/en/e/ed/Taken_film_poster.jpg", "https://www.youtube.com/watch?v=wCbDUREBwUg" )

django = media.Movie("Django", "Quentin Tarantino's Finest", "when i realise Leonardo DiCaprio isn't that annoying after all","Jamie Foxx, Leo DiCaprio whom i find annoying but is actually decent in this movie","http://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg","https://www.youtube.com/watch?v=eUdM9vrCbow")

avengers = media.Movie("The Avengers", "A really good superhero film with some of my faves.", "TOM HIDDLESTON", "Tom Hiddleston, RDJ, Cristina of Vicky Cristina Barca","http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")

kingsmen = media.Movie("The Kingsman", "Colin Firth has never looked this sexy.", "(except when he was in BBC's Pride &amp; Prejudice", "Colin Firth, obvs, the cool dude who's really famous, the guy who's in Burlesque and Alfred.","http://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg", "https://www.youtube.com/watch?v=kl8F-8tR8to")

dark_knight = media.Movie("The Dark Knight", "Filmed in bits at UCL, i love Christopher Nolan's direction.", "Christian Bale is awesome as Batman, and Heath Ledger is brilliant", "Christian Bale, Michael Caine", "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", "https://www.youtube.com/watch?v=yQ5U8suTUw0")

batman_begins = media.Movie("Batman Begins", "Christian Bale AND Liam Neeson???", "the training bit", "Christian Bale, Liam Neeson, Michael Caine", "http://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg", "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

dk_rises = media.Movie("The Dark Knight Rises", "Batman comes back!", "when Marion reveals everything", "Christian Bale, JGL, Tom Hardy, Marion Cotillard, Anne Hathaway", "http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg", "https://www.youtube.com/watch?v=7gFwvozMHR4")

love_and_other = media.Movie("Love and Other Disasters", "a romantic comedy worth watching", "when she thinks he's gay", "Brittany Murphy, Catherine Tate, Matthew Rhys", "http://upload.wikimedia.org/wikipedia/en/c/ca/Love_and_Other_Disasters.jpg", "https://www.youtube.com/watch?v=9qmiH4ROTtA")

movies = [batman_begins,dark_knight,dk_rises,love_and_other,kingsmen,django,avengers,taken,fermats_room,limitless,jeux_denfants,a_team]

fresh_tomatoes.open_movies_page(movies)
