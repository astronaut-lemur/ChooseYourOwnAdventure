##question sets: build up, question, options: next steps

###school day set
wake_up = [['It\'s 6.30 AM. Your alarm is going off.', 'Do you wake up?', 'yes', 'snooze', 'no'], 
            ['go_class', 'go_class_late','drop_out']]

exit_game = [['', 'Do you want to restart?', 'yes', 'no', 'restart'], 
            ['wake_up', 'break', 'wake_up' ]]

go_class = [['You get to school on time!', 'Do you go straight to class or talk with your friends?', 'class', 'talk', 'walk and talk'], 
            ['maths_bored', 'go_class_late', 'gossip_hurt']]

drop_out = [['You didn\'t go to any classes today.', 'Do you drop out or catch up the next day?', 'drop out', 'catch up', 'quit'], 
            ['get_job', 'paper_cut', 'exit_game']]

go_class_late = [['You\'re late!', 'Do you go to your first class or skip and go to your second?', 'go', 'skip', 'leave'], 
            ['detention', 'detention', 'drop_out']]

maths_bored = [['You go to maths. It\'s incredibly boring.', 'Do you do your work?', 'yes', 'no', 'doodle'],
            ['teacher_happy', 'detention', 'discovered_artist']]

get_job = [['Well, time to enter the real world, kid.', 'Do you get a job?', 'no', 'yes', 'go back to school'],
            ['die', 'job_centre', 'wake_up']]

paper_cut = [['You were studying so hard that you got a papercut!', 'What do you do?', 'plaster', 'nothing', 'cry'],
            ['passion_for_medicine', 'cut_infected', 'parent_pity']]

gossip_hurt = [['You\'re friend tells you some gossip about another friend.', 'Who do you tell?', 'everyone', 'nobody', 'friend'],
            ['fight_friend', 'maths_bored', 'cry']]

detention = [['You got put in detention!', 'Do you go to detention or patch it?', 'go', 'patch', 'cry'],
            ['go_detention', 'suspended', 'teacher_pity']]

teacher_happy = [['Your teacher is happy with you and someone calls you a TP.', 'What do you do?', 'fight', 'cry', 'ignore'],
            ['fight_enemy', 'teacher_pity', 'go_home']]

discovered_artist = [['Your teacher sees your doodles and is amazed!', 'What do you do with your art?', 'frame it', 'bin it', 'sell it'],
            ['parent_happy', 'go_home', 'museum']]

die = [['Well, your decision lead to death. Good job.', 'Press \'y\', \'n\' or \'I\'m an idiot for dying and I promise I won\'t do it again\' to restart.', 'y', 'n', 'i'],
            ['exit_game', 'exit_game', 'exit_game']]

passion_for_medicine = [['Wow, you\'re practically a doctor!', 'Do you follow your passion for medicine?', 'yes', 'no', 'what passion'],
            ['medical_school', 'go_home', 'negative_nelly']]

cut_infected = [['Oh no! The cut got infected!', 'What do you do?', 'nothing', 'doctor', 'cry'],
            ['die', 'go_doctor', 'cry']]

parent_pity = [['You\'re parents take pity on you and send you to bed with some hot chocolate and a water bottle.', 'Press \'y\' to wake up tommorow.', 'y', 'n', 'sleep'],
            ['wake_up', 'die', 'wake_up']]

fight_friend = [['You\'re friend is mad at you!', 'What do you do?', 'apologise', 'fight', 'cry'],
            ['go_class_late', 'fight_enemy', 'cry']]

cry = [['You start crying and it feels good to let out your emotions.', 'What do you do now?', 'cry more', 'go home', 'hide'],
            ['cry', 'go_home', 'bin_death']]

suspended = [['You got suspended!', 'When do you tell your parents?', 'asap', 'never', 'cry'],
            ['parents_angry', 'go_home', 'cry']]

teacher_pity = [['Your teacher notices that you\'re upset and wants to talk to your parents.', 'What do you say?', 'no', 'okay', 'go away'],
            ['go_home', 'parent_pity', 'detention']]

dictionary_of_questions = {
    'wake_up': wake_up, 'go_class': go_class,
    'drop_out': drop_out, 'go_class_late': go_class_late,
    'exit_game': exit_game, 'maths_bored': maths_bored,
    'gossip_hurt': gossip_hurt, 'detention': detention,
    'paper_cut': paper_cut, 'get_job': get_job,
    'teacher_happy': teacher_happy, 'discovered_artist': discovered_artist,
    'die': die, 'passion_for_medicine': passion_for_medicine,
    'cut_infected': cut_infected,'parent_pity': parent_pity,
    'fight_friend': fight_friend, 'cry': cry,
    'suspended': suspended, 'teacher_pity': teacher_pity
}

choice = ''


## for asking defining the question set and asking it
def decision_set(build_up, question, action1, action2, action3):
    while True:
        print build_up
        choice = raw_input(question + '\n')
        if (action1 in choice.lower()) or (choice == action1[0]):
            return action1
        elif (action2 in choice.lower()) or (choice == action2[0]):
            return action2
        elif (action3 in choice.lower()) or (choice == action3[0]):
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
    elif exit_ == 'wake_up':
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


game_loop(wake_up, 'The Morning\n\n', 'who needs to debug amiright')
