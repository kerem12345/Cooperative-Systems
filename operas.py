# ================== String building functions ==========================
def choose_day(some_day):  
    ret = ""
    if some_day in ["Today","today"]:                 
        ret = "Here are the performances available for today:\n\n"
        ret += "1 - Carmen\n"
        ret += "2 - La traviata\n"
        ret += "3 - Macbeth\n"

    if some_day in ["Tomorrow","tomorrow"]:
        ret = "Here are the performances available for tomorrow:\n\n"
        ret += "1 - Macbeth\n"
        ret += "2 - La traviata\n"
        ret += "3 - Parsifal\n"
        
    return ret

def get_opera(some_day, some_number):
    if some_day in ["Today","today"]:
        opera = ""
        if some_number == "1":
            opera = "Carmen"
        if some_number == "2":
            opera = "La Traviata"
        if some_number == "3":
            opera = "Macbeth"
        return opera
    if some_day in ["Tomorrow","tomorrow"]:
        opera = ""
        if some_number == "1":
            opera = "Macbeth"
        if some_number == "2":
            opera = "La Traviata"
        if some_number == "3":
            opera = "Parsifal"
        return opera

def choose_opera(some_day, some_number):
    opera = get_opera(some_day, some_number)
    ret = "You have selected {}, I can give you information about actors, the composer, plot, prices or discount information".format(opera)
    return ret

def actors(some_day, some_number):                 
    opera = get_opera(some_day, some_number)
    ret = ""
    if opera == "Carmen":
        ret = "Here is a list of actors taking part in Carmen:\n\n"
        ret += "Carmen - Anita Rachvelishvili\n"
        ret += "Don José - Charles Castronovo\n"
        ret += "Escamillo, Toreador - Sergey Kaydalov\n"
        ret += "Micaëla - Olga Kulchynska\n"
        ret += "Frasquita - Slávka Zámečníková\n"
        ret += "Mercédès - Szilvia Vörös\n"
        ret += "Zuniga - Peter Kellner\n"
        ret += "Moralès, Sergeant - Stefan Astakhov\n"
        ret += "Remendado - Carlos Osuna\n"
        ret += "Dancaïre - Michael Rakotoarivony\n"
    
    if opera == "La Traviata":
        ret = "Here is a list of actors taking part in La Traviata:\n\n"
        ret += "Violetta Valéry - Pretty Yende\n"
        ret += "Flora Bervoix - Margaret Plummer\n"
        ret += "Annina - Donna Ellen\n"
        ret += "Alfred Germont - Frédéric Antoun\n"
        ret += "George Germont - Igor Golovatenko\n"
        
    if opera == "Macbeth":
        ret = "Here is a list of actors taking part int Macbeth:\n\n"
        ret += "Macbeth - Luca Salsi\n"
        ret += "Banquo - Roberto Tagliavini\n"
        ret += "Lady Macbeth - Anna Netrebko\n"
        ret += "Macduff - Freddie De Tommaso\n"

    if opera == "Parsifal":
        ret = "Here is a list of actors taking part in Parsifal:\n\n"
        ret += "Amfortas - Ludovic Tézier\n"
        ret += "Gurnemanz - Georg Zeppenfeld\n"
        ret += "Parsifal - Jonas Kaufmann\n"
        ret += "Klingsor - Wolfgang Koch\n"
        ret += "Kundry - Elīna Garanča\n"
        ret += "Der damalige Parsifal - Nikolay Sidorenko\n"
    
    return ret

