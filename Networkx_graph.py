import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

g=nx.Graph()


g.add_edges_from([('Petrus Peregrinus','William Gilbert'),('E   G   von Kleist','Petrus van Musschenbroek'),('William Watson','Benjamin Franklin'),
('Benjamin Franklin','Joseph Priestly'),('Isaac Newton','Joseph Priestly'),
('Henry Cavendish','James Clerk Maxwell'),
('Luis Galvani','Alesandro Volta')
,('Alesandro Volta','Hans Christian Oersted'),
('Hans Christian Oersted','Andre Marie Ampere'),
('Humphrey Davy','Michael Faraday'),
('Hans Christian Oersted','Michael Faraday'),
('Michael Faraday','James Clerk Maxwell'),
('Pierre Simon Laplace','James Clerk Maxwell'),
('Heinrich Friedrich Emil Lenz','James Clerk Maxwell'),
('Andre Marie Ampere','James Clerk Maxwell'),
('Wilhelm Weber & Rudolf Kohlrausch','James Clerk Maxwell')
,('Armand Hippolyte Louis Fizeau','James Clerk Maxwell')
,('James Clerk Maxwell','Albert Abraham Michelson & E   W   Morely'), 
('James Clerk Maxwell','Albert Einstein'),
('Hermann von Helmholtz','Heinrich Rudolf Hertz'),
('James Clerk Maxwell','Heinrich Rudolf Hertz')
,('Wilhelm Weber','Heinrich Rudolf Hertz')
,('Carl Neumann','Heinrich Rudolf Hertz'),
('Heinrich Rudolf Hertz','Guglielmo Marconi'),
('Guglielmo Marconi','Samuel F   B   Morse'),
('William Gilbert','Otto Von Guericke')
,('Niccolo Cabeo','Otto Von Guericke')
,('Otto Von Guericke','Robert Boyle')
,('Stephen Gray','Granville Wheler')
,('Granville Wheler','Stephen Gray')
,('Stephen Gray','Abbe Nollet')
,('Stephen Gray','Charles Dufay')
,('Granville Wheler','Abbe Nollet')
,('Granville Wheler','Charles Dufay')
,('Benjamin Franklin','William Watson')
,('Stephen Gray','John Theophilus Desaguiliers')
,('Petrus van Musschenbroek','Jean Nicolas Sebastien Allamand')
,('Jean Nicolas Sebastien Allamand','Petrus van Musschenbroek')
,('Archibald Spencer','Benjamin Franklin')
,('Petrus van Musschenbroek','Andreas Cunaeus')
,('Benjamin Franklin','Thomas Francois Dalibard')
,('Benjamin Franklin','Georg Wilhelm Richmann')
,('Charles Dufay','William Watson')
,('Henry Cavendish','James Clerk Maxwell')
,('Pierre Simon Laplace','James Clerk Maxwell')
,('Alexis Clairaut','Pierre Simon Laplace')
,('Pierre Simon Laplace','Simeon Denis Poisson')
,('Christiaan Huygens','Augustin Jean Fresnel')
,('Thomas Young','Augustin Jean Fresnel')
,('Augustin Jean Fresnel','Simeon Denis Poisson')
,('Simeon Denis Poisson','Dominique Francois Jean Arago')
,('Wilhelm Weber','Carl Friedrich Gauss')
,('Carl Friedrich Gauss','Wilhelm Weber')
,('Benjamin Franklin','Alesandro Volta')
,('William Nicholson','Alesandro Volta')
,('Tiberius Cavallo','Alesandro Volta')
,('Abraham Bennet','Alesandro Volta')
,('Dominique Francois Jean Arago','Andre Marie Ampere')
,('Hans Christian Oersted','Dominique Francois Jean Arago')
,('Alesandro Volta','Georg Simon Ohm')
,('Joseph Fourier','Georg Simon Ohm')
,('Charles Wheatstone','Georg Simon Ohm')
,('Jean Baptiste Biot','Felix Savart')
,('Felix Savart','Jean Baptiste Biot')
,('William Hyde Wollaston','Michael Faraday')
,('Michael Faraday','Pieter Zeeman')
,('Joseph Henry','Samuel F   B   Morse')
,('Joseph Henry','Charles Wheatstone')
,('William Sturgeon','Joseph Henry')
,('Wilhelm Weber','Carl Friedrich Gauss')
,('Carl Friedrich Gauss','Wilhelm Weber')
,('Carl Wolfgang Benjamin Goldschidmt','Wilhelm Weber')
,('Carl Wolfgang Benjamin Goldschidmt','Carl Friedrich Gauss')
,('Carl Friedrich Gauss','Carl Wolfgang Benjamin Goldschidmt')
,('Rudolf Kohlrausch','Wilhelm Weber')
,('Wilhelm Weber','Rudolf Kohlrausch')
,('Sam Parker','Joseph Henry')
,('Joseph Henry','Sam Parker')
,('Rudolf Kohlrausch','James Clerk Maxwell')
,('Moritz von Jacobi','Heinrich Friedrich Emil Lenz') 
,('Oliver Heaviside','James Clerk Maxwell')
,('James Clerk Maxwell','Oliver Heaviside')
,('Albert Abraham Michelson & E   W   Morely','Albert Einstein')
,('Dominique Francois Jean Arago','Armand Hippolyte Louis Fizeau')
,('Dominique Francois Jean Arago','Leon Foucault')
,('Leon Foucault','Armand Hippolyte Louis Fizeau')
,('Armand Hippolyte Louis Fizeau','Leon Foucault')
,('Leon Foucault','Albert Abraham Michelson')
,('E   W   Morely','Albert Abraham Michelson')
,('Albert Abraham Michelson','E   W   Morely')
,('Bernhard Riemann','Carl Neumann')
,('Carl Neumann','Wilhelm Weber')
,('Carl Neumann','Rudolf Clausius')
,('Carl Neumann','James Clerk Maxwell')
,('James Clerk Maxwell','E   W   Morely'),('William Gilbert','Niccolo Cabeo'),('Jean-Baptiste Biot','Pierre-Simon Laplace'),('Bernhard Riemann','Wilhelm Weber')
])

color_map=['black'
,'violet'
,'green'
,'green'
,'green'
,'yellow'
,'blue'
,'orange'
,'orange'
,'white'
,'black'
,'orange'
,'gray'
,'orange'
,'orange'
,'white'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'black'
,'green'
,'green'
,'blue'
,'blue'
,'blue'
,'green'
,'blue'
,'green'
,'blue'
,'blue'
,'green'
,'green'
,'blue'
,'green'
,'blue'
,'blue'
,'green'
,'yellow'
,'gray'
,'pink'
,'pink'
,'red'
,'red'
,'red'
,'red'
,'violet'
,'violet'
,'blue'
,'blue'
,'blue'
,'blue'
,'blue'
,'orange'
,'blue'
,'blue'
,'blue'
,'orange'
,'orange'
,'orange'
,'violet'
,'orange'
,'orange'
,'orange'
,'violet'
,'violet'
,'black'
,'black'
,'black'
,'white'
,'white'
,'orange'
,'orange'
,'white'
,'yellow'
,'pink'
,'pink'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'violet'
,'blue'
,'blue'
,'blue'
,'blue'
,'violet'
,'black','pink','violet'
]
#g  add_node('Petrus Peregrinus')

plt.title('Graph showing the influences of physicists on other physicists')
nx.draw(g, node_color=color_map,  node_size=100,k=0.9, with_labels=False, arrow_size=20, arrowstyle='fancy')

#plt.legend()
plt.show()



