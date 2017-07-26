import fresh_tomatoes
import media

""" 
	There are 6 movies and Each movie has 5 attributes:
	title, 
	storyline,
	poster_image_url, 
	trailer_youtube_url, 
	release_year.
"""
lord_of_ring_1 = media.Movie("The Lord of the Rings: The Fellowship of the Ring",\
	"Set in Middle-earth, the story tells of the Dark Lord Sauron (Sala Baker), who is seeking the One Ring. \
	The Ring has found its way to the young hobbit Frodo Baggins. The fate of Middle-earth hangs in the balance \
	as Frodo and eight companions who form the Fellowship of the Ring begin their journey to Mount Doom in the \
	land of Mordor, the only place where the Ring can be destroyed.",\
	"https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",\
	"https://youtu.be/V75dMMIW2B4",\
	"2001")

lord_of_ring_2 = media.Movie("The Lord of the Rings: The Two Towers",
	"Continuing the plot of The Fellowship of the Ring, the film intercuts three storylines. Frodo and Sam continue\
	 their journey towards Mordor to destroy the One Ring, meeting and joined by Gollum, the ring's former owner.\
	 Aragorn, Legolas, and Gimli come to the war-torn nation of Rohan and are reunited with the resurrected Gandalf,\
	 before fighting at the Battle of Helm's Deep. Merry and Pippin escape capture, meet Treebeard the Ent, and help\
	 to plan an attack on Isengard.",
	"https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
	"https://youtu.be/2dlRvAjU_RI",
	"2002")

lord_of_ring_3 = media.Movie("The Lord of the Rings: The Return of the King",
	"It is the third and final installment in The Lord of the Rings trilogy, following The Fellowship of the Ring and \
	The Two Towers .",
	"https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
	"https://youtu.be/y2rYRu8UW8M",
	"2003")

batman_dark_knight = media.Movie("The Dark Knight",
	"When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms\
	 with one of the greatest psychological tests of his ability to fight injustice.",
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://youtu.be/EXeTwQWrcwY",
	"2008")

godfather = media.Movie("The Godfather",
	"The story, spanning 1945 to 1955, chronicles the family under the patriarch Vito Corleone, focusing on the transformation \
	of Michael Corleone (Pacino) from reluctant family outsider to ruthless mafia boss.",
	"https://i.ytimg.com/vi/rt-r-w7Z2Ag/maxresdefault.jpg",
	"https://youtu.be/sY1S34973zA",
	"1972")

back_to_the_future = media.Movie("Back to the Future",
	"Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past in a time-traveling DeLorean invented\
	 by his close friend, the maverick scientist Doc Brown.",
	"https://upload.wikimedia.org/wikipedia/pt/9/97/BackFuturePoster.jpg",
	"https://youtu.be/TmE0Z_nLG7M",
	"1985")

#	Create  instances and print the web page

movies = [lord_of_ring_1,lord_of_ring_2,lord_of_ring_3,batman_dark_knight,godfather,back_to_the_future]
fresh_tomatoes.open_movies_page(movies)
