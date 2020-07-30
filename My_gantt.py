#!/usr/bin/env python3
# -*- coding: utf-8-unix -*-

import datetime
import gantt
import matplotlib.pyplot as plt

# Change font default
gantt.define_font_attributes(fill='black',
                             stroke='black',
                             stroke_width=0,
                             font_family="Verdana")





# Petrus Peregrinus
p1 = gantt.Project(name='Petrus Peregrinus')
life1 = gantt.Task(name='Lifetime',
                start=datetime.date(1240,1,1),
                duration=40,
                color="#FF8080")
t1 = gantt.Task(name='published the "Epistala and Sigeam de Foucaucourt moletom de magnete"',
                start=datetime.date(1261,1,1),
                duration=8)
p1.add_task(life1)
p1.add_task(t1)


# William Gilbert
p2 = gantt.Project(name='William Gilbert')
life2 = gantt.Task(name='Lifetime',
                start=datetime.date(1540,1,1),
                duration=63,
                color="#FF8080")
p2.add_task(life2)


# E. G. von Kleist
p3 = gantt.Project(name='E. G. von Kleist')
life3 = gantt.Task(name='Lifetime',
                start=datetime.date(1700,1,1),
                duration=48,
                color="#FF8080")
p3.add_task(life3)



# Petrus van Musschenbroek
p4 = gantt.Project(name='Petrus van Musschenbroek')
life4 = gantt.Task(name='Lifetime',
                start=datetime.date(1692,1,1),
                duration=69,
                color="#FF8080")
p4.add_task(life4)



# William Watson
p5 = gantt.Project(name='William Watson')
life5 = gantt.Task(name='Lifetime',
                start=datetime.date(1715,1,1),
                duration=72,
                color="#FF8080")
p5.add_task(life5)



# Benjamin Franklin
p6 = gantt.Project(name='Benjamin Franklin')
life6 = gantt.Task(name='Lifetime',
                start=datetime.date(1706,1,1),
                duration=84,
                color="#FF8080")
p6.add_task(life6)



# Joseph Priestly
p7 = gantt.Project(name='Joseph Priestly')
life7 = gantt.Task(name='Lifetime',
                start=datetime.date(1733,1,1),
                duration=71,
                color="#FF8080")
p7.add_task(life7)



# Isaac Newton
p8 = gantt.Project(name='Isaac Newton')
life8 = gantt.Task(name='Lifetime',
                start=datetime.date(1642,1,1),
                duration=85,
                color="#FF8080")
p8.add_task(life8)



# Henry Cavendish
p9 = gantt.Project(name='Henry Cavendish')
life9 = gantt.Task(name='Lifetime',
                start=datetime.date(1731,1,1),
                duration=79,
                color="#FF8080")
p9.add_task(life9)



# James Clerk Maxwell
p10 = gantt.Project(name='James Clerk Maxwell')
life10 = gantt.Task(name='Lifetime',
                start=datetime.date(1831,1,1),
                duration=48,
                color="#FF8080")
p10.add_task(life10)



# Luis Galvani
p11 = gantt.Project(name='Luis Galvani')
life11 = gantt.Task(name='Lifetime',
                start=datetime.date(1737,1,1),
                duration=61,
                color="#FF8080")
p11.add_task(life11)



# Alesandro Volta
p12 = gantt.Project(name='Alesandro Volta')
life12 = gantt.Task(name='Lifetime',
                start=datetime.date(1745,1,1),
                duration=82,
                color="#FF8080")
p12.add_task(life12)



# Hans Christian Oersted
p13 = gantt.Project(name='Hans Christian Oersted')
life13 = gantt.Task(name='Lifetime',
                start=datetime.date(1777,1,1),
                duration=74,
                color="#FF8080")
p13.add_task(life13)



# Andr´e Marie Amp`ere
p14 = gantt.Project(name='Andr´e Marie Amp`ere')
life14 = gantt.Task(name='Lifetime',
                start=datetime.date(1775,1,1),
                duration=76,
                color="#FF8080")
