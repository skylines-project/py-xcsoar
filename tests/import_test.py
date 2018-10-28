def test_import():
    import xcsoar

    assert getattr(xcsoar, "Flight", None) != None
