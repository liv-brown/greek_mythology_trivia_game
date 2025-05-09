#This is a Greek Mythology themed trivia game that will quiz players on various figures and events in Greek mythology. 
import random 
#Define a list of Greek mythology themed trivia questions and provide their answers.
def greek_mythology_trivia():
    """ Play a Greek mythology trivia game. """
    questions = {
        "Who is the Greek god of the sea, earthquakes, and horses?": "Poseidon",
        "Who is the Greek goddess of wisdom, warfare strategy, and craftsmanship?": "Athena",
        "Who is the Greek goddess of the hunt, wilderness, and the moon?": "Artemis",
        "Who is the Greek god of music, poetry, prophecy, and the sun?": "Apollo",
        "Who is the Greek hero that went on a 20 year journey to get back to his kingdom in Ithaca?": "Odysseus",
        "What war did Achilles fight in?": "Trojan War",
        "Who is the centaur famous for training Greek heroes?": "Chiron",
        "Which three-headed creature guards the entrance to the Underworld?": "Cerberus",
        "Which Greek figure flew too close to the sun, causing his wax wings to melt?": "Icarus",
        "Which Greek mythology figure was cursed to hold up the sky?": "Atlas"
    }

    #Initialize the player's score
    score = 0
    num_questions = len(questions)

    #Display a welcome message to the player
    print("Welcome to the Greek Mythology Trivia Game!")

    #Iterate through the trivia questions 
    for question, answer in questions.items():
        #Display the current trivia question
        print("\nQuestion:", question)
        #Get the player's answer input
        player_answer = input("Your answer: ")
        #Check if the player's answer is correct
        if player_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.")
        #Display the player's current score after each question 
        print(f"Your score: {score}")

    #Display an end of game message and provide the player's final score.
    print("\nGame Over!")
    print(f"Your final score is: {score}/{num_questions}")

if __name__ == "__main__":
    greek_mythology_trivia()