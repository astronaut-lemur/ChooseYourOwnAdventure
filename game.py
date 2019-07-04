##question sets: build up, question, options: next steps

###school day set
wake_up = [['It\'s 6.30 AM. Your alarm is going off.', 'Do you wake up?', 'yes', 'snooze', 'no'], 
            ['go_class', 'go_class_late','drop_out']]

exit_game = [['', 'Do you want to restart?', 'yes', 'no', 'restart'], 
            ['wake_up', 'break', 'wake_up' ]]



dictionary_of_questions = {
    'wake_up': wake_up, 'exit_game': exit_game
}

choice = ''


## for asking defining the question set and asking it
def decision_set(build_up, question, action1, action2, action3):
    while True:
        print build_up
        choice = raw_input(question + '\n').lower()
        if (action1 in choice.lower()) or (choice == action1[0].lower()):
            return action1
        elif (action2 in choice.lower()) or (choice == action2[0].lower()):
            return action2
        elif (action3 in choice.lower()) or (choice == action3[0].lower()):
            return action3
        else:
            print 'I don\'t know what you want to do. Try ' + str('\'' + action1 + '\'') + ', or ' + str('\'' + action2 + '\'') + ', or ' + str('\'' + action3 + '.\'')

## for getting next step after answer
def ask_and_proceed(step):
    question_set = step[0]
    next_action = step[1]
    action = decision_set(question_set[0], question_set[1], question_set[2], question_set[3], question_set[4])
    if action == question_set[2]: ### if action1 is chosen, return outcome 1
        return next_action[0]
    elif action == question_set[3]:
        return next_action[1]
    elif action == question_set[4]:
        return next_action[2]
    else:
        print 'Huh, you broke the system.'

def exiting_game():
    exit_ = ask_and_proceed(exit_game)
    if exit_ == 'break':
        return 'break'
    elif exit_ == 'wake_up': ##change wakeup for what you want the first question to be
        return 'wake_up'
    else:
        print 'Well idk what you want. Lets restart. Next time try \'yes\' or \'no\'.'
        return 'break'


def game_loop(start_question, setting, debug):
    print str(setting)
    if debug == 'debug':
        choice = ask_and_proceed(start_question)
        print choice
        while True:
            choice = ask_and_proceed(dictionary_of_questions[choice])
            if not (choice in dictionary_of_questions):
                print choice
                print 'Not built this path yet!'
                choice = 'exit_game'
            if choice == 'exit_game':
                if exiting_game() == 'break':
                    print 'Bye!'
                    break
                elif exiting_game() == 'wake_up':
                    choice = 'wake_up'
            print choice
    else:
        choice = ask_and_proceed(start_question)
        while True:
            print '\n'            
            choice = ask_and_proceed(dictionary_of_questions[choice])
            if not (choice in dictionary_of_questions):
                print 'Not built this path yet!'
                choice = 'exit_game'
            if choice == 'exit_game':
                if exiting_game() == 'break':
                    print 'Bye!'
                    break
                elif exiting_game() == 'wake_up':
                    choice = 'wake_up'


game_loop(wake_up, 'The Morning\n\n', '')
