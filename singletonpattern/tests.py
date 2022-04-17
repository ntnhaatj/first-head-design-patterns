import unittest
from threading import Thread

from singletonpattern import native_singleton, threadsafe_singleton


class SingletonTestCase(unittest.TestCase):
    def test_native_singleton(self):
        db_connector_a = native_singleton.DBConnector('localhost', 5342)
        db_connector_b = native_singleton.DBConnector('localhost', 5342)
        self.assertEqual(id(db_connector_a), id(db_connector_b))
        setting = native_singleton.Settings('config.yaml')
        self.assertNotEqual(id(db_connector_a), id(setting))

    def test_threadsafe_when_instantiate_singleton(self):
        store = {}

        def db_client_multithreading(host, port):
            store[host] = threadsafe_singleton.DBConnector(host, port)

        thread_a = Thread(target=db_client_multithreading, args=('localhost', 5432))
        thread_b = Thread(target=db_client_multithreading, args=('127.0.0.1', 5432))
        thread_a.run()
        thread_b.run()
        self.assertEqual(store['localhost'], store['127.0.0.1'])


if __name__ == '__main__':
    unittest.main()
