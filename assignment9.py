
# Author: Jacob Christiansen
# Recitation: 104 - Vipra Gupta
#
# Assignment 9
# compute_census's goal is to find the US population in one year from now. We are provided with a few bits of data.
# birth rate, death rate, immigrant rate, and current US population
# My function takes these values in as a list, as well as defines how many seconds are in a year. Using this data,
# it calculates how many babies are born, people are killed, and immigrants have migrated into the US in a year.
# Then it simply adds the births, immigrants, and current population, then subtracts the deaths, to find the
# new population in a year.
def compute_census(list_of_rates, current_population):
    birthR = list_of_rates[0]
    deathR = list_of_rates[1]
    immR = list_of_rates[2]
    yearSecs = 31536000

    birthYr = yearSecs / birthR
    deathYr = yearSecs / deathR
    immYr = yearSecs / immR
    newPop = (birthYr+immYr+current_population)-deathYr
    return newPop

# The point of this function is to covert seconds into a day/hour/min/
# sec format. It does so with the following steps:
# -finds days, sets it to variable.
# -finds remainder of days, then converts to hours, sets it to variable.
# -finds remainder of hours, then converts to mins, sets it to variable.
# -finds remainder of mins, then converts to secs, sets it to variable.
# -outputs the variables along with a string of text to make it understandable.
def convert_seconds():
    givenSec = int(raw_input())
    daySec=0
    hourSec=0
    minSec=0
    secSec=0
    daySec = givenSec / 86400
    hourSec = (givenSec % 86400) / 3600
    minSec = ((givenSec % 86400) % 3600) / 60
    secSec = (((givenSec % 86400) % 3600) % 60)

    print str(givenSec)+" corresponds to: "+str(daySec)+" days, "+str(hourSec)+" hours, "+str(minSec)+" minutes, "+str(secSec)+" seconds."
    return

# this function takes in a list that determines how a story will be told in the following format:
# -text, user imput, text, user imput, etc (all of this based on the list of strings given)
#so every even index of the list will add that string to the final string
# and every odd index of the list will prompt a user and that to the final string
def generate_story(list_to_story):
    final = ""
    for i in range(0, len(list_to_story)):
        if(i%2==0):
            final = final+list_to_story[i]+" "
        else:
            strIn = str(raw_input(list_to_story[i]))
            final = final + strIn + " "
    final = final.rstrip()
    return final

# In this function, it is comparing two strings, and if they are equal in length, then
# they compare how similar they are to each other, based on matching 1-length strings.
# It then calculates the similarity score using the string lengths and the matching values.
# Then it returns the score.
def similarity_score(seq1, seq2):
    l1 = len(seq1)
    l2 = len(seq2)
    hamm = 0.0
    score = 0.0

    if(l1 == l2):
        for i in range(0, l1):
            test1 = seq1[i]
            test2 = seq2[i]
            if(test1 != test2):
                hamm = hamm + 1
            score = (float(l1) - hamm)/float(l1)
    else:
        score = 0;
    return score;

#This function is comparing all the similarityScores of each position inside the genome, that is length of the given sequence,
# and finding the one which is highest, and returning
# the index(count variable) of that score.
def best_match(geno, seq):
    hiScore = 0.0
    count = 0
    for i in range(0, len(geno)):
        subGeno = geno[i:i+len(seq)]
        newScore = similarity_score(subGeno, seq)
        if(hiScore < newScore):
            hiScore = newScore
            count = i
    return count;

# This function simply finds the average of all the nums in a list (all the nums summed and diveded by length of list)
#and then the median of the list (middle value in list (len/2) and if its an odd list, the answer is the difference between the middle two values summed,
#subtracted from the higher middle val)
def calc_stats(num_list):
    sum = 0.0
    count = 0.0

    for i in range(len(num_list)):
        for j in range(len(num_list)-1):
            temp1 = num_list[j]
            temp2 = num_list[j+1]
            if(temp1 > temp2):
                num_list[j] = temp2
                num_list[j+1] = temp1

    for i in range(len(num_list)):
        sum += num_list[i]
        count = count + 1

    if(sum == 0):
        avg = 0.0
    else:
        avg = sum/count

    if(len(num_list)%2 != 0):

        med = float(num_list[len(num_list)/2])
    else:
        pos2 = int(len(num_list)/2)
        pos1 = pos2-1
        val1 = num_list[pos1]
        val2 = num_list[pos2]
        med = val1+(float(val2-val1)/2.0)

    return [avg, med]

#parse_ratings reads in a file line by line, and then it splits each line in two parts (by comma), a Name, and then a string of values.
#then it takes the values and splits them into a list (by spaces)
#and each of those lines is also a new position in a large array.
#so the output will look like [ [line1,[#,#,#]], [line2,[#,#,#], [line3,[#,#,#]] ]
def parse_ratings(file_name):
    listCommaSplit = []
    fr = open(file_name)
    for line in fr:
        listCommaSplit.append(line.split(','))
    fr.close
    for i in range(len(listCommaSplit)):
        if(i < len(listCommaSplit)-1):
            listCommaSplit[i][1] = listCommaSplit[i][1][:-1]
        listCommaSplit[i][1] = listCommaSplit[i][1][1:]
        temp = listCommaSplit[i][1]
        listSpaceSplit = []
        listSpaceSplit.append(temp.split(' '))
        listCommaSplit[i][1] = listSpaceSplit[0]
        for j in range(len(listCommaSplit[i][1])):
            listCommaSplit[i][1][j] = int(listCommaSplit[i][1][j])
    return listCommaSplit

#this main tests all the fuctions
def main():

    listtest = [8, 12, 33]
    newPop = compute_census(listtest, 1000000)
    print newPop

    convert_seconds()

    str1 = "I went skiing to"
    prompt1 = "Enter a location: "
    str2 = "it was really crowded and I stayed in line for"
    prompt2 = "Enter number of hours: "
    str3 = "hours"
    list_to_story = [str1, prompt1, str2, prompt2, str3]
    print generate_story(list_to_story)

    seq1 = "CCGCCGCCGA"
    seq2 = "CCTCCTCCTA"
    print similarity_score(seq1, seq2)

    geno = "CTA"
    print best_match(seq2, geno)

    listn = [1,2.5,3,8,10.5,5]
    print calc_stats(listn)
    print parse_ratings("C:/Users/jacob/Dropbox/1300ProgramsCSCI/Ass9/test.txt")

# this makes main work because it just does
if __name__ == '__main__':
    main()