p14.add_task(life14)



# Humphrey Davy
p15 = gantt.Project(name='Humphrey Davy')
life15 = gantt.Task(name='Lifetime',
                start=datetime.date(1778,1,1),
                duration=51,
                color="#FF8080")
p15.add_task(life15)



# Michael Faraday
p16 = gantt.Project(name='Michael Faraday')
life16 = gantt.Task(name='Lifetime',
                start=datetime.date(1791,1,1),
                duration=85,
                color="#FF8080")
p16.add_task(life16)



# Pierre-Simon Laplace
p17 = gantt.Project(name='Pierre-Simon Laplace')
life17 = gantt.Task(name='Lifetime',
                start=datetime.date(1749,1,1),
                duration=78,
                color="#FF8080")
p17.add_task(life17)



# Heinrich Friedrich Emil Lenz
p18 = gantt.Project(name='Heinrich Friedrich Emil Lenz')
life18 = gantt.Task(name='Lifetime',
                start=datetime.date(1804,1,1),
                duration=61,
                color="#FF8080")
p18.add_task(life18)



# Wilhelm Weber
p19 = gantt.Project(name='Wilhelm Weber')
life19 = gantt.Task(name='Lifetime',
                start=datetime.date(1804,1,1),
                duration=87,
                color="#FF8080")
p19.add_task(life19)



# Rudolf Kohlrausch
p20 = gantt.Project(name='Rudolf Kohlrausch')
life20 = gantt.Task(name='Lifetime',
                start=datetime.date(1809,1,1),
                duration=49,
                color="#FF8080")
p20.add_task(life20)



# Armand-Hippolyte-Louis Fizeau
p21 = gantt.Project(name='Armand-Hippolyte-Louis Fizeau')
life21 = gantt.Task(name='Lifetime',
                start=datetime.date(1819,1,1),
                duration=77,
                color="#FF8080")
p21.add_task(life21)



# Albert Abraham Michelson
p22 = gantt.Project(name='Albert Abraham Michelson ')
life22 = gantt.Task(name='Lifetime',
                start=datetime.date(1852,1,1),
                duration=79,
                color="#FF8080")
p22.add_task(life22)



# Albert Einstein
p23 = gantt.Project(name='Albert Einstein')
life23 = gantt.Task(name='Lifetime',
                start=datetime.date(1879,1,1),
                duration=76,
                color="#FF8080")
p23.add_task(life23)



# Hermann von Helmholtz
p24 = gantt.Project(name='Hermann von Helmholtz')
life24 = gantt.Task(name='Lifetime',
                start=datetime.date(1821,1,1),
                duration=73,
                color="#FF8080")
p24.add_task(life24)



# Heinrich Rudolf Hertz
p25 = gantt.Project(name='Heinrich Rudolf Hertz')
life25 = gantt.Task(name='Lifetime',
                start=datetime.date(1857,1,1),
                duration=37,
                color="#FF8080")
p25.add_task(life25)



# Carl Neumann
p26 = gantt.Project(name='Carl Neumann')
life26 = gantt.Task(name='Lifetime',
                start=datetime.date(1832,1,1),
                duration=93,
                color="#FF8080")
p26.add_task(life26)



# Guglielmo Marconi
p27 = gantt.Project(name='Guglielmo Marconi')
life27 = gantt.Task(name='Lifetime',
                start=datetime.date(1874,1,1),
                duration=63,
                color="#FF8080")
p27.add_task(life27)



# Samuel F. B. Morse
p28 = gantt.Project(name='Samuel F. B. Morse')
life28 = gantt.Task(name='Lifetime',
                start=datetime.date(1791,1,1),
                duration=81,
                color="#FF8080")
p28.add_task(life28)



# Otto Von Guericke
p29 = gantt.Project(name='Otto Von Guericke')
life29 = gantt.Task(name='Lifetime',
                start=datetime.date(1602,1,1),
                duration=84,
                color="#FF8080")
