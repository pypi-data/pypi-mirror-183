

def Stability(Dtest, S):
    stability = 0
    count_student = 0
    # This loop is for searching all sequances' length of successive correct predictions for each student
    for i in range(len(S)):  # iterating all students
        student = Dtest.loc[Dtest.idUser == S[i]]  # all information about one student
        length_sequence = 0
        sequences = []
        for j in student.index:  # finding all sequences lengths for one student
            if student.TrueLabel[j] == student.predictedlabel[j]:  # if true label equals predicted label
                length_sequence += 1  # increment sequence's length
            else:  # if not equals
                if length_sequence > 0:
                    sequences.append(length_sequence)  # adding length to list
                length_sequence = 0  # return to start point
        sequences.append(length_sequence)  # adding length to list
        # calculating stability
        stability += max(sequences)  # searching sum of max length's of each student
        count_student += 1  # count number of student
    stability /= count_student  # devise sum by count of student
    return stability


# function for checking if student have been labeled with this class
def First_Labeled(Sp, C):
    t = 0
    for i in Sp.index:
        if Sp.TrueLabel[i] == C:
            t = Sp.weeknumber[i]  # week number when student had first label with C
            break
    return t


# function for finding first correct predicted label
def First_Predicted(Sp, C, ts):
    t = 0
    for i in Sp.index:
        if Sp.weeknumber[i] >= ts:  # week number after starting point
            # if true label is C and equals predicted label
            if Sp.TrueLabel[i] == C and Sp.TrueLabel[i] == Sp.predictedlabel[i]:
                t = Sp.weeknumber[i]  # week number when student had first correct prediction with C
                break
    return t


def Accuracy(Dtest, S):
    accuracy = 0
    count_student = 0
    for i in range(len(S)):  # iterating all students
        student = Dtest.loc[Dtest.idUser == S[i]]  # all information about one student
        count = 0
        count_correct = 0
        for j in student.index:  # finding all correct predictions
            if student.TrueLabel[j] == student.predictedlabel[j]:  # if true label equals predicted label
                count_correct += 1  # counting
            count += 1

        accuracy += count_correct / count
        count_student += 1  # count number of student
    accuracy /= count_student  # devise sum by count of student
    return accuracy


# Algorithm 1. Earliness per student
def Earliness(sp, C, x):
    Ec = {}  # dictionary with C as a key and week numbers as a value
    E = []
    j = 0
    if sp['TrueLabel'].isin([C]).any():
        t0 = First_Labeled(sp, C)  # first week labeled with C
        ts = t0  # denote the starting point in search
        while j < x:
            tj = First_Predicted(sp, C, ts)  # week with first correct prediction
            if tj == 0:
                break
            ej = tj - t0 + 2  # adding week numbers with searched label to ej
            E.append(ej)
            # incrementing variables
            j += 1
            ts = tj + 1
        Ec[C] = E
    return Ec


# Algorithm 2
def Earliness_Total(S, Y, x, Dtest):
    Ey = {}
    for Cj in Y:  # iterating labels
        L = []
        count_L = 0
        for idStudent in S:
            sp = Dtest.loc[Dtest.idUser == idStudent]  # list for each student
            lp = Earliness(sp, Cj, x)  # earliness for this student
            L.append(lp)  # list with earliness for all students
            count_L += 1
        for i in range(x):
            early_Cj = 0
            for l in L:  # searcing sum of week numbers for earliness
                for notes in l.values():
                    early_Cj += sum(notes)
            early_Cj_tot = early_Cj / count_L  # earliness total
            Ey[Cj] = early_Cj_tot
    return Ey


def ESS(stability, Ey):
    ESS1 = []
    average_earliness = 0
    for earliness in Ey.values():
        # for 3 different classes we have 3 different ESS
        ESS1.append((2 * (1 - earliness) * stability) / ((1 - earliness) + stability))
        # we calculate average earliness for searching ESS
        average_earliness += earliness
    ESS2 = (2 * (1 - average_earliness) * stability) / ((1 - average_earliness) + stability)

    return ESS2


def EAS(accuracy, Ey):
    EAS1 = []
    average_earliness = 0
    for earliness in Ey.values():
        # for 3 different classes we have 3 different ESS
        EAS1.append((2 * (1 - earliness) * accuracy) / ((1 - earliness) + accuracy))
        # we calculate average earliness for searching ESS
        average_earliness += earliness
    EAS2 = (2 * (1 - average_earliness) * accuracy) / ((1 - average_earliness) + accuracy)

    return EAS2
