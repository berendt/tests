def test_system_type(host):
    assert host.system_info.type == "linux"
