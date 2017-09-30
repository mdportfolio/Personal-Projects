# Beginning of quiz
print ("Hello! Welcome to Fill-In Quiz!")
level_picker = raw_input("What level do you want to play? [Easy, Medium, Hard]")

# Checks if a word in answers is a substring of the word passed in. If the word is not in there the player will have to try again.
def res_in_ans(response, answers):
	for response in answers:
		if response in answers:return response 
		else:
			print ("Try Again.")
			print (question[qi])
			attempt = 1
			tries = 3
			while (attempt <= tries):
				print ("Try Again.")
				print (question[qi])
				tries = tries - 1
				print ("Game Over: You LOSE!")             

 # A player gets a question and fills in the blank with an answer and prints it if the user gets it correct. 
def play_games(question, answers):
    new_ans = []
    for word in question:
    	replace = res_in_ans(word, answers)
    	if replace != None:
    		word = word.replace(replace, response)
    		new_ans.append(word)
    	else:
    		new_ans.append(word)
    		new = " ".join(new_ans)
    		return "Correct" + new
    	print (question[qi+1])    

# Level Selection
if level_picker == "easy":
	fillins = ["A1", "A2", "A3", "A4"]
	answers = ["Intro to Programming","python","Dave","programming"]
	question = ["You are in the A1 nanodegree program.","You learn so many things in A2.","A3 taught us so much about data structures.","Welcome to the wonderful world of A4."]
	response = raw_input()
	qi = 0
	print (question[qi])
	play_games(question, answers)   

if level_picker == "medium":
    fillins = ["A1", "A2", "A3", "A4", "A5"]
    answers = ["don't panic", "input and output", "plan out", "code", "test"]
    question = ["The first step is to A1","Secondly, you figure out the A2 of the problem.","In the third step, A3 your solution.", "Then you A4 your solution.","Lastly, don't forget to A5 your solution."]
    response = raw_input()
    qi = 0
    print (question[qi])
    play_games(question, answers)

if level_picker == "hard":
    fillins = ["A1", "A2", "A3", "A4"]
    answers = ["assignment", 30, "muttable", "Ada"]
    question = ["The difference between == and = is that = is an A1.","There are over A2 data structures generally.","In Python, lists are A3, which means you can change it.","The founding mother of programming is A4 Lovelace."]
    response = raw_input()
    qi = 0
    print (question[qi])
    play_games(question, answers)

# End of Game
print ("You have finished the game! Good Job! You're Smart!")