p29.add_task(life29)



# Niccolo Cabeo
p30 = gantt.Project(name='Niccolo Cabeo')
life30 = gantt.Task(name='Lifetime',
                start=datetime.date(1586,1,1),
                duration=64,
                color="#FF8080")
p30.add_task(life30)



# Robert Boyle
p31 = gantt.Project(name='Robert Boyle')
life31 = gantt.Task(name='Lifetime',
                start=datetime.date(1627,1,1),
                duration=64,
                color="#FF8080")
p31.add_task(life31)



# Stephen Gray
p32 = gantt.Project(name='Stephen Gray')
life32 = gantt.Task(name='Lifetime',
                start=datetime.date(1666,1,1),
                duration=70,
                color="#FF8080")
p32.add_task(life32)



# Granville Wheler
p33 = gantt.Project(name='Granville Wheler')
life33 = gantt.Task(name='Lifetime',
                start=datetime.date(1701,1,1),
                duration=69,
                color="#FF8080")
p33.add_task(life33)



# Abbe Nollet
p34 = gantt.Project(name='Abbe Nollet')
life34 = gantt.Task(name='Lifetime',
                start=datetime.date(1700,1,1),
                duration=70,
                color="#FF8080")
p34.add_task(life34)



# Charles Dufay
p35 = gantt.Project(name='Charles Dufay')
life35 = gantt.Task(name='Lifetime',
                start=datetime.date(1698,1,1),
                duration=41,
                color="#FF8080")
p35.add_task(life35)



# John Theophilus Desaguiliers
p36 = gantt.Project(name='John Theophilus Desaguiliers')
life36 = gantt.Task(name='Lifetime',
                start=datetime.date(1683,1,1),
                duration=61,
                color="#FF8080")
p36.add_task(life36)



# Petrus van Musschenbroek
p37 = gantt.Project(name='Petrus van Musschenbroek')
life37 = gantt.Task(name='Lifetime',
                start=datetime.date(1692,1,1),
                duration=69,
                color="#FF8080")
p37.add_task(life37)



# Jean Nicolas Sebastien Allamand
p38 = gantt.Project(name='Jean Nicolas Sebastien Allamand')
life38 = gantt.Task(name='Lifetime',
                start=datetime.date(1713,1,1),
                duration=74,
                color="#FF8080")
p38.add_task(life38)



# Archibald Spencer
p39 = gantt.Project(name='Archibald Spencer')
life39 = gantt.Task(name='Lifetime',
                start=datetime.date(1698,1,1),
                duration=62,
                color="#FF8080")
p39.add_task(life39)



# Andreas Cunaeus
p40 = gantt.Project(name='Andreas Cunaeus')
life40 = gantt.Task(name='Lifetime',
                start=datetime.date(1743,1,1),
                duration=54,
                color="#FF8080")
p40.add_task(life40)



# Thomas-François Dalibard
p41 = gantt.Project(name='Thomas-François Dalibard ')
life41 = gantt.Task(name='Lifetime',
                start=datetime.date(1709,1,1),
                duration=90,
                color="#FF8080")
p41.add_task(life41)



# Georg Wilhelm Richmann
p42 = gantt.Project(name='Georg Wilhelm Richmann')
life42 = gantt.Task(name='Lifetime',
                start=datetime.date(1711,1,1),
                duration=42,
                color="#FF8080")
p42.add_task(life42)



# Alexis Clairaut
p43 = gantt.Project(name='Alexis Clairaut')
life43 = gantt.Task(name='Lifetime',
                start=datetime.date(1713,1,1),
                duration=90,
                color="#FF8080")
p43.add_task(life43)



# Sim`eon-Denis Poisson
p44 = gantt.Project(name='Sim`eon-Denis Poisson')
life44 = gantt.Task(name='Lifetime',
                start=datetime.date(1781,1,1),
                duration=59,
                color="#FF8080")
p44.add_task(life44)



