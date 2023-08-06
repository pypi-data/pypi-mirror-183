import putki.discover as discover


def test_root_default():
    assert discover.root() == ''


def test_root_cwd_is_root():
    assert discover.root('.') == ''


def test_root_within_not_existing():
    assert discover.root('non-existing-path') == ''


def test_root_within_is_without():
    assert discover.root('/') == ''
