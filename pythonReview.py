def create_youtube_video(title, description, hashtag):
	return({"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}, "hashtag": hashtag})

def like(youtubevideo):
	if("likes" in youtubevideo):
		youtubevideo["likes"]+=1;
	return(youtubevideo)

def dislike(youtubevideo):
	if("dislikes" in youtubevideo):
		youtubevideo["dislikes"]+=1;
	return(youtubevideo)

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username] = comment_text;
	return(youtubevideo)

def similarity_to_video(video1, video2):
	if(len(video1["hashtag"]) == 0):
		return(0);
	sim = 0;
	for i in video1["hashtag"]:
		if(i in video2["hashtag"]):
			sim += 1;
	return(sim/len(video1["hashtag"])*100)