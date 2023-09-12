import sys
comment_score={}

for line in sys.stdin:
    # comment_id   Sent_Analysis   score
    line = line.strip()
    line_list = line.split('\t')
    comment_id = line_list[0]
    label = line_list[1]
    score = int(line_list[2])
    if label == "POSITIVE":
        comment_score[(comment_id,label)] = comment_score.get((comment_id,label),0)+int(score)
    if label == "NEGATIVE":
        comment_score[(comment_id,label)] = comment_score.get((comment_id,label),0)-score
f = open("sent analysis.txt", "w")
for comment in comment_score:
    print("comment ID: %s is labelled as %s speech with score %d " %(comment[0], comment[1],  comment_score[comment] ))   
    f.write("comment ID: %s is labelled as %s speech with score %d \n" %(comment[0], comment[1],  comment_score[comment] ))   
f.close()