# Christiaan Huygens
p45 = gantt.Project(name='Christiaan Huygens')
life45 = gantt.Task(name='Lifetime',
                start=datetime.date(1629,1,1),
                duration=66,
                color="#FF8080")
p45.add_task(life45)



# Augustin-Jean Fresnel
p46 = gantt.Project(name='Augustin-Jean Fresnel')
life46 = gantt.Task(name='Lifetime',
                start=datetime.date(1788,1,1),
                duration=39,
                color="#FF8080")
p46.add_task(life46)



# Thomas Young
p47 = gantt.Project(name='Thomas Young')
life47 = gantt.Task(name='Lifetime',
                start=datetime.date(1773,1,1),
                duration=56,
                color="#FF8080")
p47.add_task(life47)



# Dominique Francois Jean Arago
p48 = gantt.Project(name='Dominique Francois Jean Arago')
life48 = gantt.Task(name='Lifetime',
                start=datetime.date(1786,1,1),
                duration=67,
                color="#FF8080")
p48.add_task(life48)



# Carl Friedrich Gauss
p49 = gantt.Project(name='Carl Friedrich Gauss')
life49 = gantt.Task(name='Lifetime',
                start=datetime.date(1777,1,1),
                duration=78,
                color="#FF8080")
p49.add_task(life49)



# William Nicholson
p50 = gantt.Project(name='William Nicholson')
life50 = gantt.Task(name='Lifetime',
                start=datetime.date(1872,1,1),
                duration=77,
                color="#FF8080")
p50.add_task(life50)



# Tiberius Cavallo
p51 = gantt.Project(name='Tiberius Cavallo')
life51 = gantt.Task(name='Lifetime',
                start=datetime.date(1749,1,1),
                duration=60,
                color="#FF8080")
p51.add_task(life51)



# Abraham Bennet
p52 = gantt.Project(name='Abraham Bennet')
life52 = gantt.Task(name='Lifetime',
                start=datetime.date(1749,1,1),
                duration=50,
                color="#FF8080")
p52.add_task(life52)



# Georg Simon Ohm
p53 = gantt.Project(name='Georg Simon Ohm')
life53 = gantt.Task(name='Lifetime',
                start=datetime.date(1789,1,1),
                duration=65,
                color="#FF8080")
p53.add_task(life53)



# Joseph Fourier
p54 = gantt.Project(name='Joseph Fourier')
life54 = gantt.Task(name='Lifetime',
                start=datetime.date(1768,1,1),
                duration=61,
                color="#FF8080")
p54.add_task(life54)



# Charles Wheatstone
p55 = gantt.Project(name='Charles Wheatstone')
life55 = gantt.Task(name='Lifetime',
                start=datetime.date(1802,1,1),
                duration=73,
                color="#FF8080")
p55.add_task(life55)



# Jean-Baptiste Biot
p56 = gantt.Project(name='Jean-Baptiste Biot')
life56 = gantt.Task(name='Lifetime',
                start=datetime.date(1774,1,1),
                duration=88,
                color="#FF8080")
p56.add_task(life56)



# F´elix Savart
p57 = gantt.Project(name='F´elix Savart')
life57 = gantt.Task(name='Lifetime',
                start=datetime.date(1791,1,1),
                duration=50,
                color="#FF8080")
p57.add_task(life57)



# William Hyde Wollaston
p58 = gantt.Project(name='William Hyde Wollaston')
life58 = gantt.Task(name='Lifetime',
                start=datetime.date(1766,1,1),
                duration=62,
                color="#FF8080")
p58.add_task(life58)



# Pieter Zeeman
p59 = gantt.Project(name='Pieter Zeeman')
life59 = gantt.Task(name='Lifetime',
                start=datetime.date(1797,1,1),
                duration=81,
                color="#FF8080")
p59.add_task(life59)



# Carl Wolfgang Benjamin Goldschidmt
p60 = gantt.Project(name='Carl Wolfgang Benjamin Goldschidmt')
life60 = gantt.Task(name='Lifetime',
                start=datetime.date(1807,1,1),
                duration=44,
                color="#FF8080")
