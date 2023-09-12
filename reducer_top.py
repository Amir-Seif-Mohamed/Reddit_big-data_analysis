#reducer to filter the most used 
import sys
Id_topic = {}
user_topic = {}
for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    #"subreddit_id"	 "text"	 "redditor"	 main_id	 sub_main_id	 ups	 down   controversiality
    subreddit_id = line[0]
    text = line[1]
    redditor = line[2]
    #add the word to the dict and count the occurance of it according to the """subreddit""" 
    Id_topic[(subreddit_id,text)] = Id_topic.get((subreddit_id,text), 0)+1
    #add the word to the dict and count the occurance of it according to the """subreddit""" 
    user_topic[(redditor,text)] = Id_topic.get((redditor,text), 0)+1
f = open("Most used topic.txt", "w")
for comment in Id_topic:
    print("Most used topic in %s is %s with count of %d"%(comment[0],comment[1],Id_topic[comment]))
    f.write("Most used topic in %s is %s with count of %d \n"%(comment[0],comment[1],Id_topic[comment]))
f.close()

