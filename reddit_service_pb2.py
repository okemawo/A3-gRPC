# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14reddit_service.proto\"\x12\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\"\xe7\x01\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x11\n\tvideo_url\x18\x04 \x01(\t\x12\x11\n\timage_url\x18\x05 \x01(\t\x12\x11\n\tauthor_id\x18\x06 \x01(\t\x12\r\n\x05score\x18\x07 \x01(\x05\x12\x1a\n\x05state\x18\x08 \x01(\x0e\x32\x0b.Post.State\x12\x18\n\x10publication_date\x18\t \x01(\x03\"8\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\n\n\x06LOCKED\x10\x02\x12\n\n\x06HIDDEN\x10\x03\"\xd8\x01\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\tauthor_id\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x05\x12\x1d\n\x05state\x18\x05 \x01(\x0e\x32\x0e.Comment.State\x12\x18\n\x10publication_date\x18\x06 \x01(\x03\x12\x0f\n\x07post_id\x18\x07 \x01(\t\x12\x19\n\x11parent_comment_id\x18\x08 \x01(\t\",\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\n\n\x06HIDDEN\x10\x02\"(\n\x11\x43reatePostRequest\x12\x13\n\x04post\x18\x01 \x01(\x0b\x32\x05.Post\"2\n\x0fVotePostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\x0e\n\x06upvote\x18\x02 \x01(\x08\"!\n\x0eGetPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\"1\n\x14\x43reateCommentRequest\x12\x19\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x08.Comment\"8\n\x12VoteCommentRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\x0e\n\x06upvote\x18\x02 \x01(\x08\"3\n\x15GetTopCommentsRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\x05\"1\n\x13TopCommentsResponse\x12\x1a\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x08.Comment\";\n\x1a\x45xpandCommentBranchRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\t\n\x01n\x18\x02 \x01(\x05\"9\n\x1b\x45xpandCommentBranchResponse\x12\x1a\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x08.Comment2\xf9\x02\n\x06Reddit\x12)\n\nCreatePost\x12\x12.CreatePostRequest\x1a\x05.Post\"\x00\x12%\n\x08VotePost\x12\x10.VotePostRequest\x1a\x05.Post\"\x00\x12#\n\x07GetPost\x12\x0f.GetPostRequest\x1a\x05.Post\"\x00\x12\x32\n\rCreateComment\x12\x15.CreateCommentRequest\x1a\x08.Comment\"\x00\x12.\n\x0bVoteComment\x12\x13.VoteCommentRequest\x1a\x08.Comment\"\x00\x12@\n\x0eGetTopComments\x12\x16.GetTopCommentsRequest\x1a\x14.TopCommentsResponse\"\x00\x12R\n\x13\x45xpandCommentBranch\x12\x1b.ExpandCommentBranchRequest\x1a\x1c.ExpandCommentBranchResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reddit_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=24
  _globals['_USER']._serialized_end=42
  _globals['_POST']._serialized_start=45
  _globals['_POST']._serialized_end=276
  _globals['_POST_STATE']._serialized_start=220
  _globals['_POST_STATE']._serialized_end=276
  _globals['_COMMENT']._serialized_start=279
  _globals['_COMMENT']._serialized_end=495
  _globals['_COMMENT_STATE']._serialized_start=451
  _globals['_COMMENT_STATE']._serialized_end=495
  _globals['_CREATEPOSTREQUEST']._serialized_start=497
  _globals['_CREATEPOSTREQUEST']._serialized_end=537
  _globals['_VOTEPOSTREQUEST']._serialized_start=539
  _globals['_VOTEPOSTREQUEST']._serialized_end=589
  _globals['_GETPOSTREQUEST']._serialized_start=591
  _globals['_GETPOSTREQUEST']._serialized_end=624
  _globals['_CREATECOMMENTREQUEST']._serialized_start=626
  _globals['_CREATECOMMENTREQUEST']._serialized_end=675
  _globals['_VOTECOMMENTREQUEST']._serialized_start=677
  _globals['_VOTECOMMENTREQUEST']._serialized_end=733
  _globals['_GETTOPCOMMENTSREQUEST']._serialized_start=735
  _globals['_GETTOPCOMMENTSREQUEST']._serialized_end=786
  _globals['_TOPCOMMENTSRESPONSE']._serialized_start=788
  _globals['_TOPCOMMENTSRESPONSE']._serialized_end=837
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_start=839
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_end=898
  _globals['_EXPANDCOMMENTBRANCHRESPONSE']._serialized_start=900
  _globals['_EXPANDCOMMENTBRANCHRESPONSE']._serialized_end=957
  _globals['_REDDIT']._serialized_start=960
  _globals['_REDDIT']._serialized_end=1337
# @@protoc_insertion_point(module_scope)
