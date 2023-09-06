import pytest
from Stack import Stack

def test_push(empty_stack):
    empty_stack.push(1)
    assert not empty_stack.is_empty()
    assert empty_stack.size() == 1

def test_pop(sample_stack):
    item = sample_stack.pop()
    assert item == 3
    assert sample_stack.size() == 2

def test_peek(sample_stack):
    item = sample_stack.peek()
    assert item == 3
    assert sample_stack.size() == 3

def test_is_empty(empty_stack):
    assert empty_stack.is_empty()

def test_size(sample_stack):
    assert sample_stack.size() == 3

def test_pop_from_empty_stack(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()

def test_peek_empty_stack(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.peek()

if __name__ == "__main__":
    pytest.main()
