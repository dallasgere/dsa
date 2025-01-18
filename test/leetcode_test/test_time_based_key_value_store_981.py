import pytest
from src.leetcode.time_based_key_value_store_981 import (
    TimeBasedKeyValueStoreBruteOptimal,
)


@pytest.fixture
def store():
    return TimeBasedKeyValueStoreBruteOptimal()


def test_set_and_get(store):
    store.set("foo", "bar", 1)
    assert store.get("foo", 1) == "bar"
    assert store.get("foo", 2) == "bar"


def test_multiple_values_for_key(store):
    store.set("foo", "bar1", 1)
    store.set("foo", "bar2", 2)
    store.set("foo", "bar3", 3)
    assert store.get("foo", 1) == "bar1"
    assert store.get("foo", 2) == "bar2"
    assert store.get("foo", 3) == "bar3"
    assert store.get("foo", 4) == "bar3"


def test_get_nonexistent_key(store):
    assert store.get("nonexistent", 1) == ""


def test_get_before_first_timestamp(store):
    store.set("foo", "bar", 5)
    assert store.get("foo", 1) == ""


def test_multiple_keys(store):
    store.set("foo", "bar", 1)
    store.set("baz", "qux", 2)
    assert store.get("foo", 1) == "bar"
    assert store.get("baz", 2) == "qux"


def test_overwrite_value(store):
    store.set("foo", "bar1", 1)
    store.set("foo", "bar2", 1)
    assert store.get("foo", 1) == "bar2"


def test_large_number_of_entries(store):
    for i in range(1000):
        store.set(f"key{i}", f"value{i}", i)

    for i in range(1000):
        assert store.get(f"key{i}", i) == f"value{i}"
        assert store.get(f"key{i}", 1001) == f"value{i}"


def test_exact_timestamp_match(store):
    store.set("foo", "bar1", 1)
    store.set("foo", "bar2", 2)
    store.set("foo", "bar3", 3)
    assert store.get("foo", 2) == "bar2"


def test_between_timestamps(store):
    store.set("foo", "bar1", 1)
    store.set("foo", "bar3", 3)
    assert store.get("foo", 2) == "bar1"
