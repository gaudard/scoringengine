import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))

from scoring_engine.engine.config import Config


class TestConfig(object):

    def setup(self):
        self.config = Config(location="../../tests/scoring_engine/engine/example.conf")

    def test_checks_location(self):
        assert self.config.checks_location == "checks"

    def test_check_timeout(self):
        assert self.config.check_timeout == 30

    def test_db_host(self):
        assert self.config.db_host == "127.0.0.1"

    def test_db_port(self):
        assert self.config.db_port == 3306

    def test_db_username(self):
        assert self.config.db_username == "testuser"

    def test_db_password(self):
        assert self.config.db_password == "testpass"

    def test_redis_host(self):
        assert self.config.redis_host == "127.0.0.1"

    def test_redis_port(self):
        assert self.config.redis_port == 6379

    def test_redis_password(self):
        assert self.config.redis_password == "testpass"

    def test_redis_namespace(self):
        assert self.config.redis_namespace == "scoring_engine"

    def test_redis_queue_name(self):
        assert self.config.redis_queue_name == "checks"