p60.add_task(life60)



# Moritz von Jacobi
p61 = gantt.Project(name='Moritz von Jacobi')
life61 = gantt.Task(name='Lifetime',
                start=datetime.date(1801,1,1),
                duration=73,
                color="#FF8080")
p61.add_task(life61)



# Heinrich Friedrich Emil Lenz
p62 = gantt.Project(name='Heinrich Friedrich Emil Lenz')
life62 = gantt.Task(name='Lifetime',
                start=datetime.date(1804,1,1),
                duration=61,
                color="#FF8080")
p62.add_task(life62)



# Oliver Heaviside
p63 = gantt.Project(name='Oliver Heaviside')
life63 = gantt.Task(name='Lifetime',
                start=datetime.date(1850,1,1),
                duration=75,
                color="#FF8080")
p63.add_task(life63)



# L´eon Foucault
p64 = gantt.Project(name='L´eon Foucault')
life64 = gantt.Task(name='Lifetime',
                start=datetime.date(1819,1,1),
                duration=49,
                color="#FF8080")
p64.add_task(life64)



# E. W. Morely
p65 = gantt.Project(name='E. W. Morely')
life65 = gantt.Task(name='Lifetime',
                start=datetime.date(1838,1,1),
                duration=85,
                color="#FF8080")
p65.add_task(life65)



# Bernhard Riemann
p66 = gantt.Project(name='Bernhard Riemann')
life66 = gantt.Task(name='Lifetime',
                start=datetime.date(1826,1,1),
                duration=40,
                color="#FF8080")
p66.add_task(life66)



# Rudolf Clausius
p67 = gantt.Project(name='Rudolf Clausius')
life67 = gantt.Task(name='Lifetime',
                start=datetime.date(1822,1,1),
                duration=66,
                color="#FF8080")
p67.add_task(life67)


#Create master project
p = gantt.Project(name='Gantt')

#add other projects into one
p.add_task(p1)
p.add_task(p2)
p.add_task(p3)
p.add_task(p4)
p.add_task(p5)
p.add_task(p6)
p.add_task(p7)
p.add_task(p8)
p.add_task(p9)
p.add_task(p10)
p.add_task(p11)
p.add_task(p12)
p.add_task(p13)
p.add_task(p14)
p.add_task(p15)
p.add_task(p16)
p.add_task(p17)
p.add_task(p18)
p.add_task(p19)
p.add_task(p20)
p.add_task(p21)
p.add_task(p22)
p.add_task(p23)
p.add_task(p24)
p.add_task(p25)
p.add_task(p26)
p.add_task(p27)
p.add_task(p28)
p.add_task(p29)
p.add_task(p30)
p.add_task(p31)
p.add_task(p32)
p.add_task(p33)
p.add_task(p34)
p.add_task(p35)
p.add_task(p36)
p.add_task(p37)
p.add_task(p38)
p.add_task(p39)
p.add_task(p40)
p.add_task(p41)
p.add_task(p42)
p.add_task(p43)
p.add_task(p44)
p.add_task(p45)
p.add_task(p46)
p.add_task(p48)
p.add_task(p49)
p.add_task(p50)
p.add_task(p51)
p.add_task(p52)
p.add_task(p53)
p.add_task(p54)
p.add_task(p55)
p.add_task(p56)
p.add_task(p57)
p.add_task(p58)
p.add_task(p59)
p.add_task(p60)
p.add_task(p61)
p.add_task(p62)
p.add_task(p63)
p.add_task(p64)
p.add_task(p65)
p.add_task(p66)
p.add_task(p67)





##########################$ MAKE DRAW ###############
p.make_svg_for_tasks(filename='Yes_gantt.svg',
                     today=datetime.date(2020,7,30),
                     start=datetime.date(1240,1,1),
                     end=datetime.date(1970,1,1),
                     scale=gantt.DRAW_WITH_MONTHLY_SCALE)

##########################$ /MAKE DRAW ###############
