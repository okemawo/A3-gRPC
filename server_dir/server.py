from concurrent import futures
import grpc
import reddit_service_pb2_grpc as reddit_service_grpc
import reddit_service_pb2 as reddit_service
import uuid



class RedditService(reddit_service_grpc.RedditServicer):  # Change this line
    def __init__(self):
            self.posts = {
                "post1": reddit_service.Post(id="post1", title="Post 1", text="This is the first post", author_id="user1", score=10),
                "post2": reddit_service.Post(id="post2", title="Post 2", text="This is the second post", author_id="user2", score=20),
            }
            self.comments = {
                "comment1": reddit_service.Comment(text="This is a comment", author_id="user1", score=5, post_id="post1"),
                "comment2": reddit_service.Comment(text="This is another comment", author_id="user2", score=10, post_id="post1"),
            }
            self.votes = {
                "post1": 10,
                "post2": 20,
                "comment1": 5,  
            }
            self.comment_votes = {}  # Initialize comment_votes
            
    def CreatePost(self, request, context):
        post_id = str(uuid.uuid4())
        post = reddit_service.Post(id=post_id, title=request.post.title, text=request.post.text)
        self.posts[post_id] = post
        self.votes[post_id] = 0  # Initialize vote count for the new post
        return post
    
    def CreateComment(self, request, context):
        comment_id = str(uuid.uuid4())
        comment = reddit_service.Comment(id=comment_id, text=request.comment.text, author_id=request.comment.author_id, post_id=request.comment.post_id)
        self.comments[comment_id] = comment
        self.comment_votes[comment_id] = 0  # Initialize vote count for the new comment
        return comment
    
    def VoteComment(self, request, context):
        # Assuming request contains comment_id
        if request.comment_id not in self.comment_votes:
            self.comment_votes[request.comment_id] = 0
        self.comment_votes[request.comment_id] += 1
        if request.comment_id in self.comments:
            return self.comments[request.comment_id]
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Comment ID not found')
            return reddit_service.Comment()

    def VotePost(self, request, context):
        # Assuming request contains post_id
        self.votes[request.post_id] += 1
        return self.posts[request.post_id]

    def GetPost(self, request, context):
        # Assuming request contains post_id
        return self.posts[request.post_id]

    def GetTopComments(self, request, context):
        # Assuming request contains post_id and count
        top_comments = sorted((comment for comment in self.comments.values() if comment.id), key=lambda comment: self.comment_votes[comment.id], reverse=True)[:request.n]
        return reddit_service.TopCommentsResponse(comments=top_comments)

    def ExpandCommentBranch(self, request, context):
        return reddit_service.ExpandCommentBranchResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_service_grpc.add_RedditServicer_to_server(RedditService(), server)  # And this line
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()