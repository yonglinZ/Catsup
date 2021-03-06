from nose.tools import raises
from catsup.reader.meta import parse_meta, parse_catsup_meta, parse_yaml_meta


def test_catsup_meta_parser():
    meta_txt = """
    # Hello, world!

    - tags: hello, world
    """
    lines = [l.strip() for l in meta_txt.splitlines() if l]
    meta = parse_catsup_meta(lines)
    assert meta.title == "Hello, world!"
    assert meta.tags == "hello, world"


@raises(SystemExit)
def test_catsup_meta_parser_error_1():
    parse_catsup_meta(["fsdaf-,-,-,-", "fdsa- 0,"])


@raises(SystemExit)
def test_catsup_meta_parser_error_2():
    parse_catsup_meta(["#fsdaf-,-,-,-", "fdsa- 0,"])


def test_base_meta():
    pass


def test_meta_parser():
    meta_txt = """
    # Hello, world!

    - tags: hello, world
    """

    lines = [l.strip() for l in meta_txt.splitlines() if l]
    meta = parse_meta(lines)
    assert meta.title == "Hello, world!"
    assert meta.tags == "hello, world"


@raises(SystemExit)
def test_parse_unknown_meta():
    parse_meta(["fdsjaklfdsjaklfdsjaklfjdsklfjsa"])
