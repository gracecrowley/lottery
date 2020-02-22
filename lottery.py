def lottery_winners(participants, x):
    participant_names = ''
    winners = ''
    new_d = []
    for name in participants:
        for num in participants[name]:
            if num == x:
                new_d.append(name)
                winners += name + ' '
    print(f'The winners are: {winners}')

    amnt_participants = len(participants)
    amnt_of_winners = len(new_d)

    total = amnt_participants * 5
    win = total / amnt_of_winners

    print(f'They win {win} euro each')



D = {"Donald": [23, 21, 20, 34, 15, 23], "Boris": [17, 16, 3, 7, 26, 42], "Theresa": [13, 90, 47, 17, 1, 11]}

lottery_winners(D, 17)
