import grpc
import reddit_service_pb2_grpc as reddit_service_grpc
import reddit_service_pb2 as reddit_service

    
class RedditClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = reddit_service_grpc.RedditStub(self.channel)

    def create_post(self, title, text):
        post = reddit_service.Post(title=title, text=text)
        response = self.stub.CreatePost(reddit_service.CreatePostRequest(post=post))
        return response

    def vote_post(self, post_id):
        response = self.stub.VotePost(reddit_service.VotePostRequest(post_id=post_id))
        return response

    def get_post(self, post_id):
        response = self.stub.GetPost(reddit_service.GetPostRequest(post_id=post_id))
        return response

    def create_comment(self, text, author_id, post_id):
        comment = reddit_service.Comment(text=text, author_id=author_id, post_id=post_id)
        response = self.stub.CreateComment(reddit_service.CreateCommentRequest(comment=comment))
        return response

    def vote_comment(self, comment_id):
        response = self.stub.VoteComment(reddit_service.VoteCommentRequest(comment_id=comment_id))
        return response

    def get_top_comments(self, post_id, count):
        response = self.stub.GetTopComments(reddit_service.GetTopCommentsRequest(post_id=post_id, n=count))
        return response

    def expand_comment_branch(self, comment_id, count):
        response = self.stub.ExpandCommentBranch(reddit_service.ExpandCommentBranchRequest(comment_id=comment_id, n=count))
        return list(response.comments)
       
    def get_most_upvoted_reply(self, post_id):
        # Retrieve a post
        post = self.get_post(post_id)
        if not post:
            return None

        # Retrieve most upvoted comments under the post
        top_comments = self.get_top_comments(post_id, 1)
        if not top_comments.comments:
            return None

        # Expand the most upvoted comment
        most_upvoted_comment = top_comments.comments[0]
        replies = self.expand_comment_branch(most_upvoted_comment.id, 1)
        if not replies.comments:
            return None

        # Return the most upvoted reply under the most upvoted comment
        most_upvoted_reply = max(replies.comments, key=lambda reply: reply.votes)
        return most_upvoted_reply

    def get_most_upvoted_comment(self, post_id):
        response = self.stub.GetTopComments(reddit_service.GetTopCommentsRequest(post_id=post_id, n=1))
        if response.comments:
            return response.comments[0]
        else:
            return None


if __name__ == '__main__':
    client = RedditClient()

    # Create a post
    post_response = client.create_post('Test Title', 'Test Text')
    print(f"Created post ID: {post_response.id}")

    # Vote the post
    vote_post_response = client.vote_post(post_response.id)
    print(f"Voted post response: {vote_post_response}")

    # Get the post
    get_post_response = client.get_post(post_response.id)
    print(f"Got post response: {get_post_response}")

    # Create a comment
    comment_response = client.create_comment('Test Comment', 'Test Author', post_response.id)
    print(f"Created comment ID: {comment_response.id}")  # Change this line

    # Vote the comment
    vote_comment_response = client.vote_comment(comment_response.id)  # Change this line
    print(f"Voted comment response: {vote_comment_response}")
    
    # Get top comments
    top_comments_response = client.get_top_comments(post_response.id, 5)  # Change this line
    print(f"Got top comments response: {top_comments_response}")

    # Expand comment branch
    expand_comment_branch_response = client.expand_comment_branch(comment_response.post_id, 5)
    print(f"Expanded comment branch response: {expand_comment_branch_response}")
    
    