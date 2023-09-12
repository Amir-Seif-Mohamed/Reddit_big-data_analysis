import sys
num_of_replies ={}
controversial = {}
for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    #"subreddit_id"	 "text"	 "redditor"	 main_id	 sub_main_id	 ups	 down   controversiality
    comment_id = line[3]
    reply_id = line[4]
    controversiality = int(line[7])
    #count number of relpies per the comment and then check later its controversiality
    if comment_id != reply_id:
        num_of_replies[comment_id] = num_of_replies.get(comment_id,0)+1
        controversial[comment_id] = controversial.get(comment_id,0)+controversiality
f = open("rate of replies.txt", "w")
for comment in num_of_replies:
    print("Comment Id: %s has number of replies: %s and number of controversiality: %d " %(comment,num_of_replies[comment],controversial[comment]))
    f.write("Comment Id: %s has number of replies: %s and number of controversiality: %d \n " %(comment,num_of_replies[comment],controversial[comment]))

f.close()        


