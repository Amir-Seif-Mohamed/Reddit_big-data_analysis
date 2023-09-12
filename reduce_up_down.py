import sys
comment_ups = {}
comment_downs = {}
for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    #"subreddit_id"	 "text"	 "redditor"	 main_id	 sub_main_id	 ups	 down   controversiality
    comment_id = line[3]
    ups = int(line[5])
    downs = int(line[6])
    #count no. of votes per comment
    comment_ups[(comment_id)] = comment_ups.get(comment_id,0)+ups
    comment_downs[(comment_id)] = comment_downs.get(comment_id,0)+downs

f = open("Votes.txt", "w")
for comment in comment_ups:
    print("comment with ID: %s has total votes: %d "%(comment, comment_ups[comment]))
    f.write("comment with ID: %s has total votes: %d\n "%(comment, comment_ups[comment]))
f.close()