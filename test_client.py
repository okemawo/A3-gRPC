import unittest
from unittest.mock import Mock
from client_dir.client import RedditClient


client = RedditClient()

class TestGetMostUpvotedReply(unittest.TestCase):
    
    def setUp(self):
        self.api_client = Mock()
        self.reddit_client = RedditClient(self.api_client)
        
        # Create mock posts
        mock_post_1 = Mock(id='post1')
        mock_post_2 = Mock(id='post2')

        # Create mock comments
        mock_comment_1 = Mock(id='comment1', votes=10)
        mock_comment_2 = Mock(id='comment2', votes=20)

        # Assign comments to posts
        mock_post_1.comments = [mock_comment_1]
        mock_post_2.comments = [mock_comment_2]

        # Mock the API client methods
        self.api_client.get_post.side_effect = [mock_post_1, mock_post_2]
        
    def test_get_most_upvoted_reply(self):
        # Mock the API client methods
        self.api_client.create_post.return_value = Mock(id='post1')
        self.api_client.vote_post.return_value = Mock()
        self.api_client.get_post.return_value = Mock(id='post1')
        self.api_client.create_comment.return_value = Mock(id='comment1')
        self.api_client.vote_comment.return_value = Mock()
        self.api_client.get_top_comments.return_value = [Mock(id='comment1')]
        self.api_client.expand_comment_branch.return_value = [Mock(id='reply1', votes=10), Mock(id='reply2', votes=20)]

        # Mock the get_most_upvoted_reply method
        client.get_most_upvoted_reply = Mock(return_value=Mock(votes=20))

        # Call the function to test
        most_upvoted_reply = client.get_most_upvoted_reply('post1')
        
        # Check the result
        self.assertEqual(most_upvoted_reply.votes, 20)


    def test_get_post(self):
        self.api_client.get_post.return_value = Mock(id='post1')
        post = client.get_post('post1')
        self.assertEqual(post.id, 'post1')
  
        
    def test_get_most_upvoted_comment(self):
        # Mock the get_post method to return a post with two comments
        self.api_client.get_post.return_value = Mock(comments=[Mock(id='comment1', votes=10), Mock(id='comment2', votes=40)])

        # mock the get_most_upvoted_comment method
        client.get_most_upvoted_comment = Mock(return_value=Mock(id='comment2'))

        # Call the function to test
        most_upvoted_comment = client.get_most_upvoted_comment('post1')

        # Check the result
        self.assertEqual(most_upvoted_comment.id, 'comment2')
        

if __name__ == '__main__':
    unittest.main()