##question sets: build up, question, options: next steps

###school day set
wake_up = [['It\'s 6.30 AM. Your alarm is going off.', 'Do you wake up?', 'yes', 'snooze', 'no'], 
            ['go_class', 'go_class_late','drop_out']] #ooo

exit_game = [['', 'Do you want to restart?', 'yes', 'no', 'restart'], 
            ['wake_up', 'break', 'wake_up' ]] #ooo

go_class = [['You get to school on time!', 'Do you go straight to class or talk with your friends?', 'class', 'talk', 'walk and talk'], 
            ['maths_bored', 'go_class_late', 'gossip_hurt']] #ooo

drop_out = [['You didn\'t go to any classes today.', 'Do you drop out or catch up the next day?', 'drop out', 'catch up', 'quit'], 
            ['get_job', 'paper_cut', 'exit_game']] #ooo

go_class_late = [['You\'re late!', 'Do you go to your first class or skip and go to your second?', 'go', 'skip', 'leave'], 
            ['detention', 'detention', 'drop_out']] #ooo

maths_bored = [['You go to maths. It\'s incredibly boring.', 'Do you do your work?', 'yes', 'no', 'doodle'],
            ['teacher_happy', 'detention', 'discovered_artist']] #ooo

get_job = [['Well, time to enter the real world, kid.', 'Do you get a job?', 'no', 'yes', 'go back to school'],
            ['die', 'job_centre', 'wake_up']] #ooo

paper_cut = [['You were studying so hard that you got a papercut!', 'What do you do?', 'plaster', 'nothing', 'cry'],
            ['passion_for_medicine', 'cut_infected', 'parent_pity']] #ooo

gossip_hurt = [['You\'re friend tells you some gossip about another friend.', 'Who do you tell?', 'everyone', 'nobody', 'friend'],
            ['fight_friend', 'maths_bored', 'cry']] #ooo

detention = [['You got put in detention!', 'Do you go to detention or patch it?', 'go', 'patch', 'cry'],
            ['go_detention', 'suspended', 'teacher_pity']] #ooo

teacher_happy = [['Your teacher is happy with you and someone calls you a TP.', 'What do you do?', 'fight', 'cry', 'ignore'],
            ['fight_enemy', 'teacher_pity', 'go_home']] #ooo

discovered_artist = [['Your teacher sees your doodles and is amazed!', 'What do you do with your art?', 'frame it', 'bin it', 'sell it'],
            ['parent_happy', 'go_home', 'museum']] #ooo

die = [['Well, your decision lead to death. Good job.', 'Press \'y\', \'n\' or \'I\'m an idiot for dying and I promise I won\'t do it again\' to restart.', 'y', 'n', 'i'],
            ['exit_game', 'exit_game', 'exit_game']] #ooo

passion_for_medicine = [['Wow, you\'re practically a doctor!', 'Do you follow your passion for medicine?', 'yes', 'no', 'what passion'],
            ['medical_school', 'go_home', 'negative_nelly']] #ooo

cut_infected = [['Oh no! The cut got infected!', 'What do you do?', 'nothing', 'doctor', 'cry'],
            ['die', 'go_doctor', 'cry']] #ooo

parent_pity = [['You\'re parents take pity on you and send you to bed with some hot chocolate and a water bottle.', 'Press \'y\' to wake up tommorow.', 'y', 'n', 'sleep'],
            ['wake_up', 'die', 'wake_up']] #ooo

fight_friend = [['Your friend is mad at you!', 'What do you do?', 'apologise', 'fight', 'cry'],
            ['go_class_late', 'fight_enemy', 'cry']] #ooo

cry = [['You cry and it feels good to let out your emotions.', 'What do you do now?', 'cry', 'go home', 'hide'],
            ['cry', 'go_home', 'bin_death']] #ooo

suspended = [['You got suspended!', 'When do you tell your parents?', 'asap', 'never', 'cry'],
            ['parents_angry', 'go_home', 'cry']] #ooo

