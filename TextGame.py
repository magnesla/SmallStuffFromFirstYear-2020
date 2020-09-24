print(""" Velkommen til Åpne Døren! Spillet hvor du må prøve å åpne døren. Du kan alltid gå ut av spillet 
      ved å trykke enter i svarsboksen. Håper du liker spillet og lykke til! :D """)
svar1 = input('Du står utenfor en dør med en postkasse. - ').lower()
aapne_postkasse = 0
while svar1 == 'åpne døren' or svar1 == 'åpne postkassen' or svar1 != 'åpne døren' or svar1 != 'åpne postkassen':
    if svar1 == 'åpne døren' and aapne_postkasse == 0:
        print('Døren er låst ')
        svar1 = input('Du står utenfor en dør med en postkasse. - ').lower()
    elif svar1 == 'åpne postkassen' and aapne_postkasse >= 1:
        print('Postkassen er tom. Du har allerede stjålet nøkkelen fra den..')
        svar1 = input('Du står utenfor en dør med en postkasse. - ').lower()
    elif svar1 =='åpne postkassen':
        print ('Du finner en nøkkel')
        aapne_postkasse += 1
        svar1 = input('Du står utenfor en dør med en postkasse. - ').lower()
    elif svar1 == 'gå andre veien':
        print('Du snur deg og vandrer hjem igjen. Du hører en skummel lyd og løper tilbake til døren!')
        svar1 = input('Du står utenfor en dør med en postkasse. - ').lower()
    elif svar1 == '':
        print('Takk for at du så på spillet. Ha en fin dag!')
        break
    elif svar1 == 'åpne døren' and aapne_postkasse >= 1:
        print('Du låser opp døren og går inn.')
        print ('Takk for at du spilte!')
        break
    elif svar1 != 'åpne døren' or svar1 != 'åpne postkassen':
        print('Dette svaret er ikke gylig desverre. Hint: "åpne døren" eller "åpne postkassen"')
        svar1 = input('Du står utenfor en dør med en postkasse. - ').lower()