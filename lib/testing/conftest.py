import pytest
from Stack import Stack

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def sample_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s
