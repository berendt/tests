class TestElasticsearch(object):

    def test_elasticsearch_listens_on_9200(self, node, host):
        assert host.socket("tcp://%s:9200" % node["address"]).is_listening
