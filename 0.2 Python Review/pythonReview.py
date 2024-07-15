def create_youtube_videos(title,description, hashtag):
	youtube_video = {}
	youtube_video["title"] = title
	youtube_video["description"] = description
	youtube_video["likes"] = 0
	youtube_video["dislikes"] = 0
	youtube_video["comments"] = {}
	youtube_video["hashtag"] = []
	if youtube_video["hashtag"].len() > 5:
		return "error"
	return youtube_video




def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video

def add_comment(youtube_video, username, comment_text ) :
	youtube_video["comments"][username] = comment_text
	return youtube_video


new_youtube_video = create_youtube_videos("QAIS", "NICE VIDEO ")
like(new_youtube_video)
dislike(new_youtube_video)
add_comment(new_youtube_video, "ABU ELI", "NOT GOOD VIDEO ")
print("Title : " + new_youtube_video["title"])
print("Description : " + new_youtube_video["description"])
print(str(new_youtube_video["likes"]) + " people liked that !")
print(str(new_youtube_video["dislikes"])	 + " people disliked that !")
print(new_youtube_video["comments"])
