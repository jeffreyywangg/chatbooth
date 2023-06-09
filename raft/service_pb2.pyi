from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticateRequest(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ["token", "username"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    token: str
    username: str
    def __init__(self, token: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class DeliverRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class EmptyResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ["request", "token"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    request: str
    token: str
    def __init__(self, token: _Optional[str] = ..., request: _Optional[str] = ...) -> None: ...

class RaftRequestVoteRequest(_message.Message):
    __slots__ = ["candidate_id", "term"]
    CANDIDATE_ID_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    candidate_id: str
    term: int
    def __init__(self, term: _Optional[int] = ..., candidate_id: _Optional[str] = ...) -> None: ...

class RaftRequestVoteResponse(_message.Message):
    __slots__ = ["vote"]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    vote: bool
    def __init__(self, vote: bool = ...) -> None: ...

class RaftUpdateStateRequest(_message.Message):
    __slots__ = ["data", "replica_id"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    replica_id: str
    def __init__(self, replica_id: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class SendRequest(_message.Message):
    __slots__ = ["body", "token", "username"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    body: str
    token: str
    username: str
    def __init__(self, token: _Optional[str] = ..., username: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...

class StringResponse(_message.Message):
    __slots__ = ["response", "success"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    response: str
    success: bool
    def __init__(self, success: bool = ..., response: _Optional[str] = ...) -> None: ...
