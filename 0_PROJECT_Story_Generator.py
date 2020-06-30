#Project Python Story Generator. Ask users to provide inputs, based on which a story will be created.
def story_generator ():
    print "It's story time. Let's create one together!\n"

    story_dict = {
        'mystery': 'On a dark stormy night in place, the adjective noun thief was on the loose. Everyone is anxious and cannot fall asleep.',
        'modern fairytale': 'Once upon a time in place, the prince was kidnapped. The royal army has been looking for him in vain. His sister cannot sit still so she enlists his adjective squirrel and favorite noun to escape the castle at midnight and go find him.'
    }

    story_type = raw_input ("Would you like 'modern fairytale' or 'mystery'? ").lower()

    while story_type != "modern fairytale" and story_type != "mystery":
        story_type = raw_input ("Sorry, I don't understand, please choose 'modern fairytale' or 'mystery': ").lower()


    place = raw_input ("Where do you want the story to happen? ")
    adjective = raw_input ("Give me an adjective: ").lower ()
    noun = raw_input ("Give me a noun: ").lower()

    print "\nHere is your story:"
    if story_type == "modern fairytale":
        print story_dict ["modern fairytale"] .replace("place", place) .replace ("adjective", adjective) .replace ("noun", noun)
    if story_type == "mystery":
        print story_dict ["mystery"] .replace("place", place) .replace ("adjective", adjective) .replace ("noun", noun)

story_generator ()



# String Replace method https://www.w3schools.com/python/ref_string_replace.asp