teacher_pity = [['Your teacher notices that you\'re upset and wants to talk to your parents.', 'What do you say?', 'no', 'okay', 'go away'],
            ['go_home', 'parent_pity', 'detention']] #ooo

job_centre = [['You go to the job centre! They\'re advertising for waiters, astronauts and gladiators.', 'Which job do you choose?', 'waiter', 'astronaut', 'gladiator'],
            ['waiter', 'astronaut', 'die']] #ooo

go_detention = [['You go to detention.', 'Do you cause trouble?', 'yes', 'no', 'sleep'],
            ['suspended', 'go_home', 'detention']] #ooo

fight_enemy = [['Oh no, you\'ve gotten into a fight!', 'What do you do?', 'punch', 'bite', 'cry'],
            ['detention', 'suspended', 'cry']] #ooo

go_home = [['You go home after a long, hard day.', 'To wake up tomorrow, press \'y\'.', 'yes', 'no', 'rebel'],
            ['wake_up', 'exit_game', 'die']] #ooo

parent_happy = [['Your parents are very pleased with you. You go to bed content that you\'ve made them proud.', 'To wake up tomorrow, press \'y\'.', 'yes', 'no', 'rebel'],
            ['wake_up', 'exit_game', 'die']] #ooo

museum = [['Wow, somebody bought your art and it\'s on display in the museum!', 'Do you tell your parents?', 'yes', 'no', 'move out, cause your self sufficient now'],
            ['parent_happy', 'go_home', 'die']] #ooo

bin_death = [['You hid in a bin. How smart of you.', 'Press something. I don\'t care anymore.', 'yes', 'no', 'haha, bet you thought you could press anything there'],
            ['die', 'die', 'die']] #ooo

medical_school = [['Fast forward a few years and you\'ve completed medical school! Good job!', 'Press \'enter\'.', '...', 'enter', 'I\'m a rebel I do what I want'],
            ['exit_game', 'exit_game', 'die']]

negative_nelly = [['You\'re a negative nelly.', 'To become a positive polly, hit \'enter\'.', '...', 'enter', 'I\'m not a negative nelly!'],
            ['wake_up', 'wake_up', 'exit_game']]

go_doctor = [['You go to the Doctors\'.', 'Does it inspire you to persue medicine?', 'yes', 'no', 'why would it'],
            ['medical_school', 'go_home', 'negative_nelly']]

parents_angry = [['Oops, you\'re parents are mad at you.', 'How do you react?', 'cry', 'leave', 'sleep'],
            ['cry', 'job_centre', 'wake_up']]

waiter = [['You become a waiter! You lead a happy life and never go back to school again.', 'After retiring as head chef of a 4 star restaurant you press \'enter\'.', '...', 'enter', 'actually it was five star'],
            ['exit_game', 'exit_game', 'negative_nelly']]

astronaut = [['You become the youngest astronaut in space, and the first to walk on Mars. Wow!', 'As you\'re watching the sunset on pluto, you decide to press \'enter\'.', '...', 'enter', 'pluto isn\'t a real planet'],
            ['exit_game', 'exit_game', 'negative_nelly']]

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
    'suspended': suspended, 'teacher_pity': teacher_pity,
    'job_centre': job_centre, 'go_detention': go_detention,
    'fight_enemy': fight_enemy, 'go_home': go_home,
    'parent_happy': parent_happy, 'museum': museum,
    'bin_death': bin_death, 'medical_school': medical_school,
    'negative_nelly': negative_nelly, 'go_doctor': go_doctor,
    'parents_angry': parents_angry, 'waiter': waiter,
    'astronaut': astronaut, 'empty': 'empty'
}

choice = ''


## for asking defining the question set and asking it
def decision_set(build_up, question, action1, action2, action3):
    while True:
        print build_up
        choice = raw_input(question + '\n')
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


game_loop(wake_up, 'The Morning\n\n', 'who debugs things anymore')
