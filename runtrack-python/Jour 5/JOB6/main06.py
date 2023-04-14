def arrondir_notes(notes):
   
    notes_arrondies = []
    for note in notes:
        if note >= 40:
            if note % 5 >= 3:
                note_arrondie = note + 5 - note % 5
                if note_arrondie > 100:
                    note_arrondie = 100
            else:
                note_arrondie = note
        else:
            note_arrondie = note
        notes_arrondies.append(note_arrondie)
    return notes_arrondies

notes= [23,81,39,44,94]
notes_arrondies=arrondir_notes(notes)
print(notes_arrondies)