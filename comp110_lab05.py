"""
Module: comp110_lab05

Exercises from lab 05, dealing with strings and file reading.
"""

def max_wind_speed(hurricane_filename):
    """
    Finds the maximum wind speed for the hurricane.

    Parameters:
    1. hurricane_filename (type: string) - Name of the file containing the data

    Returns:
    (type: int) The maximum wind speed of the hurricane.
    """

   
    f = open(hurricane_filename, 'r')
    biggest = 0
    for line in f:
        vals = line.split(',')
        size = int(vals[4])
        if size > biggest:
            biggest = size
      
    return biggest

def contains_word(word, review):
    

    """
    Determines whether the review contains the given word. 

    Note that should ignore the "casing" of letters. For example "ok" is
    considered to be contained in the review "It was an OK movie."

    Parameters:
    1. word (type: string): The word to search for.
    2. review (type: string): The review in which to search.

    Returns:
    (type: boolean) True if word is contained in the review, and false
    otherwise.
    """
    my_str = review
    lowered_str = my_str.lower()
    if word in lowered_str:
        return True
    else:
        return False
    


def test_max_wind_speed():
    max_wind = max_wind_speed("florence.csv") 
    if max_wind == 140:
        print("max_wind_speed(florence.csv) PASSED")
    else:
        print("max_wind_speed(florence.csv) FAILED")

    max_wind = max_wind_speed("irma.csv") 
    if max_wind == 185:
        print("max_wind_speed(irma.csv) PASSED")
    else:
        print("max_wind_speed(irma.csv) FAILED")
    
    max_wind = max_wind_speed("dorian.csv") 
    if max_wind == 185:
        print("max_wind_speed(dorian.csv) PASSED")
    else:
        print("max_wind_speed(dorian.csv) FAILED")
        
    

    """ Function that tests the max_wind_speed function. """
    
    print("Starting test of max_wind_speed")

    # To Do: Call your max_wind_speed function on the irma.csv file, using an if
    # statement to indicate whether the result was correct or not.
    # Then repeat the process for the florence.csv and dorian.csv files to check
    # whether your function works for those files.

    print("FAILED: Not implemented yet.") # remove this line when you finish the to do

    print("Done testing max_wind_speed")


def test_contains_word():
    """ Function that tests the contains_word function. """

    print("\nStarting test of contains word")

    if contains_word('ok', 'ok') != True:
        print("FAILED: contains_word('ok', 'ok')")
    elif contains_word('ok', 'OK') != True:
        print("FAILED: contains_word('ok', 'OK')")
    elif contains_word('ok', 'bad') != False:
        print("FAILED: contains_word('ok', 'bad')")
    elif contains_word('ok', 'not ok') != True:
        print("FAILED: contains_word('ok', 'not ok')")
    # To Do: update the chained conditional to test all of your new test cases.
    else:
        print("All contains_word test cases passed!")


    print("Done testing contains word")


def main():
    test_max_wind_speed()
    test_contains_word()

# Do not modify anything after this point.
if __name__ == "__main__":
    main()