def composer(some_day, some_number):
    opera = get_opera(some_day, some_number)
    ret = ""
    if opera == "Carmen":
        ret = """
            Georges Bizet

            A French composer of the Romantic era. Best known for his operas in a career cut short by his early death, Bizet achieved few successes before his final work, Carmen, which has become one of the most popular and frequently performed works in the entire opera repertoire.
        """
    if opera == "La Traviata":
        ret = """
            Giuseppe Verdi

            An Italian opera composer. He was born near Busseto to a provincial family of moderate means, and developed a musical education with the help of a local patron. Verdi came to dominate the Italian opera scene after the era of Vincenzo Bellini, Gaetano Donizetti, and Gioachino Rossini, whose works significantly influenced him.
        """
    if opera == "Macbeth":
        ret = """
            Giuseppe Verdi

            An Italian opera composer. He was born near Busseto to a provincial family of moderate means, and developed a musical education with the help of a local patron. Verdi came to dominate the Italian opera scene after the era of Vincenzo Bellini, Gaetano Donizetti, and Gioachino Rossini, whose works significantly influenced him.
        """
    if opera == "Parsifal":
        ret = """
            Richard Wagner 

           A German composer, theatre director, polemicist, and conductor who is chiefly known for his operas (or, as some of his mature works were later known, "music dramas"). Unlike most opera composers, Wagner wrote both the libretto and the music for each of his stage works. Initially establishing his reputation as a composer of works in the romantic vein of Carl Maria von Weber and Giacomo Meyerbeer, Wagner revolutionised opera through his concept of the Gesamtkunstwerk ("total work of art"), by which he sought to synthesise the poetic, visual, musical and dramatic arts, with music subsidiary to drama. He described this vision in a series of essays published between 1849 and 1852. Wagner realised these ideas most fully in the first half of the four-opera cycle Der Ring des Nibelungen (The Ring of the Nibelung).
        """
    return ret

def plot(some_day, some_number):
    opera = get_opera(some_day, some_number)
    ret = ""
    if opera == "Carmen":
        ret = """
            Set in Seville around the year 1830, the opera deals with the love and jealousy of Don José, who is lured away from his duty as a soldier and his beloved Micaëla by the gypsy factory-girl Carmen, whom he allows to escape from custody. He is later induced to join the smugglers with whom Carmen is associated, but is driven wild by jealousy. This comes to a head when Carmen makes clear her preference for the bull-fighter Escamillo. The last act, outside the bull-ring in Seville, brings Escamillo to the arena, accompanied by Carmen, there stabbed to death by Don José, who has been awaiting her arrival.
        """
    if opera == "La Traviata":
        ret = """
            La traviata tells the story of the tragic love between the courtesan Violetta and the romantic Alfredo Germont. Played out against the hypocrisy of upper-class fashionable society, Alfredo and Violetta’s love threatens to shame his family. When his father directly appeals to Violetta to relinquish her one chance of happiness, Violetta submits and her act of self-sacrifice leads to her paying the ultimate price.
        """
    if opera == "Macbeth":
        ret = """
            A plot of ruthless politics, Macbeth and Lady Macbeth plot to ensure their place on the throne. Macbeth and Banquo, the leaders of the Scottish army, encounter a group of witches who prophecize that Macbeth will be King, and that Banquo will be the father of kings. Macbeth is perturbed by the prophecy and completely absorbed by his evil thoughts and plots of murder, while his wife is ruthless and stops at nothing to achieve their goals. After they kill the King, Macbeth and his wife are overcome by fear, paranoia, and rage, but they continue to kill everyone in their way to maintain their place on the throne. Ultimately, it becomes their undoing.
        """
    if opera == "Parsifal":
        ret = """
            In Wagner’s retelling of the legend of Percival and the Holy Grail, the naive young Parsifal (the German form of Percival) stumbles across a kingdom he does not understand. After being raised by his mother, away from the world of men, Parsifal knows nothing of right or wrong, nor of sin or redemption. His innocence leads him to an unusual encounter with Gurnemanz, one of the Knights of the Grail.
        """
    return ret

def discounts(some_day, some_number):
    opera = get_opera(some_day, some_number)
    ret = ""
    if opera == "Carmen":
        ret = "Discounts available for students (15%) and the elderly (20%)"
    if opera == "La Traviata":
        ret = "Discounts available for students (20%) and the elderly (20%)"
    if opera == "Macbeth":
        ret = "Discounts available for students (15%) and the elderly (30%)"
    if opera == "Parsifal":
        ret = "No discounts available at this time"
    
    return ret